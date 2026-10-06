"""Small, dependency-free MCP stdio server for LOCAL media QA only.
Protocol subset: initialize, initialized notification, ping, tools/list, tools/call.
No network, arbitrary shell, generic file writes, sampling, Git mutation or submission.
This is custom code, not an official MCP reference server or an OS security boundary.
"""
from __future__ import annotations
import argparse, json, os, sys
from common import ToolkitError, root_path, snapshot, verify_snapshot
from media import probe, contact_sheet
VERSIONS={'2025-11-25','2025-06-18','2025-03-26','2024-11-05'}

def schema(properties:dict,required:list[str]) -> dict:
    return {'type':'object','properties':properties,'required':required,'additionalProperties':False}
PATH={'type':'string','minLength':1,'maxLength':400}
TOOLS=[
 {'name':'aitc_media_probe','description':'Read technical metadata from an approved local media file. Does NOT judge semantic or visual quality.',
  'inputSchema':schema({'path':PATH},['path']), 'annotations':{'readOnlyHint':True,'destructiveHint':False,'openWorldHint':False}},
 {'name':'aitc_contact_sheet','description':'Create a NEW PNG of sampled video frames under qa/. Does not replace full viewing. No overwrite.',
  'inputSchema':schema({'path':PATH,'output':PATH,'frames':{'type':'integer','minimum':1,'maximum':16}},['path','output']),
  'annotations':{'readOnlyHint':False,'destructiveHint':False,'idempotentHint':False,'openWorldHint':False}},
 {'name':'aitc_artifact_manifest','description':'Calculate file sizes and SHA-256 for a specific artifact directory. Returns data only; does not submit or freeze.',
  'inputSchema':schema({'directory':PATH},['directory']), 'annotations':{'readOnlyHint':True,'destructiveHint':False,'openWorldHint':False}},
 {'name':'aitc_verify_manifest','description':'Compare current artifact files with a saved local manifest. Reports changed, added and removed files.',
  'inputSchema':schema({'manifest_path':PATH},['manifest_path']), 'annotations':{'readOnlyHint':True,'destructiveHint':False,'openWorldHint':False}}
]

def validate_args(s:dict,args:dict) -> None:
    if not isinstance(args,dict):raise ToolkitError('Tool arguments must be an object.')
    if set(args)-set(s['properties']):raise ToolkitError('Unexpected tool argument.')
    if set(s.get('required',[]))-set(args):raise ToolkitError('Missing required tool argument.')
    for k,v in args.items():
        p=s['properties'][k]
        if p['type']=='string':
            if not isinstance(v,str) or not p.get('minLength',0)<=len(v)<=p.get('maxLength',10000):raise ToolkitError(f'Invalid string argument: {k}')
        elif p['type']=='integer':
            if isinstance(v,bool) or not isinstance(v,int) or not p['minimum']<=v<=p['maximum']:raise ToolkitError(f'Invalid integer argument: {k}')

class Server:
    def __init__(self,root:str):self.root=root_path(root);self.started=False;self.ready=False
    def handle(self,m):
        if not isinstance(m,dict) or m.get('jsonrpc')!='2.0' or not isinstance(m.get('method'),str):
            return self.error(None,-32600,'Invalid JSON-RPC request')
        method=m['method'];rid=m.get('id');params=m.get('params',{})
        if 'id' not in m:
            if method=='notifications/initialized' and self.started:self.ready=True
            return None
        if not isinstance(params,dict):return self.error(rid,-32602,'params must be an object')
        if method=='initialize':
            if self.started:return self.error(rid,-32600,'Already initialized')
            version=params.get('protocolVersion')
            if not isinstance(version,str) or not isinstance(params.get('capabilities',{}),dict) or not isinstance(params.get('clientInfo'),dict):
                return self.error(rid,-32602,'Expected protocolVersion, capabilities and clientInfo')
            self.started=True
            return self.ok(rid,{'protocolVersion':version if version in VERSIONS else '2025-11-25',
                'capabilities':{'tools':{'listChanged':False}},'serverInfo':{'name':'aitc-local-media-qa','version':'1.0.0'},
                'instructions':'Local technical checks only. Use a Gateway-BTC-routed host. Never infer content PASS from metadata.'})
        if method=='ping':return self.ok(rid,{})
        if not self.ready:return self.error(rid,-32002,'Initialize and send notifications/initialized first')
        if method=='tools/list':
            if params.get('cursor'):return self.error(rid,-32602,'No pagination cursor is supported for this fixed list')
            return self.ok(rid,{'tools':TOOLS})
        if method=='tools/call':
            tool=next((t for t in TOOLS if t['name']==params.get('name')),None)
            if not tool:return self.error(rid,-32602,'Unknown tool')
            args=params.get('arguments',{})
            try:
                validate_args(tool['inputSchema'],args)
                name=tool['name']
                if name=='aitc_media_probe':out=probe(self.root,**args)
                elif name=='aitc_contact_sheet':out=contact_sheet(self.root,**args)
                elif name=='aitc_artifact_manifest':out=snapshot(self.root,**args)
                else:out=verify_snapshot(self.root,**args)
                return self.ok(rid,{'content':[{'type':'text','text':json.dumps(out,ensure_ascii=False)}],'isError':False})
            except Exception as e:
                return self.ok(rid,{'content':[{'type':'text','text':f'{type(e).__name__}: {str(e)[:1800]}'}],'isError':True})
        return self.error(rid,-32601,'Method not supported by this local tools-only server')
    @staticmethod
    def ok(rid,data):return {'jsonrpc':'2.0','id':rid,'result':data}
    @staticmethod
    def error(rid,code,msg):return {'jsonrpc':'2.0','id':rid,'error':{'code':code,'message':msg}}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',default=os.environ.get('AITC_WORKSPACE_ROOT'));a=p.parse_args()
    if not a.root:p.error('--root or AITC_WORKSPACE_ROOT is required')
    server=Server(a.root)
    for stream in (sys.stdin,sys.stdout):
        if hasattr(stream,'reconfigure'):stream.reconfigure(encoding='utf-8')
    while True:
        line=sys.stdin.buffer.readline(1_000_002)
        if not line:break
        if len(line)>1_000_000:
            # Close rather than continue on partial oversized messages.
            print(json.dumps(server.error(None,-32700,'Message exceeds local limit')),flush=True);break
        try:msg=json.loads(line.decode('utf-8'));out=server.handle(msg)
        except (ValueError,UnicodeDecodeError):out=server.error(None,-32700,'Invalid UTF-8 JSON')
        if out is not None:print(json.dumps(out,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
