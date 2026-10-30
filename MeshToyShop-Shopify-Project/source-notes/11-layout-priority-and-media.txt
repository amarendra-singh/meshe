# Design and layout checkpoint — 26 October 2026

The review layout below is historical. The user's new four-desktop/one-mobile reference and current verification are recorded in [document 12](12-review-reference-verification.md). Footer copy/navigation and four review demo selections are now saved and verified there.

## Confirmed priority

Design and layout first. Product imagery and catalogue cleanup are deferred. Use native editable Dawn sections, actual Shopify product/collection data and working destinations. Inspect, simplify, make focused changes, verify. User has authorized necessary plugins; no additional builder is needed for the current work.

## Saved and verified

- Video rail moved directly after the reference section (hero, categories and newest products), before the family story. Customer screenshots remain before FAQ. Native drag/drop save and reloaded editor order verified.
- Category showcases adapt to rendered counts: one/two products use a desktop copy/product split; three use three columns; four-plus use four columns. Mobile uses at most two columns and centers a single card. No duplicated filler products.
- Review track supports two large desktop screenshot cards; a lone card centers at maximum 600px. Mobile remains a swipe rail when multiple cards exist.
- Only mesh-category-shelves.liquid and mesh-media-rail.liquid uploaded. Backups in output/backups/layout-2026-10-26/.
- Official Shopify CLI Theme Check: seven files, no offenses. Toolkit validator could not run because @shopify/theme-check-common is missing.
- Desktop: real product counts 4/2/1/4, correct category destinations, no section overflow, no empty/hash-only main links or Liquid errors.
- Mobile: document 360px inside viewport 375px including scrollbar; two-column cards 156px, single-product grid 324px. No horizontal page overflow. Video track 324px/974px; Next moves it and enables Previous. FAQ opens/closes. Single review has no redundant arrows.
- Evidence: docs/evidence/layout-2026-10-26/. One review screenshot was inspected but its evidence copy and this document save were interrupted by an automatic-review usage limit. Work resumed after the stated retry time.

## Media content and automation

Editor sections: **Mesh product videos** and **Mesh customer screenshots**. Four demo posters and one clearly labeled fictional screenshot are editor-only. Shopper-facing sections hide until genuine entries exist. The posters are not playable videos.

Automatic videos use the first Shopify-hosted video from eligible products among the first 50 entries in the selected collection, default New Arrivals, up to the configured limit. Products must be published to Online Store and belong to the collection. Screenshots are native merchant-managed image/product blocks, not an automatic WhatsApp import.

Current page order: reference → videos → family story → category showcases → customer screenshots → FAQ.

## Competitor recheck

- Kobbo: Unboxing & Play Moments follows its early-years story and precedes founder/benefit content. Product-linked titles observed. Initial DOM contained no videos; full player loading/performance not verified.
- Final Suspect: Trusted By Creators → What customers says → rating content → FAQ; 12 video elements observed. Their review/rating claims were not verified or copied.
- Supplied references guide four portrait video cards and two larger review screenshots.

## Deferred product-image work

Before the priority correction, Remote watch car's existing clean image 1791209919_bFBgT2.webp was made featured, saved and reload-verified. Other product images remain unchanged in this pass.

Built-in image generation created output/product-photography/intelligent-car-studio-proposal-v1.png from intelligent-car-source.webp. It is not uploaded or approved. Prompt: extract only the top-left lime car onto a square white studio background with a contact shadow; preserve rounded body, windows, stripes, pink/red 13 hood marking, white hubs/black tyres, grille and viewpoint; remove other views, dimensions and promotional graphics; add no accessories or claims. Small-detail fidelity and colour still require review.

## To-do

1. Continue section-by-section desktop/mobile design checks, footer/navigation and collection/product-page consistency.
2. Complete media design review using genuine videos and permission-cleared screenshots when supplied. Verify product associations and actual playback then.
3. Product photography later: review Intelligent Car proposal, cleaner existing RC Stunt Bike gallery option, remaining supplier collages.
4. Future products: use the exact existing category product types and publish to Online Store. New Arrivals currently uses price > 0 and Newest creation order; free products are excluded.
5. Imported option-label cleanup remains deferred for 15 products. Do not blindly reimport historical CSV.
6. Later launch work: stock, shipping/returns/contact policies, gateway and correctly enforced 15% prepaid discount with COD. Payment setup is explicitly deferred.

No speed score, conversion uplift, pixel-perfect equivalence or launch readiness is claimed.
