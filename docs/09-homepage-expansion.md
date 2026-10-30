# Homepage expansion and functional audit

Updated: 25 October 2026, Asia/Kolkata. This supersedes the older saved/pending status in documents 05–08.

## Confirmed store state

- Shopify theme editor now identifies Dawn `198870106278` as **Active**. This changed between sessions; this agent did not click Publish.
- User explicitly approved all 17 product details, prices and Online Store publication. All 17 were set Active and included in Online Store only on 25 October. Admin verification showed Active and one channel on every row.
- New Arrivals `694940795046`, handle `new-arrivals`, was created and saved. Automatic rule: variant price greater than ₹0. Sort: Newest. Available on Online Store only.
- Four category collections retain their automatic product-type rules. Each was saved with Newest sorting and Online Store availability. All 17 matching products are now published.

| Homepage category | Collection handle | Product type rule | Collection ID |
|---|---|---|---|
| Remote Control | remote-control-toys | Remote Control Toys | 694832595110 |
| Gadgets | interactive-gadgets | Interactive Gadgets | 694832660646 |
| Puzzles & Play | puzzles-play | Puzzles & Play | 694832791718 |
| Educational | educational-toys | Educational Toys | 694832824486 |

## Saved implementation

All are native Shopify sections: merchants can reorder sections/blocks and edit their settings in the built-in theme editor. No paid page-builder app was installed.

1. **Mesh reference homepage** — original hero, two-column category tiles and two-column product grid. The automatic mode reads New Arrivals; product titles, images, URLs, prices, ranges and stock labels come from Shopify products.
2. **Mesh category showcases** — four separately editable collection blocks, each reading current collection products. Desktop four-column and mobile two-column grids. Empty collections show an explanation only in the editor and are omitted for shoppers.
3. **Mesh screen-free story** — original family-play photograph, editable benefit copy and CTA. No medical/developmental guarantees or false scarcity.
4. **Mesh product videos** — scroll-snap rail, native video controls, lazy loading and preload none. Automatic mode reads the first hosted video from products in the selected collection, defaulting to New Arrivals. Scans the first 50 collection products and displays up to eight by default. Curated editable blocks remain available.
5. **Mesh customer screenshots** — editable screenshot rail with enlarged-image links and optional transcripts. Demo blocks are gated by `request.design_mode` and do not render for shoppers.
6. **Mesh helpful FAQs** — five editable native disclosure blocks. Contact CTA is omitted until a destination is selected.

The shared `mesh-product-card` snippet uses a square white frame and uncropped `object-fit: contain` images. Actual product photos were retained. Generated product-cleanup concepts were not substituted for verified catalogue photography.

## Assets

- `output/campaign/mesh-family-play-portrait.png`: final generated aspirational family-play scene; uploaded and assigned to the story section, verified after reload. It replaces the wide `mesh-family-play.png`, which cropped a parent's face in the tall desktop panel. All three faces remain visible in the corrected composition. Image description is editable. Mobile frame verified at 360 × 450px (4:5). It is not a customer testimonial. Prompt and tool details are in `output/campaign/README.md`.
- `output/campaign/mesh-demo-conversation.png`: fictional WhatsApp-style conversation, explicitly labeled **DEMO — NOT A REAL CUSTOMER REVIEW** and **Replace before launch**. Uploaded and assigned with the editor-only demo flag enabled.
- Existing real catalogue images provide editor-only product/video storyboards until product publication and real videos are supplied. They are not playable videos.

## Reference interpretation

- User's selected desktop image governs the cream/navy/cobalt palette, hero hierarchy, two-column categories and initial product grid.
- User's later image-fit correction is implemented with square frames, superseding the initial wide card crop.
- Kobbo's observed homepage informed the product-video rail and family-play story. Its developmental statistics were not copied.
- Final Suspect's observed homepage informed the product → social proof → FAQ flow. Its reviews, customer counts and promotional claims were not reused as Mesh evidence.
- No measured conversion superiority or pixel-perfect match is claimed.

## Verification completed

