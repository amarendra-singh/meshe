"""Build local, dependency-free HTML viewers. Does not manipulate image files."""
from pathlib import Path
from html import escape
import json,re
import markdown

P=Path(__file__).resolve().parents[1]
manifest=json.loads((P/'data/design-manifest.json').read_text(encoding='utf-8'))
content=json.loads((P/'data/content.json').read_text(encoding='utf-8'))
assets=json.loads((P/'data/asset-manifest.json').read_text(encoding='utf-8'))
css='''*{box-sizing:border-box}body{margin:0;background:#FFFCF5;color:#172B4D;font:16px/1.6 system-ui,sans-serif}a{color:#2354D7}a:focus-visible,button:focus-visible{outline:3px solid #172B4D;outline-offset:4px}header{padding:40px max(24px,calc((100vw - 1200px)/2));background:#172B4D;color:white}header a{color:#FFE16B}h1{font-size:clamp(30px,4vw,48px);line-height:1.1;margin:12px 0}h2{line-height:1.2;margin:36px 0 16px}h3{margin-top:28px}main{max-width:1280px;margin:auto;padding:24px}.lead{max-width:850px}.nav{display:flex;flex-wrap:wrap;gap:12px}.nav a,button{border:1px solid #2354D7;border-radius:8px;padding:10px 16px;background:white;color:#2354D7;font:inherit;cursor:pointer;min-height:44px}.notice{border-left:5px solid #FF8547;background:#fff2e8;padding:16px;margin:20px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}.card{padding:20px;border:1px solid #d6dfec;border-radius:12px;background:white}.board{padding:20px 0;border-bottom:1px solid #d6dfec}.board img{display:block;width:100%;height:auto;border:1px solid #e0e4ea;border-radius:6px}.meta{font-size:14px;color:#53647e}table{border-collapse:collapse;width:100%;font-size:14px}th,td{text-align:left;padding:10px;border:1px solid #d6dfec;vertical-align:top;overflow-wrap:anywhere}th{background:#edf1fc}pre{overflow:auto;background:#f2f4f7;padding:16px}code{font-size:.92em}details{border:1px solid #d6dfec;background:white;border-radius:8px;margin:14px 0;padding:16px}summary{cursor:pointer;font-weight:700;min-height:32px}article{scroll-margin-top:20px;overflow-wrap:anywhere}.toc{columns:2;column-gap:32px}.swatches{display:flex;gap:12px;flex-wrap:wrap}.swatch{padding:18px;min-width:150px;border-radius:10px;border:1px solid #ddd}.asset-thumb{height:170px;max-width:100%;object-fit:contain}.table-wrap{overflow:auto}.badge{display:inline-block;padding:4px 9px;border-radius:6px;background:#edf1fc;font-size:13px}.divider{border-top:2px solid #d6dfec;margin:50px 0}@media(max-width:600px){main{padding:16px}.toc{columns:1}header{padding:24px 16px}th,td{padding:7px}.card{padding:14px}}@media print{header{background:white;color:#172B4D}.nav{display:none}details{break-inside:avoid}summary{display:none}details>div{display:block}.board{break-before:page}a{color:inherit}}'''

css+='header .badge{color:#172B4D}'

def shell(title,body,depth=0):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title><style>'+css+'</style></head><body>'+body+'</body></html>'

docs=sorted((P/'docs').glob('*.md'))
docnav=''.join(f'<li><a href="TECHNICAL-HANDBOOK.html#{d.stem}">{escape(d.stem.replace("-"," "))}</a></li>' for d in docs)
boards=''
for m in manifest['mockups']:
    boards+=f'<section class="board" id="{m["id"]}"><h2>{m["id"]} · {escape(m["title"])}</h2><p class="meta">{escape(m["basis"])} · {escape(", ".join(m["sections"]))} · Original file, unchanged</p><a href="{m["path"]}"><img src="{m["path"]}" alt="{escape(m["title"])} original desktop and mobile mockup" loading="lazy"></a></section>'
