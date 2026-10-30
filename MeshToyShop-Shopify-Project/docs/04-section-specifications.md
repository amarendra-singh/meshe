# 04 — Section-by-section build contract

For each section, the named board controls visual identity. Dimensions below are approximate measurements from 1536×1024 boards or explicit implementation targets, not source CSS. Exclude presentation labels/gutters when comparing.

## S00 — Announcement

M01. Solid cobalt strip across viewport, centred white 'Discover toys for every kind of play →'. Target 36–44 px desktop and 32–40 px mobile, natural wrapping at extreme text zoom. Single link to all products; no moving marquee needed. The user explicitly required keeping the ticker. No unconfirmed discount, shipping threshold or countdown. It precedes header in DOM and visual order.

## S01 — Header

M01. Desktop left wordmark Mesh Toy Shop with orange burst; three centred pastel pills: orange car icon/RC Toys, green puzzle icon/Puzzles, yellow bulb/Gadgets. Search and cart at right. Cream/white background, clear horizontal alignment, restrained icon stroke. Mobile logo left, search/cart/hamburger right; desktop pill navigation is in drawer. Header is not a graphic baked into the hero.

Target desktop 70–88 px, mobile 60–72 px excluding ticker; allow content-driven growth. Logo width≈250–300 px desktop and 190–220 px mobile subject to 375 px fit. Icons 24 px within 44 px hit zones. At 320 px narrow the logo appropriately; do not overlap controls. M01 itself shows a smaller mobile logo proportion than desktop. Use native accessible search/cart/menu behaviours and visible cart count when nonzero. Sticky behaviour is not specified by the mockup; preserve current theme setting unless a measured usability issue requires a documented change.

## S02 — Hero

M01. Desktop: rounded wide family photograph, generated mother and boy with blue RC toy; cream copy card over the left portion. Approximate board image bounds x 8–1096, y 118–605; width 1088, height 487, ratio 2.23:1. Overlay x 36–524, y 195–556; about 45% of image width. This is a reference composition, not a fixed height for every viewport.

Copy: small orange dash; H1 'Let curiosity lead.' with 'lead.' cobalt; subtext 'RC adventures, puzzles and hands-on play to discover together.' Solid Explore toys pill and underlined Shop RC toys with balanced spacing. No extra eyebrow or development paragraph.

Mobile: full-width cream copy first, primary action wide, secondary link beneath, then photo immediately joined via shallow convex lower edge. Keep≈6% dip; see docs 03. No white gap, detached rounded card or deep bowl. Photo is shorter than a full-screen portrait; parent/child/vehicle remain legible. Image asset is currently embedded in board; production requires a clean approved export or real shoot preserving composition. Do not substitute old father/child or wooden-block campaign image.

## S03 — Four category cards

M01 authority; supporting V9 category-anatomy reference in assets/references. Exactly Remote Control, Puzzles & Play, Gadgets, Educational in that order. Desktop 2×2; mobile 4 stacked. Board desktop cards approximately 519×168/180 px; ratio≈3.0:1. Mobile≈383×110 px; ratio≈3.5:1. Content-driven sizing at real CSS scale; horizontal grammar must survive.

Left zone≈45–50%: navy heading, supporting 2 lines, plain navy right arrow at lower left. Right zone≈45–52%: large product cutout with soft contact shadow and small orange sparks. Preserve breathing room and product scale. Entire card can be one semantic link; do not nest a second arrow link.

Backgrounds: RC pale blue, puzzles peach, gadgets pale yellow, educational pale mint. RC blue/black car; puzzle wooden blocks; gadget camera; education construction/drill. Current standalone older category artwork has a different orange truck/robot/stacker and must not be substituted. Standalone exact selected cutouts are missing; board holds the identity/composition reference.

Copy is in docs 05. No prices, cart controls, circular arrow buttons, centred labels or category icons inside these cards.

## S04 — Learning discovery

M02, exact user attachment. Header 'Little hands. Big discoveries.' with blue second phrase; subline and desktop right-aligned Explore learning toys link. On mobile the section link is a full-width outlined action below the grid.

Four vertical cards: Colour Coder, Magnetic Drawing Board, DIY Screw Drill Puzzle,3D Maze Cube. Large contained photo on peach/yellow/mint/ice-blue surface, activity chip MATCH/DRAW/BUILD/SOLVE, navy title, short body and outlined View toy. White rounded card body with aligned lower actions. Board desktop photo frames about 255×325 px (0.78 width/height); do not force square merely because an old prompt said square. Mobile photo frames≈192×209 px, with narrower type and natural title wrapping.

Desktop 4 equal columns; mobile 2×2 with 12 px gap. Preserve all four items and their order. Source mobile titles differ in wrapping; implementation may align actions using grid/flex without deleting copy. Image contain ensures full products visible. No automatic newest-first selection that fills this learning shelf with RC products. Selected board contains no prices and no Add to cart; preserve its editorial View toy purpose. Commerce controls belong in S06/S07 and PDP.

## S05 — Shared play

M03. Cream section; desktop large rounded photo left≈63% inner width (board 660×735 px), text right≈37%. Image: woman and girl using Colour Coder. Small orange strokes, spaced uppercase eyebrow, headline 'The joy of figuring it out.' with second phrase blue; subtext then three numbered peach circles and steps; solid CTA.

