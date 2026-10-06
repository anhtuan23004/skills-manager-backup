"""Bounded local media inspection; requires preinstalled FFmpeg and FFprobe."""
from __future__ import annotations
import argparse, json, math, shutil, subprocess, sys
from pathlib import Path
from common import ToolkitError, safe_path, assert_not_frozen
MEDIA = {'.png','.jpg','.jpeg','.webp','.mp4','.mov','.mkv','.wav','.mp3','.m4a','.aac','.ogg','.webm'}

def run_program(program: str, args: list[str], timeout: int = 60) -> str:
    exe = shutil.which(program)
    if not exe:
        raise ToolkitError(f'{program} not found. Install and rehearse before the competition.')
    p = subprocess.run([exe, *args], capture_output=True, text=True, encoding='utf-8', errors='replace',
                       timeout=timeout, shell=False)
    if p.returncode:
        raise ToolkitError(f'{program} failed: {p.stderr[-1800:]}')
    return p.stdout

def media_input(root: str | Path, path: str) -> Path:
    p = safe_path(root, path)
    if not p.is_file() or p.suffix.lower() not in MEDIA:
        raise ToolkitError('Expected a supported local media file.')
    if p.stat().st_size > 1_000_000_000:
        raise ToolkitError('Input exceeds the tool safety limit of 1 GB.')
    return p

def probe(root: str | Path, path: str) -> dict:
    p = media_input(root,path)
    raw = run_program('ffprobe',['-v','error','-protocol_whitelist','file,pipe','-show_format','-show_streams','-of','json',str(p)])
    d = json.loads(raw)
    # Return bounded technical data, not arbitrary embedded metadata instructions.
    keep = {'index','codec_name','codec_type','width','height','sample_rate','channels','r_frame_rate','avg_frame_rate','duration','pix_fmt'}
    fmt = d.get('format',{})
    return {'path':path, 'bytes':p.stat().st_size,
            'format':{k:fmt[k] for k in ('format_name','duration','bit_rate') if k in fmt},
            'streams':[{k:v for k,v in s.items() if k in keep} for s in d.get('streams',[])],
            'content_quality':'UNVERIFIED — metadata does not prove visual, audio, or brief compliance.'}

def contact_sheet(root: str | Path, path: str, output: str, frames: int = 9, columns: int = 3, tile_width: int = 400) -> dict:
    if isinstance(frames,bool) or not 1 <= frames <= 16 or not 1 <= columns <= 4 or not 120 <= tile_width <= 800:
        raise ToolkitError('Use frames 1–16, columns 1–4, tile_width 120–800.')
    p = media_input(root,path); out = safe_path(root,output,exists=False)
    if out.suffix.lower() != '.png' or out.exists():
        raise ToolkitError('Output must be a new PNG path. Existing files are never overwritten.')
    if Path(output).parts[0] != 'qa':
        raise ToolkitError('Contact sheets may only be written under qa/.')
    d = probe(root,path); dur = float(d.get('format',{}).get('duration',0))
    if not math.isfinite(dur) or dur <= 0:
        raise ToolkitError('Contact sheet requires media with a finite positive duration.')
    rows = math.ceil(frames/columns)
    # Derived numeric filter only; do not accept arbitrary user-provided filters or shells.
    filt = f'fps={frames/dur:.8f},scale={tile_width}:-2,tile={columns}x{rows}:nb_frames={frames}'
    out.parent.mkdir(parents=True,exist_ok=True)
    run_program('ffmpeg',['-v','error','-n','-protocol_whitelist','file,pipe','-i',str(p),'-an','-vf',filt,'-frames:v','1',str(out)],120)
    if not out.exists() or not out.stat().st_size:
        raise ToolkitError('No contact sheet was created.')
    return {'path':output,'frames_requested':frames,'note':'Frames are sampled. Watch the full clip and listen separately.'}

def normalize_video(root: str | Path, path: str, output: str, width: int, height: int, fps: int = 25) -> dict:
    assert_not_frozen(root)
    if width % 2 or height % 2 or not 128<=width<=3840 or not 128<=height<=3840 or fps not in (24,25,30,60):
        raise ToolkitError('Use even dimensions 128–3840 and fps 24/25/30/60, from the actual brief.')
    src = media_input(root,path); out = safe_path(root,output,exists=False)
    if out.exists() or out.suffix.lower() != '.mp4':
        raise ToolkitError('Output must be a new MP4.')
    out.parent.mkdir(parents=True,exist_ok=True)
    vf = f'scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1'
    run_program('ffmpeg',['-v','error','-n','-protocol_whitelist','file,pipe','-i',str(src),'-map','0:v:0','-map','0:a?',
                          '-vf',vf,'-r',str(fps),'-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-c:a','aac',
                          '-movflags','+faststart',str(out)],300)
    return probe(root,output)

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',required=True)
    sub=p.add_subparsers(dest='op',required=True)
    a=sub.add_parser('probe');a.add_argument('path')
    a=sub.add_parser('contact-sheet');a.add_argument('path');a.add_argument('output');a.add_argument('--frames',type=int,default=9)
    a=sub.add_parser('normalize-video');a.add_argument('path');a.add_argument('output');a.add_argument('--width',type=int,required=True);a.add_argument('--height',type=int,required=True);a.add_argument('--fps',type=int,default=25)
    args=p.parse_args()
    try:
        if args.op=='probe': r=probe(args.root,args.path)
        elif args.op=='contact-sheet':r=contact_sheet(args.root,args.path,args.output,args.frames)
        else:r=normalize_video(args.root,args.path,args.output,args.width,args.height,args.fps)
        print(json.dumps(r,ensure_ascii=False,indent=2))
    except (ToolkitError,ValueError,OSError,subprocess.TimeoutExpired) as e:
        print(str(e),file=sys.stderr);sys.exit(2)