swatches=''.join(f'<div class="swatch" style="background:{color};color:{ink}">{label}<br><strong>{color}</strong></div>' for label,color,ink in [('Primary','#2354D7','white'),('Cream','#FFFCF5','#172B4D'),('Tangerine','#FF8547','#172B4D'),('Yellow','#FFE16B','#172B4D'),('Navy','#172B4D','white')])
start=f'''<header><div class="badge">HANDOFF · 30 OCTOBER 2026</div><h1>Mesh Toy Shop<br>Shopify implementation package</h1><p class="lead">Eight frozen reference boards. Complete responsive build instructions. Available source assets, provenance and explicit production gaps.</p><nav class="nav"><a href="TECHNICAL-HANDBOOK.html">Technical handbook</a><a href="wireframes/index.html">Responsive wireframes</a><a href="ASSET-LIBRARY.html">Asset library</a><a href="README.md">Readme</a><a href="verification/REPORT.md">Verification report</a></nav></header><main><div class="notice"><strong>Preserve the mockups.</strong> The images below are byte-identical copies. This is a documentation package, not a live Shopify theme. Actual videos and customer messages are still missing; generated family scenes are concepts.</div><h2>Selected palette 08</h2><div class="swatches">{swatches}</div><h2>Read the specification</h2><ol class="toc">{docnav}</ol><h2>Authoritative reference gallery</h2><p>Click any image to inspect the original at full resolution. Desktop/mobile labels and device frames are presentation elements, not storefront components.</p>{boards}<h2>Footer</h2><p>No new footer board was supplied. Preserve and read back the existing native footer; see S11 in the handbook.</p></main>'''
start=start.replace('<a href="README.md">Readme</a>','<a href="README.md">Readme</a><a href="FINAL-MOCKUPS.html">Final mockups</a><a href="HANDOFF-STATUS.md">Handoff readiness</a>')
(P/'START-HERE.html').write_text(shell('Mesh Toy Shop — Start here',start),encoding='utf-8')

final_gallery='<header><h1>Final homepage mockups</h1><p>All eight retained desktop/mobile section boards, unchanged. Click an image to inspect the original file.</p><nav class="nav"><a href="TECHNICAL-HANDBOOK.html">Full technical details</a><a href="wireframes/index.html">Responsive wireframes</a><a href="ASSET-LIBRARY.html">Assets</a><a href="HANDOFF-STATUS.md">Handoff readiness</a><a href="START-HERE.html">Overview</a></nav></header><main>'+boards+'</main>'
(P/'FINAL-MOCKUPS.html').write_text(shell('Mesh Toy Shop — Final mockup gallery',final_gallery),encoding='utf-8')

def convert_links(text):
    # Markdown lives in docs/; handbook lives at package root.
    text=re.sub(r'(href|src)="\.\./([^"#]+)(#[^"]*)?"',lambda m:f'{m[1]}="{m[2]}{m[3] or ""}"',text)
    for d in docs:
        text=text.replace(f'href="{d.name}"',f'href="#{d.stem}"')
    return text
chapters=''
for d in docs:
    html=convert_links(markdown.markdown(d.read_text(encoding='utf-8'),extensions=['tables','fenced_code','sane_lists']))
    html=html.replace('<table>','<div class="table-wrap"><table>').replace('</table>','</table></div>')
    chapters+=f'<article id="{d.stem}">{html}</article><div class="divider"></div>'
handbook=f'<header><h1>Technical handbook</h1><p>Detailed contract for the next implementing AI. Original boards control visual fidelity; explicit engineering targets fill missing CSS/state detail.</p><nav class="nav"><a href="START-HERE.html">Reference gallery</a><a href="wireframes/index.html">Wireframes</a><a href="ASSET-LIBRARY.html">Assets</a></nav></header><main><ol class="toc">{docnav.replace("TECHNICAL-HANDBOOK.html","")}</ol>{chapters}</main>'
(P/'TECHNICAL-HANDBOOK.html').write_text(shell('Mesh Toy Shop — Technical handbook',handbook),encoding='utf-8')

