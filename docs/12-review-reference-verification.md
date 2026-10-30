# Review reference and layout verification — 27 October 2026

## Current priority and reference

Design/layout first; product photography remains deferred. Continue using native merchant-editable sections, real product/collection data, valid destinations, and the four Karpathy-inspired working principles.

The user's latest desktop/mobile references supersede the earlier two-column review reference: four screenshot cards on desktop, one on mobile, centered heading, cream background, side-mounted red arrow controls. The saved section implements that arrangement with a serif heading, square uncropped images and optional details below each screenshot. Exact distressed font and torn-paper decoration are not reproduced; do not call it pixel-perfect.

## Saved state verified

- Section: Mesh customer screenshots; heading: **What customers say**.
- Four distinct clearly labeled demo screenshots are selected in native image-picker blocks. All four loaded. Demo content — editor only is enabled; demos are not public endorsements.
- Current Liquid source has four desktop columns, two tablet columns, one mobile column; scroll snapping, previous/next controls, ArrowLeft/ArrowRight and Home/End support, reduced-motion handling and cleanup on section removal.
- Controls appear only when content overflows. With exactly four cards fitting on desktop, arrows hide; mobile has working side arrows. More screenshots can be added/reordered using Shopify blocks (up to 12).
- Each screenshot opens its own full-size Shopify CDN image. Optional related products use native product pickers. Reviews do not import automatically from WhatsApp.
- Videos remain immediately after the reference/new-arrivals section, with four editor-only demo posters. Real Shopify-hosted product videos populate from the configured collection as described in document 11. Actual playback awaits genuine video assets.
- Footer now contains native Explore Mesh menu links (Home, Catalog, Contact), and **Small toys. Shared moments.** with the intended brand paragraph. Correct text persisted in the storefront after reload. Email signup and existing privacy-policy link remain. No invented shipping/returns policy was added.

## Verification evidence

Desktop editor: viewport 1101px including scrollbar; document 1086px. Four cards measured 241.5px each, images about 242px square, object-fit contain. Save disabled. Screenshot visually inspected.

Mobile editor: viewport 375px including scrollbar; document 360px. Each screenshot/card 312px wide and high; track 312px. Next moves to another card. End reaches scrollLeft 996, equal to maximum 996, and disables Next. Home returns to start and disables Previous. Screenshot visually inspected. Orange outline in mobile evidence is keyboard focus.

Storefront after reload:

| Section | Observed result |
|---|---|
| Header | 97px desktop height |
| Hero/story CTAs | Both reach /collections/all, HTTP 200 |
| Four category tiles | Correct collection destinations, all HTTP 200 |
| New arrivals | Four actual product cards |
| Category showcases | 4/2/1/4 actual cards, respective collection links preserved |
| Review/video demo sections | Zero public media rails; no fictional samples exposed |
| FAQ | Five native disclosures |
| Footer | Correct saved copy and native menu destinations |
| General | No empty/hash-only main/footer links, no Liquid errors, no horizontal overflow (1394px document inside 1409px viewport including scrollbar) |

Footer Home/Catalog/Contact/Privacy destinations returned HTTP 200 in the preceding pass. Contact includes a real contact form; it was not submitted. Shopify CLI Theme Check passed again: seven files, no offenses.

Evidence: docs/evidence/reviews-2026-10-27/desktop-review-layout.png and mobile-review-layout.png. Earlier footer/review evidence remains in docs/evidence/layout-2026-10-26/.

## Dynamic content contract

- Product names, media, prices, price ranges, availability and URLs come from Shopify products.
- Category showcases read selected smart collections. New products require the matching existing product type and Online Store publication; section limits determine how many newest products are shown.
- New Arrivals currently includes price > 0 and sorts by creation date, newest first. Free products and old products newly activated are not necessarily the newest displayed entries.
- Adding a product in this pass was not used as a test, so no synthetic catalogue item was published.
- Screenshot blocks update when the merchant adds/replaces/reorders their images. Review content is not inferred from product publication.

## Remaining work

1. Continue overall navigation, collection/product-page design and responsive consistency. Homepage/reference work is verified to the extent recorded, not declared fully finished.
2. Supply genuine videos and permission-cleared customer screenshots before enabling those entries for shoppers; test playback and final product associations then.
3. Product imagery and imported option-label cleanup remain on the later to-do list.
4. Shipping/returns/stock/payment setup and the correctly enforced 15% prepaid incentive remain separate launch work. No speed score, conversion uplift or checkout readiness is claimed.
