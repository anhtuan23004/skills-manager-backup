"""BTC-only API utility. Default: validate/dry-run, not a network call.
Supplemental run records never replace or alter official BTC logs.
"""
from __future__ import annotations
import argparse, base64, json, mimetypes, os, re, socket, sys, time, uuid
from pathlib import Path
from urllib.request import Request, build_opener, HTTPRedirectHandler, ProxyHandler
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, quote
from common import ToolkitError, safe_path, root_path, write_new, json_bytes, utc_now, hash_file, validate_live_permission

ROUTES = {'text':('POST','/chat/completions'), 'responses':('POST','/responses'),
          'image':('POST','/images/generations'), 'video-create':('POST','/videos'),
          'tts':('POST','/audio/speech'), 'stt':('POST','/audio/transcriptions'),
          'embedding':('POST','/embeddings'), 'video-status':('GET','/videos/{id}'),
          'video-download':('GET','/videos/{id}/content'), 'key-info':('GET','/key/info')}
class GatewayError(ToolkitError): pass
class BudgetError(GatewayError): pass
class AmbiguousCreationError(GatewayError): pass

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def validate_base(base: str) -> str:
    u=urlsplit(base)
    if u.scheme!='https' or u.hostname!='api.thucchien.ai' or u.username or u.password or u.port not in (None,443) or u.query or u.fragment or u.path.rstrip('/') not in ('','/v1'):
        raise ToolkitError('Only https://api.thucchien.ai with optional /v1 is allowed.')
    return base.rstrip('/')

def classify_error(status: int, body: bytes) -> str:
    text=body.decode('utf-8',errors='replace').lower()
    if status==429 and any(x in text for x in ('budget','hạn mức','ngân sách')):return 'budget'
    if status==429:return 'rate'
    if status==401:return 'authentication'
    if status==403:return 'permission_or_model'
    if status==400:return 'request_schema'
    return 'gateway'

def transport(method: str, url: str, headers: dict, body: bytes | None, timeout: int = 120):
    # No environment proxy and no redirects: do not forward a BTC key to another host.
    opener=build_opener(ProxyHandler({}),NoRedirect())
    try:
        with opener.open(Request(url,data=body,headers=headers,method=method),timeout=timeout) as r:
            data=r.read(512_000_001)
            if len(data)>512_000_000:raise GatewayError('Response exceeds 512 MB utility limit.')
            return r.status,dict(r.headers),data
    except HTTPError as e:
        return e.code,dict(e.headers),e.read(100_000)

def validate_payload(op: str, payload: dict, config: dict) -> None:
    if op not in ROUTES:raise ToolkitError('Unsupported operation.')
    if not isinstance(payload,dict):raise ToolkitError('Payload must be a JSON object.')
    if ROUTES[op][0]=='GET':return
    model=payload.get('model')
    if not isinstance(model,str) or model not in config.get('allowed_models',[]):
        raise ToolkitError('Model must be in the team-reviewed allowlist in ops/gateway.json.')
    forbidden={'api_key','authorization','headers','base_url','endpoint','api_base','token'}
    if forbidden & {k.lower() for k in payload}:raise ToolkitError('Credentials/endpoint overrides do not belong in a payload.')
    if op=='image' and payload.get('n',1)!=1:raise ToolkitError('BTC image guide uses n=1.')
    if op=='video-create' and str(payload.get('seconds','')) not in {'4','6','8'}:
        raise ToolkitError('Specify video seconds explicitly as 4, 6, or 8 per the supplied BTC guide.')
    tools=payload.get('tools',[])
    if tools:
        if config.get('allow_web_search') is not True:raise ToolkitError('Search is disabled; confirm permission before enabling.')
        if not isinstance(tools,list):raise ToolkitError('tools must be a list.')
        for t in tools:
            if not isinstance(t,dict) or not (set(t)=={'googleSearch'} or (t.get('type')=='web_search' and set(t)=={'type'})):
                raise ToolkitError('Only the explicitly enabled BTC grounding tool is allowed here.')
    def walk(v):
        if isinstance(v,dict):
            for k,x in v.items():
                if k in {'url','image_url'} and isinstance(x,str) and not x.startswith('data:image/'):
                    raise ToolkitError('Use approved local images encoded as data URLs, not remote media URLs.')
                walk(x)
        elif isinstance(v,list):
            for x in v:walk(x)
    walk(payload)

