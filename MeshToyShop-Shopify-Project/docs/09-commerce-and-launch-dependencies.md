# 09 — Catalog, commercial rules and launch dependencies

## Catalog scope and pricing

Mesh Enterprise at https://www.meshenterprise.in/ is part of the merchant's range. The historical 17 Shopify imports are a subset, not the whole assortment. Do not import unrelated household products solely because they share a supplier website. Existing product-map records are references and must be reconciled to current Shopify products.

Confirmed pricing rule for NEW IndiaMART selections: 2.5× listed quote. No requested rounding. Verified examples: Colour Coder 180→450, sticker book 100→250, mosaic board 250→625. Existing Shopify prices must not be silently overwritten. Supplier quotes/MOQs are not retail stock guarantees. No compare-at savings, fabricated sale percentages or fake MRP should be derived from this multiplier.

Product listing requirements: verified exact toy/variant, current sellable stock, actual price, materials, dimensions, contents, battery requirements, manufacturer age guidance and warnings. Supplier marketing copy is not proof of cognitive benefit or certification. Data/product-map.json deliberately leaves unresolved Shopify IDs null.

## Prepaid incentive

Historical confirmed merchant rule:15% discount for prepaid orders, COD available, no cap and no minimum. Gateway work remains deferred; no enforcement solution is verified in this handoff. The current ticker is the selected discovery message, not a prepaid advertising strip.

Before activation, verify current plan, checkout/gateway capabilities and any chosen app's supported enforcement path. A payment-method-dependent offer cannot be considered safe merely because the cart shows a discount or a banner says prepaid. Switching to COD, express checkout, gateway failure, abandoned/resumed checkout and discount stacking must all be tested. Do not promise a particular Shopify Function/UI extension can inspect a final payment choice without confirming current capability.

Required test outcomes: prepaid eligible order receives 15%; COD receives no prepaid benefit; switching methods recalculates correctly; no unintended cap/minimum; tax/shipping treatment explicit; existing discount combinations intentional; refunds use correct paid totals. No live real-money test order without the user's relevant authorization. Record payment provider fees and contribution margin before enabling the incentive.

## Competitor-derived FAQ proposals — not active Mesh terms

The user requested copying competitor policies. We researched and paraphrased; competitor fulfilment capacity is not Mesh capacity. Visual questions are fixed, operational answers remain pending.

| FAQ | Prepared proposed answer | Dependency |
|---|---|---|
| When will my order arrive? | We aim to dispatch within two working days. Estimated delivery is 3–8 working days after dispatch, depending on your PIN code. Tracking is shared once shipped. | Confirm actual warehouse/courier timings and tracking automation |
| How much does shipping cost? | Shipping is calculated at checkout before payment. | Configure actual rates and exceptions; no free-shipping threshold approved |
| Can I pay on delivery? | COD is available for eligible orders and PIN codes, subject to confirmation. Available payment options and charges appear at checkout. | Verify COD coverage, fees and validation |
| What if an item arrives damaged? | Contact us within 48 hours with your order number and photos of the item and packaging. Keep packaging while we review and arrange the appropriate resolution. | Confirm reporting window, replacement/refund process; do not imply statutory rights expire |
| Can I cancel or return an order? | Contact us promptly to request cancellation before dispatch. For an incorrect or defective item, contact support with the order details. | Finalize eligibility, reverse pickup, costs, refund method/timing and exceptions |

Source checked 30 October: [FunCorp shipping](https://www.funcorp.in/pages/shipping-policy) lists dispatch within 2 working days, location-dependent estimates, ordinary shipping₹70 up to₹699/free above₹699 and₹100 additional COD handling. These are observations, not Mesh rates. [FunCorp returns](https://www.funcorp.in/pages/returns-cancellation-policy) uses wrong-item/defect eligibility, same-day damage evidence wording plus a 48-hour return contact window, and a four-hour cancellation request condition. The proposed Mesh wording above intentionally avoids copying that inconsistency. Neither source establishes a legally sufficient Mesh policy; publish only operationally accurate final terms.

## App/plugin and retention boundaries

No new app is required for a static homepage, native FAQ, product-linked video or screenshot blocks. Start with native theme/Shopify features. If a later feature needs an app, compare current subscription cost, page weight, checkout compatibility, merchant workflow and maintenance using official documentation and actual store testing before selecting it. No paid subscription is approved by this package.

Cart recovery/retargeting is a later configured flow, not silently bundled into this design. Specify consent, eligible audience, suppression after purchase, frequency, genuine incentive and attribution before enabling campaigns. Don't send email/WhatsApp campaigns from this documentation task. No unsolicited extra popup or new discount path should appear in the approved homepage.

## Release blockers versus build tasks

Layout can be built immediately against the frozen references. Before launch: real media/permissions, resolved product IDs and accurate data, confirmed support identity/policies, shipping/taxes, checkout/payment tests, enforced prepaid rule if advertised, privacy/consent configuration and final accessibility/performance verification. User approval of the homepage does not resolve those operational inputs.