- Official Shopify CLI Theme Check: seven files, no offenses after the collection-count fixes and automatic video addition.
- Shopify runtime found an error that static lint missed: empty collection counts compared as strings. Both product sections now coerce the count with `default: 0 | plus: 0`.
- After an editor reload, runtime Liquid error count was zero. Four product image frames measured 497 × 497 pixels with white backgrounds at the checked desktop preview width.
- Both newly generated images loaded successfully after reload.
- All six intended section types were present; four category headings and five FAQ blocks were generated.
- Header and hero CTAs resolve to `/collections/all`; category tiles resolve to the four correct collection handles.
- An accidental default Featured Collection section from the picker was removed, and the intended FAQ was saved.
- Collection saves confirmed all four category sorts as Newest and each as available on one channel.
- Automatic product discovery switch verified `aria-pressed=true`. Automatic product-video controls are present after reload.
- Desktop preview width/scroll width: 1081/1081; mobile: 360/360. No horizontal overflow at these checked widths.
- Mobile product frames: four at 158 × 158px. No failed images in the checked editor DOM.
- Mobile video-rail next arrow moved scroll position from 2px to approximately 249px; FAQ disclosure opened successfully.
- Live storefront: zero Liquid errors and zero demo review/category preview cards.
- Shop all and all four category URLs returned HTTP 200, with no 404 title.
- Search submitted `maze` to Shopify's real search results page; zero results is expected while products are drafts.
- Cart drawer opened its empty state with Close, Continue shopping and Log in controls. No checkout or order was submitted.

## Automatic update contract

For a product to appear to shoppers, it must be Active, available to Online Store and the relevant market, and match the collection rules. Set its product type to one of the exact values above to populate the matching category. New Arrivals includes products priced above zero; free products are excluded by that rule. Newest means Shopify creation date, not date first published. Existing older drafts activated later may appear below more recently created products.

Product videos must be genuine hosted videos in Shopify product media. Reviews and FAQs are merchant-authored editorial content; they are editable, not automatically invented from product listings.

## Remaining launch dependencies

- Product publication and add-to-cart tests are complete. Checkout/payment testing remains deferred. No synthetic catalogue item was published merely for testing.
- Real video playback and review-gallery behavior with multiple authentic screenshots require the merchant's assets. Empty/demo branches were checked; no real playback is claimed.
- Supply real product videos and permission-cleared customer screenshots, replacing demo blocks before exposing them.
- The user approved imported product facts/prices and publication. Inventory is not tracked on all 17 products. Confirm operating stock, shipping/returns and payment gateway before opening sales; the prepaid offer remains deferred.
- Measure storefront performance after real catalogue/media publication; no speed score has been claimed.


## Post-publication verification — 25 October evening

- All 17 products: Active, Online Store only; all 17 observed product URLs returned HTTP 200 with correct product titles/prices and no Liquid errors.
- Store remains password-protected; catalogue publication does not remove this protection or configure a payment gateway.
- New Arrivals homepage cards: Remote watch car (850), Intelligent Car (1499), Bumper car Go kart (1999), RC Stunt Bike (1499), in INR. Automatic creation-date sorting explains why these supersede the original four editorial preview products.
- Category collections contain 7 remote-control, 2 puzzle, 1 educational and 7 gadget products. Homepage shelves display 4 / 2 / 1 / 4 respectively. All collection destinations returned HTTP 200.
- All-products collection reports 17 products: 16 on page 1 and Stunt Spiderman Toy on page 2. Duplicate links per Dawn card were deduplicated when counting products.
- Real homepage card navigation opened Remote watch car, with its matching 850 INR sale price. Add to cart passed; quantity two updated total to 1700 INR. The original cart was empty, and the test item was removed afterward. No checkout/order was submitted.
- Search for maze returned six results with 3D Maze Cube first, using native Shopify search.
- Desktop main product frames measured 578 × 578px; shelf frames 296 × 296px, all using contain. The four main product images loaded successfully.
- Populated mobile preview: 360px viewport and 360px document width, no horizontal overflow or Liquid errors. Main product frames 158 × 158px; shelf frames 155 × 155px; category grids have two columns.
- Public storefront continues to omit demo reviews and empty product-video rail. Five FAQ disclosures remain present.
- One import-quality issue was found during cart testing: the option name was imported as Default Title instead of Shopify's canonical Title. Correction status is recorded below.


## Design-first checkpoint — 25 October evening

User redirected priority to design first and requested continuous progress saving. Further catalogue normalization and checkout work are deferred while homepage design is refined.

- Two canonical option-name corrections saved: Remote watch car and Intelligent Car. The remaining 15 products retain the original option name; no subsequent correction was committed. Bumper car Go kart was opened but its option control remained disabled, so no edit was made.
- The import CSV now uses canonical option name Title / value Default Title for all 17 products, preventing repetition on a future deliberate import. Do not reimport blindly: the historical CSV still carries draft/unpublished fields.
- Immediate visual gaps: mixed supplier/packaging imagery in category tiles, an awkward wrapped Remote Control arrow, and busy catalogue photography compared with the clean selected reference.
- Next design pass: consistent original category illustrations/cutouts, tidy label/arrow alignment, desktop and mobile visual comparison. Preserve real catalogue photos and dynamic collection/product connections.