def multipart(payload: dict, field: str, p: Path) -> tuple[bytes,str]:
    if p.stat().st_size>40_000_000:raise ToolkitError('Upload exceeds 40 MB helper limit.')
    if field not in {'file','input_reference'}:raise ToolkitError('Unsupported multipart field.')
    boundary='aitc'+uuid.uuid4().hex
    parts=[]
    for k,v in payload.items():
        if not re.fullmatch(r'[a-zA-Z0-9_]+',k):raise ToolkitError('Invalid multipart field name.')
        if isinstance(v,(dict,list)):raise ToolkitError('Multipart utility expects scalar payload fields.')
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    # Fixed safe filename avoids quoting/control-character injection from user filenames.
    suffix=p.suffix.lower() if re.fullmatch(r'\.[a-z0-9]{1,8}',p.suffix.lower()) else '.bin'
    mime=mimetypes.guess_type('upload'+suffix)[0] or 'application/octet-stream'
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{field}"; filename="upload{suffix}"\r\nContent-Type: {mime}\r\n\r\n'.encode()+p.read_bytes()+b'\r\n')
    parts.append(f'--{boundary}--\r\n'.encode())
    return b''.join(parts),f'multipart/form-data; boundary={boundary}'

def call(op: str, payload: dict, config: dict, key: str, *, job_id: str='', attachment: Path | None=None,
         sender=transport, sleep=time.sleep) -> tuple[dict,bytes]:
    validate_payload(op,payload,config)
    base=validate_base(config.get('base_url','https://api.thucchien.ai/v1'))
    method,path=ROUTES[op]
    if '{id}' in path:
        if not job_id or len(job_id)>1000 or not re.fullmatch(r'[A-Za-z0-9_=.:-]+',job_id):raise ToolkitError('Invalid video job ID.')
        path=path.replace('{id}',quote(job_id,safe=''))
    url=('https://api.thucchien.ai' if op=='key-info' else base)+path
    if not key or '\r' in key or '\n' in key:raise ToolkitError('Missing or invalid API key environment variable.')
    headers={'Authorization':'Bearer '+key,'Accept':'application/json'}
    body=None
    if method=='POST':
        if attachment is not None:
            field='input_reference' if op=='video-create' else 'file' if op=='stt' else ''
            if not field:raise ToolkitError('Attachments supported only for video-create and stt.')
            body,ctype=multipart(payload,field,attachment)
        else:
            if op=='stt':raise ToolkitError('STT requires --attachment.')
            body=json_bytes(payload);ctype='application/json'
        headers['Content-Type']=ctype
    for attempt in range(3 if method=='GET' else 1):
        try:
            status,rh,data=sender(method,url,headers,body,timeout=120)
        except (URLError,TimeoutError,ConnectionError,socket.timeout) as e:
            if method=='POST':
                raise AmbiguousCreationError('POST transport failed; creation/charge may have occurred. No automatic retry. Inspect saved run and BTC status.') from e
            if attempt==2:raise GatewayError('GET failed after bounded retries.') from e
            sleep(2**attempt);continue
        kind=classify_error(status,data)
        if status==429 and kind=='budget':raise BudgetError('BTC budget exhausted; waiting/retrying will not restore budget.')
        if method=='GET' and status in (429,500,502,503,504) and attempt<2:
            sleep(2**attempt);continue
        if not 200<=status<300:
            # Error bodies can contain keys/prompts; do not echo them automatically.
            raise GatewayError(f'HTTP {status} ({kind}); inspect BTC docs/status. No automatic POST retry.')
        h={k.lower():v for k,v in rh.items()}
        return {'status':status,'content_type':h.get('content-type',''),
                'request_id':h.get('x-request-id') or h.get('request-id'),
                'cost_header':h.get('x-litellm-response-cost')},data
    raise GatewayError('Retry limit reached.')

def image_ext(b: bytes) -> str:
    if b.startswith(b'\x89PNG\r\n\x1a\n'):return '.png'
    if b.startswith(b'\xff\xd8\xff'):return '.jpg'
    if b[:4]==b'RIFF' and b[8:12]==b'WEBP':return '.webp'
    raise ToolkitError('Unrecognized image bytes; do not assume the generated file is a PNG.')

