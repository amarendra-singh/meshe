# Shoppable video section — 30 October 2026

Status: requested mockup completed; proposal not selected or deployed. User asked for a video section like other websites. No actual video files supplied. Existing selected sections were not changed.

## Artifact and reference inventory

[Desktop/mobile mockup](../output/design-concepts/mesh-shoppable-video-v1.png). Created using built-in image generation and [saved prompt](../output/design-concepts/video-section-prompt.txt). Reference images inspected: actual Colour Coder, pink cat sticker-book page, yellow tiger bead board in catalog-references. Prior palette08 and typography direction carried forward; no specific competitor video reference supplied.

Headline: Watch them play. Subtext: See how it works. Find their next favourite.

Desktop: three portrait demonstration posters, centred play controls, short action captions, compact white product footer, retail price and full-width Add to cart. Left/right carousel controls beside the heading. Mobile: one large poster and a visible portion of the next, product footer and Add to cart, progress dots and swipe hint. Cream background, navy text, cobalt actions, small tangerine dash. Suggested placement after shopping discovery and before the growth explanation, rather than another RC section.

## Product and price basis

[Mesh educational catalog](https://www.meshenterprise.in/learning-and-educational-toy.html) rechecked 30 October: Colour Coder under Kids Learning Toys, quoted ₹180. User's 2.5× rule gives ₹450. Sticker-by-Number Book ₹100 × 2.5 = ₹250 and Mosaic Bead Board ₹250 × 2.5 = ₹625, previously verified in document20. Retail calculations are proposals under the confirmed rule, not stock verification. No Shopify prices changed. All product names in the UI are concise display names.

## Visual QA

Checked all three product/price pairs and Add to cart controls, three play icons, distinct activities, complete header and mobile swipe affordance. External label explicitly says demonstration posters are not real footage. No fabricated testimonials, viewers, video durations or performance claims.

Remaining differences: generated mobile preview includes a device frame; desktop poster approximately333×527 (0.63 width/height), rather than exact9:16 (0.5625). Mobile poster approximately288×474 (0.61). Real implementation should use consistent9:16 media, object-position tuned to keep the activity visible. Generated images approximate the product; partially obscured Colour Coder and altered fine board details require replacement with genuine demonstrations. Mobile is a regenerated image variant, not an exact crop. Raster colours approximate palette08; CSS must use exact tokens.

## Proposed interaction and performance requirements

This is an implementation specification, not a claim that any features are live:

- Load lightweight poster images initially; fetch the selected video on play. Reserve media dimensions to avoid shifting the page.
- Play one video at a time, with pause, mute/unmute and captions when speech communicates useful information. Never autoplay sound. Pausing/closing must be obvious; keyboard controls and accessible labels required.
- The section remains useful before video loads: product link, current price and purchase action stay visible. Keep product-price/availability tied to Shopify variants, not static image text.
- A single available variant may add directly; multiple required options open a selector first. Loading, success, out-of-stock and cart errors must be visible. Do not accidentally add a product when a shopper taps play.
- Film short demonstrations of the exact SKU and included parts. Show the action early; avoid developmental promises or staged customer endorsements. Obtain guardian consent for identifiable children.
- Use simple native theme media where sufficient. No video-shopping app selected: assess payload, maintenance, actual recurring cost and required cart behaviour before recommending one.

## Why include it

Hypothesis: a visible demonstration clarifies toy mechanics and scale; placing the matching purchase action underneath reduces navigation between watching and shopping. This is different from written benefits or customer messages. Measure video starts, completion, associated adds to cart and eventual checkout against similar traffic; no conversion lift is claimed from this mockup.

Public pages of [Rabitat](https://www.rabitat.com/), [Final Suspect](https://finalsuspect.com/) and [Viaana](https://viaanakidsstore.com/) were checked. Text extraction did not establish their exact video interactions, so this proposal is not presented as a verified copy of any competitor's video implementation.