cards=''
for a in assets:
    cards+=f'<div class="card"><a href="{a["path"]}"><img class="asset-thumb" src="{a["path"]}" alt="{escape(Path(a["path"]).name)}" loading="lazy"></a><h3>{escape(Path(a["path"]).name)}</h3><p class="meta">{escape(a["role"])}<br>{a["width"] or "vector"} × {a["height"] or "vector"} · {a["bytes"]:,} bytes</p><p>{escape(a["readiness"].replace("_"," "))}</p><details><summary>Provenance and checksum</summary><p class="meta">Source: {escape(a["source"])}<br>SHA-256: {a["sha256"]}</p></details></div>'
assetpage=f'<header><h1>Asset library</h1><p>{len(assets)} unchanged image/reference files. Read the role before using an asset.</p><nav class="nav"><a href="START-HERE.html">Start here</a><a href="data/asset-manifest.csv">CSV inventory</a><a href="data/asset-slots.json">Asset gaps / slots</a></nav></header><main><div class="notice">Catalog images are not necessarily the exact generated render in the mockup. Legacy artwork must not replace selected imagery. Embedded-only scenes and missing real videos/messages are recorded in the asset-slot register.</div><div class="grid">{cards}</div></main>'
(P/'ASSET-LIBRARY.html').write_text(shell('Mesh Toy Shop — Asset library',assetpage),encoding='utf-8')

wirecss='''body{background:#f1f3f6}.toolbar{position:sticky;top:0;z-index:3;padding:12px 20px;background:white;border-bottom:1px solid #bcc5d3;display:flex;gap:8px;align-items:center;flex-wrap:wrap}.toolbar button[aria-pressed=true]{background:#2354D7;color:white}.stage{overflow-x:auto;padding:24px}.canvas{width:1280px;margin:auto;background:white;border:1px solid #9faabc;padding:20px;container-type:inline-size;transition:none}.wf{border:1px solid #8290a8;padding:16px;margin:16px 0;background:#fff}.wf h2{font-size:20px;margin:0 0 12px}.wf p{margin:8px 0;font-size:14px}.section-label{font:12px/1.4 monospace;letter-spacing:.04em;color:#52617b}.box{border:1px dashed #75829a;background:#f2f4f7;padding:16px;min-height:50px;display:grid;place-content:center;text-align:center;font-size:14px;overflow-wrap:anywhere}.bar{border:1px solid #8290a8;padding:12px;text-align:center;background:#e9edf4}.row{display:flex;gap:16px;align-items:center}.logo{font-weight:800}.header-fill{flex:1}.desktop-nav{display:flex;gap:12px}.mobile-nav{display:none}.hero-area{position:relative;min-height:320px;background:#e0e4eb;padding:28px;display:flex;align-items:center}.hero-copy{width:46%;padding:24px;border:1px solid #75829a;background:white;z-index:1}.hero-photo{position:absolute;right:20px;top:30px;width:46%;height:260px}.hero-copy h3{font-size:32px;line-height:1.05;margin:0 0 10px}.actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:14px}.action{border:1px solid #52617b;background:#e1e6ef;border-radius:24px;padding:10px 16px;text-align:center;font-size:14px}.categories{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.category{border:1px solid #8290a8;border-radius:12px;padding:16px;display:grid;grid-template-columns:1fr 1fr;gap:16px}.category .box{min-height:110px}.products{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}.product{border:1px solid #8290a8;border-radius:12px;padding:12px;display:flex;flex-direction:column;gap:10px}.product .box{aspect-ratio:.78;min-height:0}.product .action{margin-top:auto}.shared{display:grid;grid-template-columns:63fr 37fr;gap:24px}.shared-photo{grid-column:1;grid-row:1/4;min-height:420px}.shared-head{grid-column:2}.shared-steps{grid-column:2}.shared-cta{grid-column:2}.panorama{aspect-ratio:2.32;min-height:0}.purchase-row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:18px}.purchase{display:grid;grid-template-columns:30fr 70fr;gap:12px;border-bottom:1px solid #bac3d0;padding:12px}.rail{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory}.rail-card{flex:0 0 calc((100% - 32px)/3);border:1px solid #8290a8;padding:10px;scroll-snap-align:start}.video-frame{aspect-ratio:.63}.story-frame{aspect-ratio:.8}.growth-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}.growth-item{display:grid;grid-template-columns:1fr 1fr;gap:16px;border-bottom:1px solid #bac3d0;padding:12px}.growth-item .box{aspect-ratio:1}.faq-groups{display:grid;grid-template-columns:1fr 1fr;gap:20px}.faq-group{border:1px solid #8290a8;padding:14px}.faq-question{border-bottom:1px solid #bcc5d3;padding:12px 0;font-size:14px}.faq-answer{background:#edf0f5;padding:10px;font-size:13px}.contact{margin-top:18px}.legend{font-size:13px;color:#52617b}.note{background:#fff6d8;border-left:3px solid #b08827;padding:12px;margin:10px 0;font-size:13px}@container(max-width:989px){.desktop-nav{display:none}.mobile-nav{display:block}.hero-area{display:block;padding:0;background:#e0e4eb}.hero-copy{width:100%;position:relative;padding:24px;margin-bottom:6.2cqw;border:0}.hero-copy:after{content:'';position:absolute;left:0;right:0;bottom:-6.2cqw;height:12.4cqw;background:white;border-radius:0 0 50% 50%;z-index:-1}.hero-copy{isolation:isolate}.hero-photo{position:static;width:100%;height:240px}.products{grid-template-columns:repeat(2,minmax(0,1fr))}.shared{display:flex;flex-direction:column}.shared-photo{order:2;min-height:0;aspect-ratio:1.13}.shared-head{order:1}.shared-steps{order:3}.shared-cta{order:4}.growth-grid{grid-template-columns:1fr}.faq-groups{grid-template-columns:1fr}.rail-card{flex-basis:calc((100% - 16px)/2)}}@container(max-width:749px){.canvas{padding:12px}.categories{grid-template-columns:1fr}.category{gap:10px;padding:12px}.category .box{min-height:90px}.hero-copy h3{font-size:30px}.hero-copy .actions{display:block}.hero-copy .action{margin:10px 0}.products{gap:12px}.product{padding:8px;font-size:13px}.product .box{aspect-ratio:.92;padding:8px}.product .action{padding:10px 6px}.purchase-row{grid-template-columns:1fr}.panorama{aspect-ratio:1.21}.rail-card{flex-basis:86%}.growth-item{grid-template-columns:42fr 58fr;gap:10px;padding:8px}.wf{padding:12px}.wf h2{font-size:20px}.row{gap:8px}.logo{font-size:16px}.header-fill{display:none}.mobile-nav{margin-left:auto;font-size:13px}.story-frame{aspect-ratio:.8}}'''

