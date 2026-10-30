"""Assemble immutable reference copies and handoff data. No image manipulation."""
from pathlib import Path
import csv, hashlib, json, shutil
from PIL import Image

PACKAGE = Path(__file__).resolve().parents[1]
WORKSPACE = PACKAGE.parent
if (PACKAGE / 'data/design-manifest.json').exists():
    raise SystemExit('Frozen handoff already exists. This seed assembler must not overwrite approved data. Use build_viewers.py and validate_package.py for documentation updates.')
records = []

def write_json(rel, value):
    p = PACKAGE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def copy_asset(source, dest, role, status, sections=None):
    source = Path(source)
    if not source.is_absolute():
        source = WORKSPACE / source
    if not source.is_file():
        return False
    target = PACKAGE / dest
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
    width = height = None
    if source.suffix.lower() != '.svg':
        with Image.open(source) as im:
            width, height = im.size
    try:
        origin = source.relative_to(WORKSPACE).as_posix()
    except ValueError:
        origin = str(source)
    records.append(dict(path=dest, source=origin, sha256=digest, bytes=target.stat().st_size,
                        width=width, height=height, role=role, readiness=status,
                        sections=sections or [], transformed=False))
    return True

mockups = [
    ('M01', 'mesh-mobile-shallow-curve-v11.png', 'Ticker, header, hero and four categories', ['S00','S01','S02','S03'], 'Latest corrected hero; final baseline'),
    ('M02', 'mesh-discovery-user-selected.png', 'Learning discovery', ['S04'], 'Exact user-selected attachment'),
    ('M03', 'mesh-shared-play-section-v2.png', 'Shared play', ['S05'], 'Explicit next approve'),
    ('M04', 'mesh-creative-play-v1.png', 'Creative shopping', ['S06'], 'Retained final baseline'),
    ('M05', 'mesh-shoppable-video-v1.png', 'Shoppable video', ['S07'], 'Latest addition before homepage-complete instruction'),
    ('M06', 'mesh-play-growth-palette08-v3.png', 'Growth and connection', ['S08'], 'Latest palette08 revision'),
    ('M07', 'mesh-whatsapp-palette08-v2.png', 'Customer WhatsApp stories', ['S09'], 'Latest layout; real messages missing'),
    ('M08', 'mesh-faq-palette08-v3.png', 'Expanded FAQ', ['S10'], 'Latest ten-question revision'),
]
manifest = []
for ident, name, title, sections, basis in mockups:
    rel = 'assets/mockups/' + name
    assert copy_asset('output/design-concepts/' + name, rel, 'authoritative_mockup', 'reference_only_not_standalone_web_asset', sections)
    manifest.append(dict(id=ident, path=rel, title=title, sections=sections, basis=basis))

refs = [
    ('output/design-concepts/mesh-bright-premium-palettes.png', 'palette08-selection.png', 'Option08 only; other options not selected'),
    ('output/design-concepts/mesh-reference-cards-four-v9.png', 'category-anatomy-v9-reference-only.png', 'Category anatomy only; mobile hero superseded'),
    ('output/design-concepts/mesh-hero-blue-balanced-v7.png', 'shallow-curve-v7-reference-only.png', 'Curve comparison only; header/categories superseded'),
    ('ChatGPT Image Oct 29, 2026, 02_31_54 AM.png', 'user-menu-pill-reference.png', 'User supplied menu icon/pill style'),
    ('C:/Users/iamar/AppData/Local/Temp/codex-clipboard-d449bf73-5317-4a17-b058-59064ef8c311.png', 'user-category-card-detail.png', 'User supplied horizontal card detail'),
    ('C:/Users/iamar/AppData/Local/Temp/codex-clipboard-824e47d5-2324-4552-9326-b16cb662b0dc.png', 'user-palette08-reference.png', 'Latest supplied palette board, option08'),
]
for source, name, role in refs:
    copy_asset(source, 'assets/references/' + name, role, 'supporting_reference_not_alternative_design')

