# Dawn build status

**Superseded status notice, 25 October:** Read [Homepage expansion and functional audit](09-homepage-expansion.md) for current state. Dawn is now Active. All custom sections are uploaded and added, category collections and New Arrivals are available on Online Store with Newest sorting, and all 17 approved products are now published to Online Store. The storefront remains password-protected. Older pending-upload and usage-limit statements below are historical.

Updated: 24 October 2026 (Asia/Kolkata)

**Later audit update:** Dynamic revision2 and the blue/simplified header have now been saved. Three missing product preview images were repaired; all nine homepage image references persist after reload. Final header-height/cart-icon CSS is local only. Responsive screenshots and search/cart checks remain pending. The current automatic approval-review limit is3:27PM. See [latest section audit](08-section-audit.md), which supersedes older saved/pending and blocker entries below.

## Store state

| Area | Verified state |
|---|---|
| Primary store | `2zs0x1-0z.myshopify.com`, named `meshtoyshop`, on trial |
| Second store | Trial canceled |
| Live theme | Horizon |
| Draft theme | Dawn, theme ID `198870106278` |
| Catalogue | 17 Mesh Enterprise listings imported as **draft** products; not published to sales channels |
| Collections | Four smart collections using product type: Remote Control Toys (7), Interactive Gadgets (7), Puzzles & Play (2), Educational Toys (1); no sales channels |
| Payments / apps | No payment setup or app installation completed in this build |

The product import files are in [data/meshenterprise](../data/meshenterprise/README.md). Source prices and compare-at prices were captured from the public site, not confirmed by this merchant.

## Saved Dawn draft

The latest attached desktop reference supersedes earlier layout proposals. Detailed section comparisons and evidence are in [Desktop reference implementation](07-reference-build.md).

- New custom “Mesh reference homepage” Liquid section saved and added to the draft.
- Original warm toy hero uploaded and assigned, with editable eyebrow, heading, description and Shop all toys action.
- Four pastel category tiles and four editor-only product preview cards use actual catalogue images; both grids have two desktop columns.
- Previous image banner, multicolumn and rich-text sections hidden. Previous work preserved.
- Stacked Mesh wordmark SVG uploaded; width set to180; Save clicked. Its resulting header rendering still needs a fresh screenshot.
- Announcement copy correct; cobalt background, header navigation/icon layout and final dimensions remain unfinished.
- Cart drawer and search suggestions configured earlier; no end-to-end functional pass for this revision yet.

## Local revision awaiting upload

`theme-work/sections/mesh-reference-home.liquid` adds collection resource pickers, merchant-editable colors and CTA URL, live product price ranges and availability, responsive image candidates and empty-section handling. It refines category heights and hero typography against the 848px reference. These changes have **not been uploaded**.

Official Shopify CLI Theme Check: 2 files inspected, no offenses. This is a section-level check; the second file is an empty locale fixture. Do not upload that fixture over Dawn translations. The bundled skill validator is unavailable because `@shopify/theme-check-common` is missing.

Desktop and mobile screenshot comparison, horizontal overflow, keyboard focus, search/cart/collection links and measured performance remain pending. Do not claim a pixel-perfect match or measured speed improvement yet.

## Catalogue quality gate

The imported descriptions reproduce the source site's keyword-heavy marketing text. Before product activation, rewrite and substantiate each listing. In particular:

- Confirm product identity, actual included items, dimensions, materials, colours/variants, batteries and charging, compatibility, and age guidance.
- Verify claims such as “safe non toxic”, “Montessori”, “STEM”, developmental or IQ benefits, “AI”, 2.4 GHz, noise reduction, and battery specifications. Remove unsupported claims.
- Check trademark/licensing permission for the Spider-Man/Marvel listing.
- Check whether “Bumper car Go kart” is a miniature RC toy; source copy also calls it a toddler ride-on toy, which may mislead shoppers.
- Verify selling and compare-at prices with the merchant; do not use an unsubstantiated strikethrough price.
- Confirm ownership/permission for source product photos before publishing them. Image alt text currently repeats each product title rather than describing each distinct gallery image.
- Confirm inventory, shipping weight, tax setup, and the market's required product information.

## Prepaid offer: confirmed terms and implementation

The merchant confirmed **15% off prepaid orders**, while **COD remains available**, with **no discount cap or minimum order value**. The online payment gateway is unknown. There is no active prepaid discount yet.

A plain Shopify automatic percentage discount is unsuitable for this exact requirement because Shopify's documented standard eligibility controls do not select the checkout payment method; it could also discount COD. A candidate solution must enforce the rule at checkout, keep COD available when the discount is absent, and recalculate correctly when a shopper switches payment methods. Test actual INR totals with an online payment and COD, including return from the provider and discount stacking.

Current official App Store candidates (23 October 2026):

| Candidate | Listed cost | Evidence and concern |
|---|---|---|
| [PrepayGuard: Prepaid & COD](https://apps.shopify.com/prepayguard) | Free | Explicitly says selected discount codes hide COD until the code is removed. New listing with no reviews; code entry adds friction. Test before use. |
| [Karto Partial COD & OTP Verify](https://apps.shopify.com/cod-shield-2) | Free tier | Free tier lists discounts on full/partial payment, but its exact full-prepaid rule and checkout behaviour need verification. Two reviews; partial payment is limited to 50 orders/month. |
| [Codify Prepaid Plus](https://apps.shopify.com/prepaid-discount) | $3.99/month after trial | Explicit payment-method targeting and cap/minimum settings. Paid fallback if free options fail; six reviews at research time. |

Do not install an app or advertise the 15% offer until the selected gateway and checkout behaviour are confirmed. App charges and features may change; recheck the listing before installation. See Shopify's [discount methods](https://help.shopify.com/en/manual/discounts/discount-methods), [automatic discount](https://help.shopify.com/en/manual/discounts/discount-methods/automatic-discounts), and [discount combination](https://help.shopify.com/en/manual/discounts/discount-combinations) documentation.

## Current block and next actions

Tabbit browser actions are paused because the automatic approval review reported a usage limit and did not execute the last requested action. The latest rejection said to try again at 8:30 AM on24 October. Do not use another browser or API route to evade that review. The last rejected action was header markup inspection. Once available, upload the local revision and finish header styling and visual verification through Tabbit. No alternate route was used to evade review.

A separate automatic review rejected an active product import because that would publish products to sales channels without explicit approval. The products were imported safely as drafts. Publishing them remains a distinct merchant decision after the catalogue quality gate.

Remaining launch work: confirm the payment gateway and test the prepaid rule; confirm stock and commercial facts; set accurate delivery, refund, and contact details; review mobile, accessibility, search, cart, checkout, and actual performance; choose a Shopify plan and decide when to publish products and Dawn.
