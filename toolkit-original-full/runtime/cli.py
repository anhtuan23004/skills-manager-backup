"""Human-operated manifest/freeze/package helpers. Never mutates Git or BTC logs."""
from __future__ import annotations
import argparse, json, sys, zipfile
from pathlib import Path
from common import ToolkitError, root_path, safe_path, snapshot, verify_snapshot, write_new, json_bytes

def freeze(root:str,directory:str='final')->dict:
    r=root_path(root);m=snapshot(r,directory)
    out=safe_path(r,'ops/freeze.json',exists=False);write_new(out,json_bytes(m))
    return {'frozen_manifest':'ops/freeze.json','files':len(m['files']),'note':'Does not submit, commit or provide trusted timing evidence.'}

def package(root:str,output:str)->dict:
    r=root_path(root);v=verify_snapshot(r,'ops/freeze.json')
    if not v['unchanged']:raise ToolkitError('Final files changed since freeze; do not package a different version as the approved one.')
    m=json.loads((r/'ops/freeze.json').read_text('utf-8'))
    # Conservative total uncompressed threshold; actual portal rules still govern.
    if m['total_bytes']>500_000_000:raise ToolkitError('Artifact total exceeds 500 MB training attachment limit.')
    p=safe_path(r,output,exists=False)
    if p.suffix.lower()!='.zip' or p.exists():raise ToolkitError('Choose a NEW ZIP output path.')
    if p.is_relative_to(safe_path(r,m['directory'])):raise ToolkitError('ZIP must be outside the final artifact folder.')
    p.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(p,'x',compression=zipfile.ZIP_DEFLATED) as z:
        for item in m['files']:
            src=safe_path(r,item['path']);z.write(src,item['path'])
        z.writestr('MANIFEST.json',json_bytes(m))
    if p.stat().st_size>500_000_000:raise ToolkitError('ZIP exceeds 500 MB. It was created but must NOT be submitted under that limit.')
    return {'zip':output,'bytes':p.stat().st_size,'status':'PACKAGED_NOT_SUBMITTED',
            'note':'Use ZIP only if the actual prompt/portal accepts it. Source/prompts stay in BTC repo; recordings are separate.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',required=True)
    sub=p.add_subparsers(dest='op',required=True)
    a=sub.add_parser('manifest');a.add_argument('--directory',default='final');a.add_argument('--output',default='qa/manifest.json')
    a=sub.add_parser('freeze');a.add_argument('--directory',default='final')
    a=sub.add_parser('verify');a.add_argument('--manifest',default='ops/freeze.json')
    a=sub.add_parser('package');a.add_argument('--output',default='submission/final.zip')
    a=p.parse_args()
    if a.op=='manifest':
        obj=snapshot(a.root,a.directory);out=safe_path(a.root,a.output,exists=False)
        if out.is_relative_to(safe_path(a.root,a.directory)):raise ToolkitError('Write manifest outside the artifact directory.')
        write_new(out,json_bytes(obj))
    elif a.op=='freeze':obj=freeze(a.root,a.directory)
    elif a.op=='verify':obj=verify_snapshot(a.root,a.manifest)
    else:obj=package(a.root,a.output)
    print(json.dumps(obj,ensure_ascii=False,indent=2))
if __name__=='__main__':
    try:main()
    except (ToolkitError,ValueError,OSError,KeyError) as e:print(str(e),file=sys.stderr);sys.exit(2)