product_uses = {
    'colour-coder.jpg':['S04','S05','S07','S08'],
    'magnetic-board.jpg':['S04'],
    'diy-screw-drill-puzzle-toy.webp':['S04'],
    '3d-maze-cube.webp':['S04'],
    'sticker-book.jpg':['S06','S07','S08'],
    'mosaic-board.jpg':['S06','S07'],
    'magnetic-tiles.jpg':['S08'],
}
for source in sorted((WORKSPACE/'output/design-concepts/catalog-references').iterdir()):
    if source.suffix.lower() in ('.png','.jpg','.jpeg','.webp'):
        used = product_uses.get(source.name, [])
        copy_asset(source, 'assets/product-source/'+source.name,
                   'catalog_reference_used_in_selected_mockup' if used else 'supplemental_catalog_reference_not_selected_art',
                   'verify_rights_resolution_sku_before_production', used)

copy_asset('output/design-concepts/mesh-wordmark.svg', 'assets/legacy-reference/mesh-wordmark.svg',
           'legacy_wordmark_not_verified_selected_master', 'do_not_substitute_without_visual_match', ['S01'])
for source in sorted((WORKSPACE/'output/category-art').glob('*.png')):
    copy_asset(source, 'assets/legacy-reference/'+source.name,
               'older_category_art_not_selected_cutout', 'do_not_substitute_for_M01', ['S03'])

history = PACKAGE/'source-notes'
history.mkdir(exist_ok=True)
for number in [1,3,11,12,13,16,17,18,19,20,21,22,23]:
    for source in sorted((WORKSPACE/'docs').glob(f'{number:02d}-*.md')):
        # Plain-text snapshot avoids suggesting old relative links form an active specification.
        shutil.copy2(source, history/(source.stem+'.txt'))
for source in sorted((WORKSPACE/'output/design-concepts').glob('*prompt*.txt')):
    out = PACKAGE/'source-notes/prompts'/source.name
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, out)
for folder in ['sections','snippets']:
    for source in sorted((WORKSPACE/'theme-work'/folder).glob('*.liquid')):
        out = PACKAGE/'implementation-reference'/folder/source.name
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, out)

section_defs = [
 ('S00','announcement','Announcement','M01','Full width','Full width'),
 ('S01','header','Header','M01','Logo + 3 icon pills + search/cart','Logo + search/cart/menu'),
 ('S02','hero','Hero','M01','Photo with left cream overlay','Copy + shallow curve + photo'),
 ('S03','categories','Four categories','M01','2 columns × 2 rows','4 horizontal stacked cards'),
 ('S04','discovery','Learning discovery','M02','4 product columns','2 columns × 2 rows'),
 ('S05','shared-play','Shared play','M03','Photo 63% / copy 37%','Copy, photo, steps, CTA'),
 ('S06','creative-play','Creative shopping','M04','Panorama + 2 purchase areas','Photo + 2 purchase rows'),
 ('S07','shoppable-video','Video shopping','M05','3 portrait cards','1 card + next glimpse'),
 ('S08','growth','Growth and connection','M06','2 × 2 image/text modules','4 stacked image/text rows'),
 ('S09','customer-stories','WhatsApp stories','M07','3 portrait cards','1 card + next glimpse'),
 ('S10','faq','Expanded FAQ','M08','2 groups / 10 questions','2 stacked groups / 10 questions'),
 ('S11','footer','Inherited footer',None,'Existing native footer','Existing responsive footer'),
]
sections=[dict(id=a,key=b,title=c,mockup=d,desktop=e,mobile=f,order=i) for i,(a,b,c,d,e,f) in enumerate(section_defs)]
write_json('data/design-manifest.json',dict(version='1.0',date='2026-10-30',
    authority='Latest user homepage-complete instruction plus explicit earlier selections/corrections',
    order_status='Documented assembly inference; no full-page composite supplied',
    mockups=manifest,sections=sections,
    rejected=['mesh-mobile-curve-restored-v10.png','mesh-rc-section-v1.png','mesh-rc-feature-add-to-cart-v2.png'],
    superseded_not_to_substitute=['mesh-next-section-discovery-v3.png','mesh-buying-help-v1.png']))

