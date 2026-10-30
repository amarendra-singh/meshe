# 03 — Design system and responsive specification

Exact tokens are in [design-tokens.json](../data/design-tokens.json). The source boards are raster concepts, not reliable font or colour samples.

## Colour and type

| Role | Value | Rule |
|---|---|---|
| Primary | #2354D7 | Purchase actions, links, selected headline emphasis, ticker |
| Page cream | #FFFCF5 | Dominant large surfaces |
| Tangerine | #FF8547 | Short strokes and warm accents; not small text on cream |
| Yellow | #FFE16B | Restrained highlights |
| Navy | #172B4D | Main headings/body/control outlines |
| White | #FFFFFF | Cards and text on primary buttons |

Existing category/menu/discovery pastel backgrounds remain as shown: pale blue, peach, pale yellow and pale mint. Treat them as tinted component surfaces rather than extra competing action colours. Products retain their real colours. Do not apply colour filters to photos.

Font identity is not confirmed by generated images. Proposed implementation match: Outfit variable for rounded confident headings; DM Sans for body/UI. Prefer available licensed/self-hosted WOFF2 or Shopify-supported font settings; verify actual files/license before adding. Preserve the full Mesh Toy Shop name and orange burst; the legacy SVG is not automatically the approved wordmark master. Do not replace headings with black, a serif face, handwriting or thin geometric display type.

| Text role | Desktop target | Mobile target | Behaviour |
|---|---|---|---|
| Hero H1 | 64–76 px,700–800,1.0–1.06 line-height | 38–44 px,1.02–1.08 | 'Let curiosity' / 'lead.' where width permits |
| Section H2 | 42–56 px,700–800,1.06–1.15 | 30–36 px,1.08–1.16 | Meaningful phrase wrapping; never overflow |
| Card H3 | 20–26 px,650–750 | 17–20 px | Allow 2 lines, no ellipsis for product identity |
| Body | 18–22 px,400–500,1.4–1.5 | 16–18 px,1.4–1.5 | Navy/muted navy with verified contrast |
| Buttons | 17–19 px,600 | 16–18 px,600 | Minimum 44CSS px interaction area |
| Eyebrow | 12–14 px,600,0.10 emtracking | 12–13 px | Uppercase only where board uses it |

These sizes are starting targets; generated boards use different presentation scales. Match relative hierarchy and wrapping at the same effective viewport. Do not enlarge a later heading until it rivals the hero merely because its board has a large export title.

## Breakpoints and container

- Mobile:320–749 px. Tablet:750–989 px. Desktop:990 px+. Test widescreen at 1920 px; constrain readable content rather than stretching cards indefinitely.
- Initial container target:1440 px maximum with 32 px desktop and 16 px mobile gutters; tablet 24 px. Adjust only to match the reference proportions, not to change component layout.
- Standard gaps: desktop 20–24 px, mobile 12–16 px. Section vertical padding: desktop 56–72 px, mobile 32–44 px. Hero/category boundary is tighter, approximately 16 px.
- Button radius 999 px except video shopping buttons, which use the more modest rounded rectangle visible in M05. Content radius 12–20 px; desktop hero overlay 28–32 px. Do not turn all cards into identical pills.
- No horizontal page overflow. Only deliberate video/customer tracks scroll horizontally. Preserve document-level vertical scrolling on touch.

## Hero curve geometry — regression-critical

Reference sampling: V7 centre dip≈6.6% of sampled width; rejected V10 ≈ 10.2%; V11≈6.2%. Measure the curve's central offset relative to the straight chord between its left/right join endpoints, not the overall panel height.

Implementation acceptance target:5.5–7.0% of mobile hero width. Example at 390 px content width:21.5–27.3 px dip, target 24.2 px. At 375 px:20.6–26.3 px. The cream panel overlaps the image continuously; photo top is not an independently rounded box. A shallow elliptical/pseudo-element or equivalent scalable path may be used, but retain room for all text and CTA above the curve. No fixed height that clips translated/enlarged text.

## Element-specific responsive behaviour

| Component | Required mobile treatment | Never do |
|---|---|---|
| Header | Hide desktop pills into menu; keep search/cart/menu visible | Shrink pills to unreadable labels or hide ticker |
| Categories | Single-column wide horizontal cards; retain description and arrow | Convert to 2×2 square icon tiles |
| Discovery | 2 columns with consistent photo/text/action slots | Carousel or 1 column at normal 375–430 width |
| Shared play | Copy above photo; steps and CTA below | Photo first on mobile or new curve |
| Creative | Preserve both activities in image crop; two purchase rows | Reuse discovery card grid |
| Video | Large portrait + next sliver; footer/action visible | Autoplay sound or tiny four-up mobile videos |
| Growth | Photo left, copy right within 4 stacked modules | Four full-screen hero banners |
| WhatsApp | Large readable message card, next-card glimpse | Invented conversation or unreadable thumbnail grid |
| FAQ | Two labelled groups stacked, first question initially open | Truncate question text or replace with 4 questions |

At 320 px and 200% text zoom allow natural reflow. If two discovery columns cannot retain usable text/actions at large zoom, accessibility reflow is an explicit exception, not permission to change the ordinary mobile design. Landscape phones use available width rules, not user-agent detection.

## Image fitting

Packshots: contain, preserving complete product and proportions. Lifestyle photos: cover only when approved focal areas remain intact. Hero mother, child and toy must remain recognisable; don't crop faces or remove the woman. Use separate mobile art-directed assets where needed. Customer screenshots: contain and offer enlargement, never crop message text to force a ratio. Video footage may be 9:16 while display frame follows M05≈0.63 width/height; keep essential action in the safe centre.