def save_result(op: str, data: bytes, run: Path, meta: dict) -> dict:
    result=dict(meta)
    if op in {'tts','video-download'}:
        if data.lstrip().startswith((b'{',b'[')):raise GatewayError('Expected media bytes but received JSON.')
        c=meta.get('content_type','').lower()
        if op=='video-download': ext='.mp4'
        elif data.startswith(b'RIFF') and data[8:12]==b'WAVE':ext='.wav'
        elif data.startswith(b'ID3') or (len(data)>1 and data[0]==255 and data[1]&224==224):ext='.mp3'
        elif 'wav' in c:ext='.wav'
        elif 'mpeg' in c:ext='.mp3'
        else:ext='.bin'
        p=run/('output'+ext);write_new(p,data);result['output']=p.name
        result['verify_media']='Run media probe and listen/watch; do not assume suffix proves codec.'
    else:
        try:d=json.loads(data)
        except (ValueError,UnicodeDecodeError) as e:raise GatewayError('Expected JSON but response was not valid JSON.') from e
        if op=='image':
            rows=d.get('data') or []
            if not rows or not rows[0].get('b64_json'):raise GatewayError('No base64 image found at data[0].b64_json.')
            try:binary=base64.b64decode(rows[0]['b64_json'],validate=True)
            except Exception as e:raise GatewayError('Invalid image base64.') from e
            p=run/('output'+image_ext(binary));write_new(p,binary);result['output']=p.name
        elif op=='text':
            try:content=d['choices'][0]['message']['content']
            except (KeyError,IndexError,TypeError) as e:raise GatewayError('No text content in completion.') from e
            if not isinstance(content,str) or not content.strip():raise GatewayError('Empty or non-text response; check model and token budget.')
            write_new(run/'output.txt',content.encode('utf-8'));result['output']='output.txt'
        elif op=='responses':
            parts=[c.get('text','') for item in d.get('output',[]) if item.get('type')=='message' for c in item.get('content',[]) if c.get('type')=='output_text']
            text=d.get('output_text') or '\n'.join(parts)
            if not text:raise GatewayError('No output_text found in Responses result.')
            write_new(run/'output.txt',text.encode('utf-8'));result['output']='output.txt'
        elif op=='key-info':
            # Key inspection can return secret fields. Persist only safe budget/status fields.
            allowed={'spend','max_budget','blocked','expires','rpm_limit','tpm_limit','max_parallel_requests'}
            info=d.get('info',d)
            result['key_info']={k:v for k,v in info.items() if k in allowed} if isinstance(info,dict) else {}
        else:
            write_new(run/'output.json',json_bytes(d));result['output']='output.json'
        for k in ('usage','id','status'):
            if k in d:result[k]=d[k]
    result['completed_at']=utc_now()
    if result.get('output'):
        p=run/result['output'];result['sha256']=hash_file(p);result['bytes']=p.stat().st_size
    return result

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',required=True);p.add_argument('--op',required=True,choices=ROUTES)
    p.add_argument('--payload');p.add_argument('--job-id',default='');p.add_argument('--attachment');p.add_argument('--machine',choices=['A','B'],default='A');p.add_argument('--live',action='store_true')
    a=p.parse_args();r=root_path(a.root)
    config=json.loads(safe_path(r,'ops/gateway.json').read_text('utf-8'))
    payload=json.loads(safe_path(r,a.payload).read_text('utf-8')) if a.payload else {}
    validate_payload(a.op,payload,config);base=validate_base(config['base_url'])
    if not a.live:
        print(json.dumps({'dry_run':True,'operation':a.op,'base_url':base,'model':payload.get('model'),
                          'note':'No HTTP call and no paid task. This is not a live integration test.'},ensure_ascii=False,indent=2));return 0
    validate_live_permission(r)
    if os.getenv('AITC_ENABLE_NETWORK')!='YES':raise ToolkitError('Set AITC_ENABLE_NETWORK=YES explicitly after human checks.')
    key=os.getenv('AITC_API_KEY','')
    if not key:raise ToolkitError('Set AITC_API_KEY in the process environment, not a prompt.')
    encoded=json.dumps(payload,ensure_ascii=False)
    if key in encoded:raise ToolkitError('API key detected inside payload; remove it before logging/calling.')
    attachment=safe_path(r,a.attachment) if a.attachment else None
    run=r/'runs'/(a.machine+'-'+uuid.uuid4().hex)
    run.mkdir(parents=True)
    record={'started_at':utc_now(),'machine':a.machine,'operation':a.op,'payload':payload,'job_id':a.job_id,
            'attachment':a.attachment,'supplemental_only':True}
    if attachment:record['attachment_sha256']=hash_file(attachment)
    write_new(run/'request.json',json_bytes(record))
    try:
        meta,data=call(a.op,payload,config,key,job_id=a.job_id,attachment=attachment)
        result=save_result(a.op,data,run,meta)
        write_new(run/'result.json',json_bytes(result))
    except Exception as e:
        write_new(run/'failure.json',json_bytes({'at':utc_now(),'error_type':type(e).__name__,
                   'status':'AMBIGUOUS' if isinstance(e,AmbiguousCreationError) else 'FAILED',
                   'note':'Original BTC logs are not changed. Do not retry paid creation blindly.'}))
        raise
    result['run_directory']=run.relative_to(r).as_posix()
    print(json.dumps(result,ensure_ascii=False,indent=2));return 0

if __name__=='__main__':
    try:sys.exit(main())
    except (ToolkitError,ValueError,OSError) as e:
        print(str(e),file=sys.stderr);sys.exit(2)