write_json('data/design-tokens.json',dict(
    status='Palette confirmed; metrics/font choices are implementation targets',
    colors=dict(primary='#2354D7',cream='#FFFCF5',tangerine='#FF8547',yellow='#FFE16B',navy='#172B4D',white='#FFFFFF'),
    component_exceptions='Preserve selected pale mint/pastel category/menu/discovery surfaces; no new unrelated UI accents',
    typography=dict(heading_candidate='Outfit',body_candidate='DM Sans',identity_confirmed=False),
    breakpoints_css_px=dict(mobile_max=749,tablet_min=750,tablet_max=989,desktop_min=990),
    container_max_css_px=1440,gutters_css_px=dict(mobile=16,tablet=24,desktop=32),
    touch_target_min_css_px=44,mobile_hero_curve_dip_fraction=dict(target=.062,min=.055,max=.070),
    targets_not_measured=dict(lcp_seconds=2.5,inp_ms=200,cls=.1)))

categories=[
 dict(title='Remote Control',description='Simple joys. Big adventures indoors and out.',destination='collection_remote_control',surface='pale blue'),
 dict(title='Puzzles & Play',description='Hands-on fun for everyday moments.',destination='collection_puzzles',surface='pale peach'),
 dict(title='Gadgets',description='Little surprises to explore and share.',destination='collection_gadgets',surface='pale yellow'),
 dict(title='Educational',description='Build, try and discover together.',destination='collection_educational',surface='pale mint')]
discovery=[
 dict(product='colour_coder',title='Colour Coder',tag='MATCH',description='Slide colours to match a pattern.'),
 dict(product='magnetic_drawing_board',title='Magnetic Drawing Board',tag='DRAW',description='Lift beads with the magnetic pen.'),
 dict(product='diy_drill',title='DIY Screw Drill Puzzle',tag='BUILD',description='Build pictures with shapes and screws.'),
 dict(product='maze_cube',title='3D Maze Cube',tag='SOLVE',description='Guide the ball through the maze.')]
growth=[
 dict(title='Attention & patience',body='Follow a pattern, one move at a time.',label='Pattern play'),
 dict(title='Problem-solving',body='Test a piece. Change the plan. Try again.',label='Building play'),
 dict(title='Creative expression',body='Choose colours. Make a picture their own.',label='Art & making'),
 dict(title='Connection & emotions',body='Take turns, name feelings and celebrate effort.',label='Playing together')]
questions=[
 ('How do I choose the right toy?', 'Start with what they enjoy: puzzles, building, art or imaginative play. Check the toy’s age guidance before choosing.', 'visible_mockup_copy'),
 ('Can play support focus and patience?', 'Matching a pattern or trying a puzzle gives children opportunities to stay with a task and try again. Follow their pace and keep play enjoyable; outcomes vary.', 'draft'),
 ('Which toys work without batteries?', 'Many puzzles, art activities and building sets work without batteries. Check each product’s power requirements and included accessories.', 'draft'),
 ('What comes in the box?', 'Contents vary by product. Check the listing for pieces, accessories and any batteries needed. Ask us if anything is unclear before ordering.', 'draft'),
 ('Can you help me choose a gift?', 'Tell us the child’s age, interests and your budget, and we can help you compare suitable options. Follow the manufacturer’s age guidance.', 'draft'),
 ('When will my order arrive?', None, 'operational_confirmation_required'),
 ('How much does shipping cost?', None, 'operational_confirmation_required'),
 ('Can I pay on delivery?', None, 'operational_confirmation_required'),
 ('What if an item arrives damaged?', None, 'operational_confirmation_required'),
 ('Can I cancel or return an order?', None, 'operational_confirmation_required')]
