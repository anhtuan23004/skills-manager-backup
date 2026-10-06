"""Print local MCP configuration. Does not edit host config, BTC repo, or permissions."""
import argparse,json,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--root',required=True,help='Dedicated existing competition work folder')
a=p.parse_args();root=Path(a.root).expanduser().resolve()
if not root.is_dir():p.error('Workspace root must already exist')
server=Path(__file__).resolve().with_name('mcp_server.py')
print(json.dumps({'mcpServers':{'aitc-local-media-qa':{'command':sys.executable,'args':[str(server),'--root',str(root)]}}},ensure_ascii=False,indent=2))