def box(t,cls=''):
    return f'<div class="box {cls}">{t}</div>'
def sec(ident,title,body):
    return f'<section class="wf" id="wf-{ident}"><div class="section-label">{ident} · STRUCTURAL WIREFRAME</div><h2>{title}</h2>{body}</section>'
parts=[]
parts.append(sec('S00','Announcement','<div class="bar">Discover toys for every kind of play →</div>'))
parts.append(sec('S01','Header','<div class="row"><span class="logo">Mesh Toy Shop</span><span class="header-fill"></span><div class="desktop-nav"><span class="action">RC Toys</span><span class="action">Puzzles</span><span class="action">Gadgets</span><span class="action">Search / Cart</span></div><div class="mobile-nav">Search · Cart · Menu</div></div>'))
parts.append(sec('S02','Hero','<div class="hero-area"><div class="hero-copy"><h3>Let curiosity<br>lead.</h3><p>RC adventures, puzzles and hands-on play to discover together.</p><div class="actions"><span class="action">Explore toys</span><span class="action">Shop RC toys</span></div></div>'+box('Mother + child + RC photo<br>Maintain safe subject zones','hero-photo')+'</div><p class="legend">Mobile: continuous cream edge; central dip≈6.2% of hero width. This diagram is not a new mockup.</p>'))
parts.append(sec('S03','Four horizontal category cards','<div class="categories">'+''.join('<div class="category"><div><strong>'+escape(x['title'])+'</strong><p>'+escape(x['description'])+'</p><span>→</span></div>'+box('Large right-side product<br>shadow + orange marks')+'</div>' for x in content['categories'])+'</div>'))
parts.append(sec('S04','Little hands. Big discoveries.','<p>Match a pattern. Make a shape. Try a new way.</p><div class="products">'+''.join('<div class="product">'+box('Contained product image')+'<span>'+x['tag']+'</span><strong>'+escape(x['title'])+'</strong><p>'+escape(x['description'])+'</p><span class="action">View toy →</span></div>' for x in content['discovery']['products'])+'</div><p>Explore learning toys →</p>'))
parts.append(sec('S05','Shared play','<div class="shared">'+box('Mother + daughter + Colour Coder<br>Desktop photo≈63% of inner width','shared-photo')+'<div class="shared-head"><p>A PLAY IDEA TO SHARE</p><h3>The joy of figuring it out.</h3><p>A pattern to solve. A little encouragement. A moment to share.</p></div><ol class="shared-steps"><li>Pick a pattern</li><li>Slide to match</li><li>Swap turns</li></ol><div class="shared-cta action">Explore Colour Coder →</div></div>'))
parts.append(sec('S06','Made by little hands.','<p>Peel a sticker. Place a bead. Make it their own.</p>'+box('One shared overhead photo<br>Sticker book LEFT / tiger bead board RIGHT','panorama')+'<div class="purchase-row">'+''.join('<div class="purchase">'+box('Toy thumbnail')+'<div><strong>'+title+'</strong><p>'+price+'</p><div class="action">Add to cart</div></div></div>' for title,price in [('Sticker-by-Number Book','₹250'),('Mosaic Bead Board','₹625')])+'</div><p>Explore creative play →</p>'))
parts.append(sec('S07','Watch them play.','<p>See how it works. Find their next favourite.</p><div class="rail">'+''.join('<div class="rail-card">'+box('▶<br>Real video / poster required<br>'+caption,'video-frame')+'<strong>'+name+'</strong><p>'+price+'</p><div class="action">Add to cart</div></div>' for name,caption,price in [('Colour Coder','Slide. Match. Try again.','₹450'),('Sticker-by-Number Book','One sticker at a time.','₹250'),('Mosaic Bead Board','Build a colourful pattern.','₹625')])+'</div><p>Previous / Next · Mobile: swipe + progress</p>'))
parts.append(sec('S08','Play that gives them room to grow.','<p>Ways to practise, create and connect.</p><div class="growth-grid">'+''.join('<div class="growth-item">'+box('Activity photo')+'<div><strong>'+escape(x['title'])+'</strong><p>'+escape(x['body'])+'</p><span class="badge">'+escape(x['label'])+'</span></div></div>' for x in content['growth']['modules'])+'</div><div class="action">Explore ways to play →</div>'))
parts.append(sec('S09','Your playtime stories.','<p>A closer look at everyday play.</p><div class="rail">'+''.join('<div class="rail-card">'+box('Genuine screenshot needed<br>NO fabricated message','story-frame')+'<p>Matching toy thumbnail + name</p><p>View toy →</p></div>' for _ in range(3))+'</div><p>Previous / Next; full-size readable screenshot</p>'))
fg=''
for gi,group in enumerate(content['faq']['groups']):
    fg+='<div class="faq-group"><h3>'+group+'</h3>'
    for q in content['faq']['questions']:
        if q['group']==gi:
            fg+='<div class="faq-question">'+escape(q['question'])+(' −' if q['initial_open'] else ' +')+'</div>'
            if q['initial_open']:
                fg+='<div class="faq-answer">'+escape(q['answer'])+'</div>'
    fg+='</div>'
