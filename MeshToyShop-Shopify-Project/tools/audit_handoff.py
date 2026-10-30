"""Deep, non-destructive handoff audit. Pillow is used only to decode/read images."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib,json,re,shutil,subprocess,sys,tempfile,unicodedata
import xml.etree.ElementTree as ET
from PIL import Image

P=Path(__file__).resolve().parents[1]
def read(name):return json.loads((P/name).read_text(encoding='utf-8'))
def normal(s):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s).replace('’',"'")).strip()
errors=[];decoded=[]
assets=read('data/asset-manifest.json'); slots=read('data/asset-slots.json')
design=read('data/design-manifest.json'); content=read('data/content.json'); products=read('data/product-map.json')
for a in assets:
    file=P/a['path']
    try:
        if file.suffix=='.svg':
            root=ET.parse(file).getroot()
            external=[v for el in root.iter() for k,v in el.attrib.items() if k.endswith('href') and not v.startswith(('#','data:'))]
            if external:errors.append('SVG depends on external resource: '+a['path'])
            dimensions='vector'
        else:
            with Image.open(file) as im:
                im.load(); dimensions=list(im.size)
                if dimensions!=[a['width'],a['height']]:errors.append('Dimension mismatch: '+a['path'])
        decoded.append(dict(path=a['path'],decoded=True,dimensions=dimensions))
    except Exception as e:errors.append('Cannot decode '+a['path']+': '+str(e))

routes=read('data/routes-and-actions.json')
product_keys={x['key'] for x in products['products']}
route_keys=set(routes['bindings'])
section_keys={x['id'] for x in design['sections']}
for a in routes['actions']:
    if a['section'] not in section_keys:errors.append('Unknown action section: '+a['id'])
    if a.get('binding') and a['binding'] not in route_keys:errors.append('Unknown binding: '+a['id'])
    if a.get('product') and a['product'] not in product_keys:errors.append('Unknown product: '+a['id'])
for x in content['categories']:
    if x['destination'] not in route_keys:errors.append('Unresolved category alias: '+x['destination'])
if content['announcement']['destination'] not in route_keys:errors.append('Unresolved announcement alias')

copydoc=normal((P/'docs/05-content-and-destinations.md').read_text(encoding='utf-8'))
locked=[]
for key in ['hero','discovery','shared_play','creative_play','video','growth','stories','faq']:
    for field in ['heading','body']:
        if field in content[key]:locked.append(content[key][field])
for x in content['categories']:locked.extend([x['title'],x['description']])
for x in content['discovery']['products']:locked.extend([x['title'],x['description'],x['tag']])
for x in content['growth']['modules']:locked.extend([x['title'],x['body'],x['label']])
for x in content['faq']['questions']:locked.append(x['question'])
locked.append(content['faq']['questions'][0]['answer'])
for text in locked:
    if normal(text) not in copydoc:errors.append('Visible copy missing from copy registry: '+text)

class Resources(HTMLParser):
    def __init__(self):super().__init__();self.references=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'src' in a:self.references.append(a['src'])
        if tag=='link' and 'href' in a:self.references.append(a['href'])
        if tag=='img' and 'srcset' in a:self.references.extend(x.strip().split(' ')[0] for x in a['srcset'].split(','))
resource_count=0
for f in P.rglob('*.html'):
    parser=Resources();parser.feed(f.read_text(encoding='utf-8'))
    for ref in parser.references:
        resource_count+=1
        if urlsplit(ref).scheme or ref.startswith('//'):errors.append('Nonlocal HTML runtime resource: '+str(f.relative_to(P))+' -> '+ref)

original_hashes={x['path']:hashlib.sha256((P/x['path']).read_bytes()).hexdigest() for x in design['mockups']}
if not (P/'verification/deep-audit.json').exists():
    (P/'verification/deep-audit.json').write_text('{"passed": false, "status": "audit in progress"}\n',encoding='utf-8')
temp_base=Path(tempfile.gettempdir()).resolve()
temp_root=Path(tempfile.mkdtemp(prefix='mesh-handoff-portability-')).resolve()
assert temp_root.parent==temp_base and temp_root.name.startswith('mesh-handoff-portability-')
try:
    relocated=temp_root/'different-name-with-spaces'
    shutil.copytree(P,relocated,ignore=shutil.ignore_patterns('__pycache__'))
    result=subprocess.run([sys.executable,str(relocated/'tools/validate_package.py')],capture_output=True,text=True,encoding='utf-8')
    relocation=dict(passed=result.returncode==0,folder_name_changed=True,original_workspace_required=False,stdout=result.stdout.strip(),stderr=result.stderr.strip())
    if result.returncode:errors.append('Relocated package validation failed')
    for rel,h in original_hashes.items():
        if hashlib.sha256((relocated/rel).read_bytes()).hexdigest()!=h:errors.append('Relocation changed reference '+rel)
finally:
    # Only the newly created, verified audit directory may be removed.
    assert temp_root.parent==temp_base and temp_root.name.startswith('mesh-handoff-portability-')
    shutil.rmtree(temp_root)
for rel,h in original_hashes.items():
    if hashlib.sha256((P/rel).read_bytes()).hexdigest()!=h:errors.append('Audit changed original mockup '+rel)

out=dict(passed=not errors,errors=errors,images_decoded=len(decoded),decoded_assets=decoded,
         locked_copy_strings_checked=len(locked),action_contracts_checked=len(routes['actions']),
         html_runtime_resources_checked=resource_count,relocation=relocation,
         standalone_product_reference_slots=sum(x['standalone_available'] for x in slots),
         slots_without_confirmed_standalone=sum(not x['standalone_available'] for x in slots),
         original_mockup_hashes_unchanged=True)
(P/'verification/deep-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['decoded_assets','relocation']},indent=2))
raise SystemExit(bool(errors))
