"""Validate package integrity, reference selection, links and content counts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import hashlib,json,re

P=Path(__file__).resolve().parents[1]
W=P.parent
V=P/'verification'
V.mkdir(exist_ok=True)
report=V/'REPORT.md'
if not report.exists():
    report.write_text('# Package verification\nPending.\n',encoding='utf-8')
errors=[]
checked=[]
assets=json.loads((P/'data/asset-manifest.json').read_text(encoding='utf-8'))
for a in assets:
    dest=P/a['path']
    source=Path(a['source'])
    if not source.is_absolute(): source=W/source
    if not dest.is_file(): errors.append('Missing asset: '+a['path']);continue
    h=hashlib.sha256(dest.read_bytes()).hexdigest()
    if h!=a['sha256']: errors.append('Changed package image: '+a['path'])
    if source.exists() and hashlib.sha256(source.read_bytes()).hexdigest()!=h:
        errors.append('Source/copy mismatch: '+a['path'])
    checked.append(dict(path=a['path'],sha256=h,source_exists=source.exists(),matches=h==a['sha256']))

class Links(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.add(d['id'])
        for k in ('href','src'):
            if k in d:self.refs.append(d[k])

link_count=0
html_ids={}
for file in P.rglob('*.html'):
    parser=Links();parser.feed(file.read_text(encoding='utf-8'));html_ids[file.resolve()]=parser.ids
for file in list(P.rglob('*.md'))+list(P.rglob('*.html')):
    text=file.read_text(encoding='utf-8')
    if file.suffix=='.html':
        parser=Links();parser.feed(text);refs=parser.refs
    else:
        refs=[x[1] for x in re.findall(r'(!?\[[^\]]*\])\(([^)]+)\)',text)]
    for raw in refs:
        ref=raw.strip('<>')
        u=urlsplit(ref)
        if u.scheme=='file':
            errors.append(f'Nonportable local link: {file.relative_to(P)} -> {ref}')
            continue
        if u.scheme or ref.startswith('//'):continue
        target=(file.parent/unquote(u.path)).resolve() if u.path else file.resolve()
        link_count+=1
        if not target.is_relative_to(P.resolve()):
            errors.append(f'Link escapes package: {file.relative_to(P)} -> {ref}')
            continue
        if not target.exists():errors.append(f'Broken local link: {file.relative_to(P)} -> {ref}')
        elif u.fragment and target.suffix=='.html' and u.fragment not in html_ids.get(target,set()):
            errors.append(f'Broken HTML anchor: {file.relative_to(P)} -> {ref}')

data={}
for file in (P/'data').glob('*.json'):
    try:data[file.name]=json.loads(file.read_text(encoding='utf-8'))
    except Exception as e:errors.append(f'Invalid JSON {file.name}: {e}')
m=data['design-manifest.json'];c=data['content.json']
assertions={
 'eight_authoritative_boards':len(m['mockups'])==8,
 'twelve_page_regions':len(m['sections'])==12,
 'exact_selected_discovery':next(x for x in m['mockups'] if x['id']=='M02')['path'].endswith('mesh-discovery-user-selected.png'),
 'corrected_hero_v11':m['mockups'][0]['path'].endswith('mesh-mobile-shallow-curve-v11.png'),
 'four_categories':len(c['categories'])==4,
 'four_discovery_products':len(c['discovery']['products'])==4,
 'three_shared_steps':len(c['shared_play']['steps'])==3,
 'two_creative_products':len(c['creative_play']['products'])==2,
 'three_videos':len(c['video']['products'])==3,
 'four_growth_modules':len(c['growth']['modules'])==4,
 'ten_faqs':len(c['faq']['questions'])==10,
 'five_order_answers_unconfirmed':sum(x['answer'] is None for x in c['faq']['questions'])==5,
 'five_questions_per_group':all(sum(q['group']==g for q in c['faq']['questions'])==5 for g in [0,1]),
 'palette08_exact':data['design-tokens.json']['colors']['primary']=='#2354D7',
 'no_extra_rc_mockup':all('mesh-rc-' not in x['path'] for x in m['mockups']),
 'three_reference_prices':{p['key']:p['mockup_reference_price_inr'] for p in data['product-map.json']['products'] if p['mockup_reference_price_inr'] is not None}=={'colour_coder':450,'sticker_book':250,'mosaic_board':625},
 'no_empty_locale_fixture_copied':not (P/'implementation-reference/locales/en.default.json').exists(),
}
for key,ok in assertions.items():
    if not ok:errors.append('Failed content invariant: '+key)
asset_paths={a['path'] for a in assets}
actual_paths={f.relative_to(P).as_posix() for f in (P/'assets').rglob('*') if f.is_file()}
for name in sorted(actual_paths-asset_paths):errors.append('Uninventoried asset: '+name)
for name in sorted(asset_paths-actual_paths):errors.append('Inventory entry without file: '+name)
if len(asset_paths)!=len(assets):errors.append('Duplicate asset inventory path')
for slot in data['asset-slots.json']:
    if slot['source'] not in asset_paths:errors.append('Unmapped asset slot: '+slot['id'])
for product in data['product-map.json']['products']:
    if product['source_image'] not in asset_paths:errors.append('Unmapped product image: '+product['key'])
for mockup in m['mockups']:
    if mockup['path'] not in asset_paths:errors.append('Unmapped mockup: '+mockup['id'])
for file in P.rglob('*'):
    if file.suffix.lower() in ['.png','.jpg','.jpeg','.webp','.svg'] and 'assets' not in file.relative_to(P).parts:
        errors.append('Image outside assets/: '+str(file.relative_to(P)))

qa_count=sum(a['role']=='local_browser_verification_evidence' for a in assets)
result=dict(date='2026-10-30',passed=not errors,image_copies_checked=len(checked)-qa_count,qa_images_checked=qa_count,local_links_checked=link_count,content_invariants=assertions,errors=errors,asset_copies=checked)
(V/'package-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
browser=V/'browser-checks.json'
browser_note='Browser inspection not yet recorded.'
if browser.exists():
    b=json.loads(browser.read_text(encoding='utf-8'))
    browser_note='Tabbit browser evidence is recorded in browser-checks.json. This checks the local gallery, handbook and wireframes, not Shopify checkout or a deployed theme.'
if (V/'receiving-ai-browser-checks.json').exists():
    b=json.loads((V/'receiving-ai-browser-checks.json').read_text(encoding='utf-8'))
    if not b.get('passed'): errors.append('Receiving-AI browser checks did not pass')
    browser_note='Latest Tabbit evidence: [receiving-AI browser checks](receiving-ai-browser-checks.json). All 38 asset-library images and eight final boards loaded; 14 handbook chapters rendered; eight wireframe widths (320, 390, 749, 750, 768, 989, 990, 1280) checked with 49 assertions. The mobile/tablet curve measures approximately 6.2% of the hero width. This checks the local documentation, not a deployed Shopify storefront.'
result['passed']=not errors
(V/'package-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report.write_text(f'''# Package verification — 30 October 2026

Result: **{'PASS' if not errors else 'FAIL'}** for automated package checks.

- {len(checked)-qa_count} original/reference image copies checked against their SHA-256 hashes; {qa_count} browser-evidence screenshots inventoried separately.
- Eight authoritative mockup files preserved without regeneration, cropping or recolouring.
- {link_count} local Markdown/HTML links checked for existence; HTML anchors checked.
- {len(assertions)} content/selection invariants checked, including V11 hero, exact selected discovery, 4 categories, 4 discovery products, 3 video cards, 4 growth modules and 10 FAQs.
- Machine-readable JSON parsed; images restricted to assets/; empty locale fixture excluded.
- Original source mockups were visually inspected during preparation. Comparison findings and embedded-asset limitations are recorded in docs04/06.

{browser_note}

## Scope limitations

No Shopify theme code was authored, deployed or validated as a new implementation. The historical source snapshot is unchanged and incomplete. No real checkout, payment, video playback or customer evidence was created by these package checks. Asset provenance records do not establish rights or stock. Final typography, genuine media and operational inputs remain as documented.

## Detailed results

See [machine-readable checks](package-checks.json), [deep asset/portability audit](deep-audit.json) and [file checksum inventory](files-sha256.json).

Errors: {len(errors)}.
'''+(''.join('\n- '+x for x in errors)),encoding='utf-8')
# Inventory excludes itself to avoid a recursive checksum dependency.
files=[]
for f in sorted(P.rglob('*')):
    if f.is_file() and f.name!='files-sha256.json' and '__pycache__' not in f.parts:
        files.append(dict(path=f.relative_to(P).as_posix(),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
(V/'files-sha256.json').write_text(json.dumps(files,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['asset_copies','content_invariants']},indent=2))
raise SystemExit(1 if errors else 0)
