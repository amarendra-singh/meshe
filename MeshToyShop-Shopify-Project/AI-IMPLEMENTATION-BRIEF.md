# Instructions to the building AI

First read [HANDOFF-STATUS.md](HANDOFF-STATUS.md). It separates verified file completeness from missing production inputs, and links to the instruction coverage and asset-readiness audit. A successful package check does not mean every production image, video, operational answer or product binding is available.

Build the Mesh Toy Shop homepage in Shopify's existing Dawn-based store using this package. Do not create a generic toy-store template. This package specifies the homepage; supporting product/collection/cart pages must remain functional, but their final visual redesign has not been approved here.

## First actions

1. Read the authority register and inspect all eight original boards in assets/mockups. Compare their mobile and desktop halves independently. These are not whole-page images to embed as a storefront.
2. Read data/design-manifest.json, data/content.json, data/asset-manifest.json, data/asset-slots.json and data/product-map.json.
3. Inspect current store/theme state, complete theme source, product handles/variant IDs, menus, collections, active locales and cart implementation. Historical records mention store 2 zs 0 x 1-0 z.myshopify.com and Dawn theme 198870106278; these are discovery hints, not live-state confirmation.
4. Back up the current theme and make changes in the agreed development theme. The included partial legacy source is an inspection aid only.
5. Resolve dependencies in docs 09 without changing the approved visual composition. Unavailable media should remain explicit development placeholders; do not fabricate replacements.

## Required output

Native merchant-editable sections; accessible responsive DOM; live Shopify products/prices/availability; working collection/PDP routes; cart actions with error states; click-to-play video; genuine screenshot rail when assets exist; ten grouped FAQs; inherited functional footer. Keep all established typography proportions, image placement, card grammar and shallow hero transition.

## Fixed versus inferred

Locked: copy shown on boards, hero curve character, category card anatomy/count, selected discovery file, woman/child imagery direction, broad product range, palette 08, section-specific controls.

Engineering targets: Outfit-like heading/DM Sans-like body pairing, breakpoint thresholds, max widths, spacing scale, focus treatment, dynamic states and tablet interpolation. These fill missing implementation detail; they are not permission to make a new visual concept. Review line wrapping and geometry against the source, not font family names alone.

Unresolved production inputs: genuine lifestyle assets/videos/customer screenshots, exact live product bindings, final logo master/font files, actual shipping/returns/support/payment settings and footer paragraph. Work on all independent implementation while these are resolved. Do not present unknowns as confirmed.

## Completion criteria

Use docs 11 acceptance matrix and record evidence for each section at desktop and mobile widths. Complete package-derived UI checks, Theme Check, actual cart/error/variant testing, video playback, accessibility and performance checks. Demonstrate no unintentional page overflow, content loss, duplicate sections or mockup drift. State any remaining gaps and never call screenshot placeholders functioning videos or genuine reviews.
