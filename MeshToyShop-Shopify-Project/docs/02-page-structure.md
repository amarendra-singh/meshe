# 02 — Page structure and wireframes

Open [interactive wireframes](../wireframes/index.html). The diagrams show layout and reading order, not new colours, copy or visual approvals. Original boards remain authoritative.

## Assembly order

| Order | Section ID | Role | Board | Desktop | Mobile |
|---|---|---|---|---|---|
| 00 | announcement | Discover range | M01 | Full-width ticker | Full-width ticker |
| 01 | header | Brand, browse, search, cart | M01 | Logo;3 pastel icon pills;search/cart | Logo;search/cart/menu |
| 02 | hero | Curiosity/shared-play invitation | M01 | Wide image, left cream overlay | Copy/actions, shallow convex edge, photo |
| 03 | categories | Four collection routes | M01 | 2 columns ×2 rows horizontal cards | 4 stacked horizontal cards |
| 04 | discovery | Four concrete play activities | M02 | 4 vertical product cards | 2 columns ×2 rows |
| 05 | shared-play | One caregiver play idea | M03 | Photo about 63%, text 37% | Heading/copy → photo →3 steps →CTA |
| 06 | creative-play | Two creative purchases | M04 | Panoramic photo;2 purchase areas | Photo;2 stacked purchase rows |
| 07 | shoppable-video | See mechanics, then shop | M05 | 3 portrait demos and shopping footers | 1 large card + next sliver |
| 08 | growth | Four observable play opportunities | M06 | 2×2 image/text modules | 4 stacked image/text rows |
| 09 | customer-stories | Genuine customer messages | M07 | 3 portrait screenshot cards | 1 card + next sliver |
| 10 | faq | Choosing and ordering help | M08 | 2 groups side by side | Choosing group then order group |
| 11 | footer | Existing support/navigation | Inherit | Existing native Dawn footer | Existing accessible responsive footer |

This sequence preserves the latest section set. The newly requested video section is positioned before growth; the shared-play section remains after discovery. Video was not used to replace another approved section. The exact assembly order is a documented inference, not a recovered full-page design.

## Section boundaries

Only the mobile hero has the shallow curved copy/photo transition. All other sections have straight outer boundaries and ordinary local corner radii. Do not insert waves, giant blobs or gaps between the hero curve and photo. Normal vertical section spacing should be consistent; do not copy the presentation board's grey DESKTOP/MOBILE labels, blank bottom canvas margins, phone frame or preview warning bars into the customer page.

Development-only preview labels stay outside shopper content when placeholders are visible in an explicitly labelled development preview. Genuine public media uses actual content and no mockup instructions.

## Tablet interpolation

No tablet board was supplied. At 750–989CSS px: collapse header to mobile menu, use mobile-style hero copy/photo flow, retain 2 category columns only while their horizontal anatomy remains readable, show 2 discovery columns, stack shared-play content, retain 2 creative purchase areas if each has at least 300 px, show 2 video cards with horizontal overflow for the third, stack growth modules in one column, show 2 customer cards, and stack FAQ groups. At the low end, fall back to mobile layouts rather than squeezing text or shrinking touch controls. These are engineering rules subject to source-matching QA.

## Navigation destination model

Announcement and Explore toys → all products. RC routes → Remote Control collection. Puzzles/Gadgets/Educational → selected corresponding collections. Discovery/play-idea actions → exact selected products. Creative collection link → an existing, verified relevant collection or one configured deliberately; never a guessed URL. Growth CTA → selected learning/play collection. Customer story footer → product actually discussed. Ask Mesh → confirmed support route. Missing destinations are configuration gaps, not '#'.

## Supporting pages

Keep product, collection, search, cart, contact and existing policy routes functional. Use native current theme patterns unless a later approved page design exists. Do not reinterpret homepage completion as approval of an entirely new PDP/checkout layout. Commerce behaviour is specified separately because homepage buttons depend on it.