content=dict(
 announcement=dict(text='Discover toys for every kind of play →',destination='all_products'),
 header=dict(brand='Mesh Toy Shop',menu=['RC Toys','Puzzles','Gadgets']),
 hero=dict(heading='Let curiosity lead.',emphasis='lead.',body='RC adventures, puzzles and hands-on play to discover together.',primary='Explore toys',secondary='Shop RC toys'),
 categories=categories,
 discovery=dict(heading='Little hands. Big discoveries.',body='Match a pattern. Make a shape. Try a new way.',cta='Explore learning toys',item_cta='View toy',products=discovery),
 shared_play=dict(eyebrow='A PLAY IDEA TO SHARE',heading='The joy of figuring it out.',body='A pattern to solve. A little encouragement. A moment to share.',steps=['Pick a pattern','Slide to match','Swap turns'],cta='Explore Colour Coder'),
 creative_play=dict(eyebrow='THE CREATIVE CORNER',heading='Made by little hands.',body='Peel a sticker. Place a bead. Make it their own.',cta='Explore creative play',purchase_cta='Add to cart',products=[dict(key='sticker_book',description='Match numbers to make animal pictures.'),dict(key='mosaic_board',description='Place colourful beads to create a pattern.')]),
 video=dict(heading='Watch them play.',body='See how it works. Find their next favourite.',purchase_cta='Add to cart',mobile_hint='Swipe to explore',products=[dict(key='colour_coder',caption='Slide. Match. Try again.'),dict(key='sticker_book',caption='One sticker at a time.'),dict(key='mosaic_board',caption='Build a colourful pattern.')]),
 growth=dict(heading='Play that gives them room to grow.',body='Ways to practise, create and connect.',cta='Explore ways to play',modules=growth),
 stories=dict(heading='Your playtime stories.',body='A closer look at everyday play.',cta='View toy',real_screenshots_available=False),
 faq=dict(heading='A few things before playtime.',body='Choosing, ordering and getting ready to play.',groups=['Choosing a toy','Orders & support'],questions=[dict(id=f'faq_{i+1:02}',group=0 if i<5 else 1,question=q,answer=a,status=s,initial_open=i==0) for i,(q,a,s) in enumerate(questions)],contact_heading='Still have a question?',contact_body='Send us the product names and what you’re looking for.',contact_cta='Ask Mesh'),
 footer=dict(status='inherit_current_theme_and_read_back',known_heading='Small toys. Shared moments.',known_menu=['Home','Catalog','Contact'],brand_paragraph=None))
write_json('data/content.json',content)

old_products=json.loads((WORKSPACE/'data/meshenterprise/products.json').read_text(encoding='utf-8-sig'))
product_rows=[]
defs=[('colour_coder','Colour Coder','colour-coder.jpg',180,450),('magnetic_drawing_board','Magnetic Drawing Board','magnetic-board.jpg',135,None),('diy_drill','DIY Screw Drill Puzzle','diy-screw-drill-puzzle-toy.webp',None,None),('maze_cube','3D Maze Cube','3d-maze-cube.webp',None,None),('sticker_book','Sticker-by-Number Book','sticker-book.jpg',100,250),('mosaic_board','Mosaic Bead Board','mosaic-board.jpg',250,625),('magnetic_tiles','Magnetic Tiles','magnetic-tiles.jpg',None,None)]
for key,title,filename,quote,reference in defs:
    old=next((p for p in old_products if (key=='maze_cube' and p['title']=='3D Maze Cube') or (key=='diy_drill' and 'drill' in p['title'].lower())),None)
    product_rows.append(dict(key=key,display_title=title,source_image='assets/product-source/'+filename,
         supplier_quote_inr=quote,mockup_reference_price_inr=reference,
         price_rule='2.5x quote for new selections only; retain live price for existing products',
         shopify_product_id=None,shopify_variant_id=None,shopify_handle=None,
         historical_source_sku=old.get('sku') if old else None,
         historical_captured_price_inr=old.get('price_inr') if old else None,
         historical_data_is_live=False,age_verified=False,rights_verified=False))
write_json('data/product-map.json',dict(products=product_rows,collection_bindings={k:None for k in ['collection_remote_control','collection_puzzles','collection_gadgets','collection_educational','collection_creative_play','collection_learning_play']},support_whatsapp=None,source='https://www.meshenterprise.in/learning-and-educational-toy.html'))