parts.append(sec('S10','A few things before playtime.','<p>Choosing, ordering and getting ready to play.</p><div class="faq-groups">'+fg+'</div><div class="bar contact">Still have a question? · Ask Mesh →</div>'))
parts.append(sec('S11','Existing footer','<div class="note">Inherited, no new approved footer board. Read current theme settings rather than inventing copy.</div><p>Small toys. Shared moments. · Explore Mesh: Home / Catalog / Contact · Existing signup + privacy link</p>'))
wirecss+='''.canvas{padding:0}.wf{margin:16px}.growth-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.growth-item{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.growth-item>*{min-width:0}.growth-item .badge{max-width:100%;overflow-wrap:anywhere}.row>*{min-width:0}@container(max-width:989px){.growth-grid{grid-template-columns:minmax(0,1fr)}}@container(max-width:749px){.wf{margin:12px}.growth-item{grid-template-columns:minmax(0,42fr) minmax(0,58fr)}.mobile-nav{font-size:12px}.logo{font-size:15px}.box{overflow-wrap:anywhere}.hero-copy .action{display:block}.hero-copy .action:last-child{border:0;background:transparent;text-decoration:underline;padding:4px}}'''
wire='''<header><h1>Responsive structural wireframes</h1><p>Layout diagram only. Original images remain unchanged in the reference gallery. Width buttons change the diagram container, not the browser viewport.</p><nav class="nav"><a href="../START-HERE.html">Original mockups</a><a href="../TECHNICAL-HANDBOOK.html">Technical handbook</a></nav></header><div class="toolbar" aria-label="Wireframe width"><strong>Preview width:</strong><button data-width="1280" aria-pressed="true">Desktop 1280</button><button data-width="768" aria-pressed="false">Tablet 768</button><button data-width="390" aria-pressed="false">Mobile 390</button><button data-width="320" aria-pressed="false">Small mobile 320</button><span id="width-label" aria-live="polite">1280 CSS px</span></div><div class="stage"><div class="canvas" id="canvas">'''+''.join(parts)+'''</div></div><script>for(const b of document.querySelectorAll('[data-width]')){b.addEventListener('click',()=>{const w=Number(b.dataset.width);document.querySelector('#canvas').style.width=w+'px';document.querySelector('#width-label').textContent=w+' CSS px';for(const x of document.querySelectorAll('[data-width]'))x.setAttribute('aria-pressed',String(x===b));});}</script>'''
wirecss=wirecss.replace('@container(', '@container layout (')
wirecss+='''.canvas{border:0;outline:1px solid #9faabc;container-name:layout}.hero-area{container-type:inline-size}'''
(P/'wireframes').mkdir(exist_ok=True)
(P/'wireframes/index.html').write_text(shell('Mesh Toy Shop — Responsive wireframes',wire).replace('</style>','\n'+wirecss+'</style>',1),encoding='utf-8')
ascii_text='''# Wireframe reading order

These diagrams are structural only. The eight original mockups control visual fidelity.

DESKTOP
Ticker
Logo | pastel menu pills | Search Cart
Hero photo [left cream copy overlay]
Category 1 | Category 2
Category 3 | Category 4
Discovery 1 | 2 | 3 | 4
Shared photo 63% | text, steps, CTA37%
Creative overhead panorama
Purchase 1 | Purchase 2
Video 1 | Video 2 | Video 3
Growth 1 | Growth 2
Growth 3 | Growth 4
Customer story 1 | 2 | 3
FAQ choosing5 | FAQ orders5
Existing footer

MOBILE
Ticker
Logo | Search Cart Menu
Hero copy / actions
Shallow convex edge (approximately6%width)
Hero photo
Category1,2,3,4 (horizontal cards stacked)
Discovery1 | 2
Discovery3 | 4
Shared copy → photo → steps → CTA
Creative photo → purchase1 → purchase2
Video1 + next-card glimpse
Growth1,2,3,4 (each photo left/text right)
Customer story1 + next-card glimpse
FAQ choosing5 → orders5
Existing footer

TABLET
Use the documented interpolation in docs02/03. Header collapses; hero stacks; categories/discovery retain2columns if readable; shared play stacks; videos/stories show2cards; growth/FAQ groups stack. No separate approved tablet mockup exists.
'''
(P/'wireframes/README.md').write_text(ascii_text,encoding='utf-8')
print('Created START-HERE.html, TECHNICAL-HANDBOOK.html, ASSET-LIBRARY.html and responsive wireframes.')
