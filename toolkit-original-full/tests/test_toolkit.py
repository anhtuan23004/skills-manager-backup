"""Offline regression tests. No BTC API keys, network calls or third-party models."""
from __future__ import annotations
import base64, json, os, re, shutil, subprocess, sys, tempfile, unittest, zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'runtime'))
from common import ToolkitError,safe_path,write_new,json_bytes,snapshot,verify_snapshot,validate_live_permission,assert_not_frozen
from gateway import validate_base,validate_payload,call,save_result,BudgetError,GatewayError,AmbiguousCreationError
from media import probe,contact_sheet,normalize_video
from cli import freeze,package
from mcp_server import Server

class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.r=Path(self.tmp.name)
        (self.r/'final').mkdir();(self.r/'final'/'text.txt').write_text('Sản phẩm thử nghiệm',encoding='utf-8')
        (self.r/'ops').mkdir()
    def tearDown(self):self.tmp.cleanup()
    def permission(self,**kw):
        d={'mode':'practice','toolkit_scope_approved':True,'official_logging_verified':True,'agent_routes_only_btc':True}
        d.update(kw);(self.r/'ops'/'permission.json').write_bytes(json_bytes(d))
    def test_relative_path(self):self.assertEqual(safe_path(self.r,'final/text.txt'),self.r/'final/text.txt')
    def test_reject_unsafe_paths(self):
        for v in ['../secret','/etc/passwd','C:/secret','final/../../secret','.env','.ai-log/session.jsonl','scripts/x.py','final\\text.txt']:
            with self.subTest(v=v),self.assertRaises(ToolkitError):safe_path(self.r,v,exists=False)
    def test_reject_symlink(self):
        if not hasattr(os,'symlink'):self.skipTest('No symlink support')
        (self.r/'final'/'link').symlink_to(self.r/'final'/'text.txt')
        with self.assertRaises(ToolkitError):safe_path(self.r,'final/link')
    def test_no_overwrite(self):
        with self.assertRaises(FileExistsError):write_new(self.r/'final'/'text.txt',b'changed')
    def test_manifest_unchanged(self):
        m=snapshot(self.r);write_new(self.r/'ops'/'manifest.json',json_bytes(m))
        self.assertTrue(verify_snapshot(self.r,'ops/manifest.json')['unchanged'])
    def test_manifest_detects_changes(self):
        write_new(self.r/'ops'/'manifest.json',json_bytes(snapshot(self.r)))
        (self.r/'final'/'text.txt').write_text('changed');(self.r/'final'/'extra.txt').write_text('added')
        d=verify_snapshot(self.r,'ops/manifest.json');self.assertFalse(d['unchanged']);self.assertEqual(d['modified'],['final/text.txt']);self.assertEqual(d['added'],['final/extra.txt'])
    def test_manifest_no_whole_workspace(self):
        with self.assertRaises(ToolkitError):snapshot(self.r,'.')
    def test_permission_false(self):
        self.permission(official_logging_verified=False)
        with self.assertRaises(ToolkitError):validate_live_permission(self.r)
    def test_permission_practice(self):
        self.permission();self.assertEqual(validate_live_permission(self.r)['mode'],'practice')
    def test_expired_competition(self):
        self.permission(mode='competition',end_at=(datetime.now(timezone.utc)-timedelta(seconds=1)).isoformat())
        with self.assertRaises(ToolkitError):validate_live_permission(self.r)
    def test_naive_deadline_rejected(self):
        self.permission(mode='competition',end_at='2030-01-01T12:00:00')
        with self.assertRaises(ToolkitError):validate_live_permission(self.r)
    def test_freeze_blocks_generation(self):
        self.permission();freeze(str(self.r))
        with self.assertRaises(ToolkitError):validate_live_permission(self.r)
    def test_freeze_does_not_overwrite(self):
        freeze(str(self.r))
        with self.assertRaises(FileExistsError):freeze(str(self.r))
    def test_package_correct_version(self):
        freeze(str(self.r));out=package(str(self.r),'submission/final.zip')
        self.assertEqual(out['status'],'PACKAGED_NOT_SUBMITTED')
        with zipfile.ZipFile(self.r/'submission'/'final.zip') as z:
            self.assertIsNone(z.testzip());self.assertEqual(set(z.namelist()),{'final/text.txt','MANIFEST.json'})
    def test_package_refuses_modified(self):
        freeze(str(self.r));(self.r/'final'/'text.txt').write_text('new version')
        with self.assertRaises(ToolkitError):package(str(self.r),'submission/final.zip')

