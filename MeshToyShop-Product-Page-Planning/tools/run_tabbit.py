"""Run a saved read-only research program through the stable Tabbit launcher."""
from pathlib import Path
import argparse,json,subprocess
p=argparse.ArgumentParser();p.add_argument('program');p.add_argument('request');p.add_argument('--tab');a=p.parse_args()
root=Path(__file__).resolve().parents[1]
args=[r'C:\Users\iamar\AppData\Local\Tabbit\LocalAgent\bin\tabbit-cli.exe','nodejs','--task','Mesh product research','--request-id',a.request]
if a.tab:args+=['--tab',a.tab]
r=subprocess.run(args,input=Path(a.program).read_text(encoding='utf-8'),capture_output=True,encoding='utf-8')
(root/'data'/f'{a.request}-receipt.json').write_text(r.stdout,encoding='utf-8')
try:
    j=json.loads(r.stdout);print(json.dumps(j,ensure_ascii=True))
except Exception:print(r.stdout)
if r.stderr:print(r.stderr)