slots=[]
def slot(ident,section,kind,available,source,notes):
    slots.append(dict(id=ident,section=section,kind=kind,standalone_available=available,source=source,notes=notes))
slot('hero-desktop-mobile','S02','lifestyle',False,'assets/mockups/mesh-mobile-shallow-curve-v11.png','Selected scene embedded only; clean master/real shoot required, preserve woman/boy/RC composition')
for key in ['remote-control','puzzles','gadgets','educational']:
    slot('category-'+key,'S03','cutout',False,'assets/mockups/mesh-mobile-shallow-curve-v11.png','Exact selected cutout embedded only; legacy art is not a substitute')
for prod in product_rows:
    slot('product-'+prod['key'],'catalog','packshot',True,prod['source_image'],'Catalog original; resolution/rights/SKU require verification')
slot('shared-play-photo','S05','lifestyle',False,'assets/mockups/mesh-shared-play-section-v2.png','Selected mother/daughter scene embedded only')
slot('creative-overhead','S06','lifestyle',False,'assets/mockups/mesh-creative-play-v1.png','Preserve both activities in desktop/mobile art direction')
for key in ['colour-coder','sticker-book','mosaic-board']:
    slot('video-'+key,'S07','video_and_poster',False,'assets/mockups/mesh-shoppable-video-v1.png','Actual clip missing; poster scene embedded only, not proof of use')
for key in ['attention','problem-solving','creative-expression','connection']:
    slot('growth-'+key,'S08','lifestyle',False,'assets/mockups/mesh-play-growth-palette08-v3.png','Selected scene embedded only; exact product geometry/realism not guaranteed')
for n in range(1,4):
    slot('whatsapp-'+str(n),'S09','customer_screenshot',False,'assets/mockups/mesh-whatsapp-palette08-v2.png','No genuine message provided; obtain permission and redact personal data')
slot('wordmark','S01','logo',False,'assets/legacy-reference/mesh-wordmark.svg','Legacy candidate available but exact approved vector master unconfirmed')
write_json('data/asset-slots.json',slots)
for source in sorted((PACKAGE/'assets/verification').glob('*.png')):
    with Image.open(source) as im:
        width,height=im.size
    records.append(dict(path=source.relative_to(PACKAGE).as_posix(),
        source=source.relative_to(WORKSPACE).as_posix(),
        sha256=hashlib.sha256(source.read_bytes()).hexdigest(),bytes=source.stat().st_size,
        width=width,height=height,role='local_browser_verification_evidence',
        readiness='documentation_QA_not_storefront_asset',sections=[],transformed=False))
write_json('data/asset-manifest.json',records)
with (PACKAGE/'data/asset-manifest.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(records[0]))
    writer.writeheader()
    for r in records:
        writer.writerow({**r,'sections':','.join(r['sections'])})

(PACKAGE/'implementation-reference/README.md').write_text('''# Historical partial Dawn source — DO NOT PUSH AS A THEME

These files are unchanged inspection references from the earlier implementation. They do not implement the latest eight-board homepage. Their old layouts and counts do not override this package's docs.

The directory lacks a complete theme checkout. Current Shopify source/settings must be pulled/read and backed up before implementation. The original empty locale lint fixture is deliberately excluded. Never replace live translations or push this folder wholesale.

No code from this snapshot was authored or validated anew by the handoff task; historical checks are not current-build verification.
''',encoding='utf-8')
(PACKAGE/'source-notes/README.md').write_text('''# Historical evidence snapshots

The numbered .txt files preserve previous notes verbatim, including outdated statuses and historical relative links. They are evidence, not active specifications. Use docs/01-design-authority.md and the eight current mockup boards when conflicts arise. Source prompt files record generation history, not permission to regenerate the selected images.
''',encoding='utf-8')
print(json.dumps(dict(images=len(records),authoritative_mockups=len(manifest),asset_slots=len(slots),products=len(product_rows)),indent=2))