class GatewayTest(unittest.TestCase):
    def setUp(self):self.c={'base_url':'https://api.thucchien.ai/v1','allowed_models':['demo'],'allow_web_search':False}
    def test_allowed_base(self):self.assertEqual(validate_base('https://api.thucchien.ai/v1/'),'https://api.thucchien.ai/v1')
    def test_reject_bases(self):
        for url in ['http://api.thucchien.ai','https://api.openai.com/v1','https://api.thucchien.ai.evil.test','https://abc@api.thucchien.ai','https://api.thucchien.ai?key=x','https://api.thucchien.ai/v2']:
            with self.subTest(url=url),self.assertRaises(ToolkitError):validate_base(url)
    def test_unknown_model(self):
        with self.assertRaises(ToolkitError):validate_payload('text',{'model':'unapproved'},self.c)
    def test_video_seconds_explicit(self):
        with self.assertRaises(ToolkitError):validate_payload('video-create',{'model':'demo'},self.c)
        validate_payload('video-create',{'model':'demo','seconds':'4'},self.c)
    def test_image_n_one(self):
        with self.assertRaises(ToolkitError):validate_payload('image',{'model':'demo','n':2},self.c)
    def test_no_endpoint_injection(self):
        with self.assertRaises(ToolkitError):validate_payload('text',{'model':'demo','api_key':'secret'},self.c)
    def test_web_disabled(self):
        with self.assertRaises(ToolkitError):validate_payload('text',{'model':'demo','tools':[{'googleSearch':{}}]},self.c)
    def test_remote_media_blocked(self):
        with self.assertRaises(ToolkitError):validate_payload('text',{'model':'demo','messages':[{'content':[{'image_url':{'url':'https://example.org/image.png'}}]}]},self.c)
    def test_post_timeout_not_retried(self):
        calls=[]
        def sender(*a,**kw):calls.append(1);raise TimeoutError()
        with self.assertRaises(AmbiguousCreationError):call('text',{'model':'demo'},self.c,'placeholder',sender=sender)
        self.assertEqual(len(calls),1)
    def test_budget_not_retried(self):
        calls=[]
        def sender(*a,**kw):calls.append(1);return 429,{},b'Budget has been exceeded'
        with self.assertRaises(BudgetError):call('key-info',{},self.c,'placeholder',sender=sender,sleep=lambda _:None)
        self.assertEqual(len(calls),1)
    def test_get_rate_bounded_retry(self):
        calls=[]
        def sender(*a,**kw):
            calls.append(1);return (429,{},b'rate limited') if len(calls)<3 else (200,{},b'{}')
        meta,data=call('video-status',{},self.c,'placeholder',job_id='video_1',sender=sender,sleep=lambda _:None)
        self.assertEqual(len(calls),3);self.assertEqual(data,b'{}')
    def test_post_rate_not_retried(self):
        calls=[]
        def sender(*a,**kw):calls.append(1);return 429,{},b'rate limited'
        with self.assertRaises(GatewayError):call('text',{'model':'demo'},self.c,'placeholder',sender=sender)
        self.assertEqual(len(calls),1)
    def test_bad_video_id(self):
        with self.assertRaises(ToolkitError):call('video-status',{},self.c,'placeholder',job_id='../x',sender=lambda *a,**kw:None)
    def test_text_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);r=save_result('text',json_bytes({'choices':[{'message':{'content':'Bản thử'}}]}),p,{})
            self.assertEqual((p/r['output']).read_text('utf-8'),'Bản thử');self.assertEqual(len(r['sha256']),64)
    def test_empty_result_rejected(self):
        with tempfile.TemporaryDirectory() as tmp,self.assertRaises(GatewayError):
            save_result('text',json_bytes({'choices':[{'message':{'content':''}}]}),Path(tmp),{})
    def test_base64_image_saved(self):
        image=base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aN1sAAAAASUVORK5CYII=')
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);r=save_result('image',json_bytes({'data':[{'b64_json':base64.b64encode(image).decode()}]}),p,{})
            self.assertEqual((p/r['output']).read_bytes(),image)
    def test_key_info_does_not_persist_secrets(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=save_result('key-info',json_bytes({'info':{'key':'secret','spend':1,'max_budget':50}}),Path(tmp),{})
            self.assertNotIn('secret',json.dumps(r));self.assertEqual(r['key_info']['max_budget'],50)
    def test_default_cli_dry_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            r=Path(tmp);(r/'ops').mkdir();(r/'ops'/'gateway.json').write_bytes(json_bytes(self.c));(r/'payload.json').write_bytes(json_bytes({'model':'demo'}))
            p=subprocess.run([sys.executable,str(ROOT/'runtime'/'gateway.py'),'--root',str(r),'--op','text','--payload','payload.json'],capture_output=True,text=True,timeout=10)
            self.assertEqual(p.returncode,0,p.stderr);self.assertTrue(json.loads(p.stdout)['dry_run']);self.assertFalse((r/'runs').exists())

class MCPTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.r=Path(self.tmp.name);(self.r/'final').mkdir();(self.r/'final'/'a.txt').write_text('test');self.s=Server(str(self.r))
    def tearDown(self):self.tmp.cleanup()
    def initialize(self):
        r=self.s.handle({'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-11-25','capabilities':{},'clientInfo':{'name':'test','version':'1'}}})
        self.s.handle({'jsonrpc':'2.0','method':'notifications/initialized'});return r
    def test_preinit_tools_denied(self):self.assertIn('error',self.s.handle({'jsonrpc':'2.0','id':1,'method':'tools/list'}))
    def test_init_protocol(self):self.assertEqual(self.initialize()['result']['protocolVersion'],'2025-11-25')
    def test_exact_four_tools(self):
        self.initialize();r=self.s.handle({'jsonrpc':'2.0','id':2,'method':'tools/list'});self.assertEqual(len(r['result']['tools']),4)
    def test_manifest_call(self):
        self.initialize();r=self.s.handle({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'aitc_artifact_manifest','arguments':{'directory':'final'}}})
        self.assertFalse(r['result']['isError']);self.assertEqual(len(json.loads(r['result']['content'][0]['text'])['files']),1)
    def test_traversal_error(self):
        self.initialize();r=self.s.handle({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'aitc_artifact_manifest','arguments':{'directory':'../'}}})
        self.assertTrue(r['result']['isError'])
    def test_arbitrary_shell_not_exposed(self):
        self.initialize();r=self.s.handle({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'shell','arguments':{'command':'echo x'}}})
        self.assertIn('error',r)
    def test_extra_argument_rejected(self):
        self.initialize();r=self.s.handle({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'aitc_artifact_manifest','arguments':{'directory':'final','other':'x'}}})
        self.assertTrue(r['result']['isError'])
    def test_stdio_process_handshake_and_manifest(self):
        messages=[{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-11-25','capabilities':{},'clientInfo':{'name':'offline-test','version':'1'}}},{'jsonrpc':'2.0','method':'notifications/initialized'},{'jsonrpc':'2.0','id':2,'method':'tools/list'},{'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'aitc_artifact_manifest','arguments':{'directory':'final'}}}]
        p=subprocess.run([sys.executable,str(ROOT/'runtime'/'mcp_server.py'),'--root',str(self.r)],input='\n'.join(json.dumps(m) for m in messages)+'\n',capture_output=True,text=True,timeout=15)
        self.assertEqual(p.returncode,0,p.stderr);rows=[json.loads(l) for l in p.stdout.splitlines()]
        self.assertEqual(len(rows),3);self.assertFalse(rows[-1]['result']['isError'])