Mobile: eyebrow/headline/subtext first, photo≈384×340 px, steps below, full-width CTA. Do not retain desktop photo-first DOM reading order through a visually reordered but confusing keyboard sequence; organise semantic content carefully. No duplicate headings announced. Keep number badges decorative when the steps are an ordered list. Do not add another hero wave or product-card grid.

Steps: Pick a pattern → Slide to match → Swap turns. These are a suggested caregiver activity, not certified game rules. CTA Explore Colour Coder → selected product. Exact generated image includes product cover deck; genuine demonstration asset should show accurate parts and use.

## S06 — Creative play shopping

M04. Eyebrow THE CREATIVE CORNER. Headline 'Made by little hands.' Subline 'Peel a sticker. Place a bead. Make it their own.' One wide overhead craft scene showing sticker book on left and tiger board on right. Board desktop scene≈1032×444 px (2.32:1); mobile≈420×346 px (1.21:1). Keep both activities visible, no face-led portrait replacement.

Under scene: two unboxed desktop purchase areas separated by thin vertical line, each with thumbnail left, title/body/price/button right. Mobile: two stacked rows, thumbnail left and title/price/button right; descriptions are omitted in M04 mobile and may remain desktop-only. Horizontal divider separates mobile rows. Preserve shopping bag icon and solid pill Add to cart. Bottom centred Explore creative play link with arrow.

Products: Sticker-by-Number Book₹250; Mosaic Bead Board₹625. Values are reference calculations; live UI uses selected product/variant price, with no silent overwrites of live catalog. Missing product means editor-only placeholder and configuration warning; public cart action requires purchasable variant.

## S07 — Shoppable video

M05. 'Watch them play.' and 'See how it works. Find their next favourite.' Desktop three portrait poster cards, centred play controls, bottom overlay captions, compact white shopping footer and full-width cobalt rounded-rectangle Add to cart. Header right has circular previous/next controls. Mobile one large card plus next sliver, footer visible, dots and swipe hint. Phone casing/status bar in board are presentation only.

Approximate desktop poster 333×527 px (0.63 ratio), mobile 288×474(0.61). Preserve approximate visible frame geometry, not a forced square. Slots: Colour Coder₹450, Sticker-by-Number Book₹250, Mosaic Bead Board₹625. Each linked to exact product and real matching video. Preview label outside UI says posters are not real footage; do not fake playback or invent durations/views.

Click-to-play, one active player, accessible pause/audio/fullscreen where supported. A card tap on the play control must not trigger Add to cart. Navigation controls disabled when no further movement; suppress unneeded carousel controls when all content fits, while retaining visual spacing. Full state contract in docs 08.

## S08 — Growth and connection

M06. Centred headline 'Play that gives them room to grow.' and subline. Small warm decorative strokes/star/triangle, not large coloured blocks. Desktop 2×2 editorial modules separated by thin rules: photo left and text/activity pill right within each. Mobile 4 stacked image-left/text-right rows. Bottom centred Explore ways to play button; mobile full width.

Four modules: Attention & patience / Problem-solving / Creative expression / Connection & emotions. Photos depict pattern play, magnetic building, art and mother/child turn-taking. Body copy describes actions, not promised IQ/attention/behaviour results. Pills are labels in the board, not approved extra navigation. If made interactive later, destinations and semantics require explicit specification.

Target photo proportion about 1.1:1 desktop and≈0.95:1 mobile with bounded crops. Source exact dimensions vary per column; do not stretch people. Latest photos remain generated, and fine product details are not guaranteed.

## S09 — Customer WhatsApp stories

M07. Left-aligned headline 'Your playtime stories.' with blue final word, subline, small orange dash. Three desktop portrait cards; mobile 1 plus next sliver. Light-blue top band, small green platform mark, pale-yellow content area, white footer with matching-product thumbnail/title and View toy. Circular carousel controls below. No mobile phone casing.

All three screenshot positions are placeholders, not real customers. Keep actual future screenshot text intact and readable. Do not recolour genuine conversations to simulate authenticity or reconstruct their content. A full-size viewer may be used for legibility with accessible close/focus handling. If a message refers to no product, omit the matching product footer instead of guessing.

The current board's labels are internal preview instructions. Public production requires real consent-cleared screenshots; otherwise hide this section for shoppers, retain clearly marked editor preview. Previously authorised fictional development samples must not become public reviews. No ratings, dates, names, testimonials or count badges may be invented.

## S10 — Expanded FAQ

M08. Header 'A few things before playtime.' with blue ending and subline. Two pale-blue group panels desktop; stacked mobile. Left Choosing a toy with 5 questions, right Orders & support with 5. First question expanded initially; all others collapsed. Plus/minus controls, thin separators, no clipped multi-line questions.

Bottom peach contact strip: chat outline, Still have a question?, supporting sentence, Ask Mesh blue pill. Desktop horizontal alignment; mobile compact wrap without overcrowding. Use native details/summary or equivalent accessible state. No extra purchase button inside answers. FAQ answer copy/operational status in docs 05/09.

## S11 — Footer

No new board. Preserve the existing native footer and current responsive behaviour. Historical verified labels: Explore Mesh; Home, Catalog, Contact; Small toys. Shared moments.; email signup; existing privacy-policy link. Read back current paragraph, menu handles and policy links; do not recover copy from guesswork. Add operational policy links only when those pages are confirmed. No unverified payment logos, certifications, phone numbers or social profiles. Footer visual fidelity is inherited-state verification, not comparison to an absent mockup.