@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'),'FFmpeg and FFprobe required')
class MediaTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.r=Path(self.tmp.name);(self.r/'assets').mkdir()
        p=subprocess.run(['ffmpeg','-v','error','-f','lavfi','-i','testsrc2=size=320x180:rate=25','-f','lavfi','-i','sine=frequency=500:sample_rate=44100','-t','1','-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac',str(self.r/'assets'/'test.mp4')],capture_output=True,text=True,timeout=20)
        self.assertEqual(p.returncode,0,p.stderr)
    def tearDown(self):self.tmp.cleanup()
    def test_probe_real_media(self):
        r=probe(self.r,'assets/test.mp4');v=next(s for s in r['streams'] if s['codec_type']=='video');self.assertEqual(v['width'],320);self.assertIn('UNVERIFIED',r['content_quality'])
    def test_contact_sheet_real_media(self):
        r=contact_sheet(self.r,'assets/test.mp4','qa/contact.png',frames=3);self.assertGreater((self.r/r['path']).stat().st_size,100)
    def test_contact_sheet_wrong_folder(self):
        with self.assertRaises(ToolkitError):contact_sheet(self.r,'assets/test.mp4','final/contact.png',frames=3)
    def test_normalize_real_media(self):
        r=normalize_video(self.r,'assets/test.mp4','final/test.mp4',320,240,25);v=next(s for s in r['streams'] if s['codec_type']=='video');self.assertEqual((v['width'],v['height']),(320,240))
    def test_normalize_frozen_denied(self):
        (self.r/'ops').mkdir();(self.r/'ops'/'freeze.json').write_text('{}')
        with self.assertRaises(ToolkitError):normalize_video(self.r,'assets/test.mp4','final/test.mp4',320,240,25)

class SkillStructureTest(unittest.TestCase):
    def test_fifteen_skills_and_contracts(self):
        paths=list((ROOT/'skills').glob('*/SKILL.md'));self.assertEqual(len(paths),15)
        for p in paths:
            with self.subTest(skill=p.parent.name):
                text=p.read_text('utf-8');self.assertTrue(text.startswith('---\n'));head=text.split('---',2)[1]
                name=re.search(r'^name: (.+)$',head,re.M).group(1);desc=re.search(r'^description: (.+)$',head,re.M).group(1)
                self.assertEqual(name,p.parent.name);self.assertRegex(name,r'^[a-z0-9]+(?:-[a-z0-9]+)*$');self.assertLessEqual(len(name),64);self.assertLessEqual(len(desc),1024)
                self.assertTrue((p.parent/'references'/'contract.md').is_file());self.assertIn('## Đầu vào',text);self.assertIn('## Đầu ra bắt buộc',text);self.assertLess(len(text.splitlines()),500)
    def test_configs_valid_json(self):
        for p in (ROOT/'config').glob('*.json'):self.assertIsInstance(json.loads(p.read_text('utf-8')),dict)

if __name__=='__main__':unittest.main()
