# 13 — Evidence, decisions and unresolved inputs

## Evidence hierarchy

Current user instruction declares the homepage design phase done and asks for an unchanged detailed build handoff. Original boards plus the explicit corrections establish the baseline. Historical source notes are included as text snapshots for traceability; they may contain superseded wording and are not a second active specification.

## Current primary technical references

Checked 30 October 2026. Shopify toolkit search failed with 'fetch failed'; direct official documentation was accessed instead. No generated theme code was produced in this documentation task.

- [Sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) — native merchant-editable modules.
- [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) — section configuration/order.
- [Cart API](https://shopify.dev/docs/api/ajax/reference/cart) — locale-aware cart mutations and bundled rendering.
- [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering) — partial HTML refresh.
- [image_tag](https://shopify.dev/docs/api/liquid/filters/image_tag) — responsive image output and intrinsic dimensions.
- [video_tag](https://shopify.dev/docs/api/liquid/filters/video_tag) — Shopify video output.
- [Performance guidance](https://shopify.dev/docs/storefronts/themes/best-practices/performance).
- [Accessibility guidance](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility).

Technical details must be rechecked if implementation occurs against a different platform version/capability. No app pricing, checkout plan entitlement or API operation has been invented in this package.

## Content and catalog evidence

- [Mesh educational catalog](https://www.meshenterprise.in/learning-and-educational-toy.html): product types and source price references. Supplier claims are not independent verification.
- [Mesh home](https://www.meshenterprise.in/): broader range beyond imported subset.
- [AAP play guidance](https://www.healthychildren.org/English/family-life/power-of-play/Pages/the-power-of-play-how-fun-and-games-help-children-thrive.aspx): supports discussion of play and caregiver interaction, not proof of Mesh-specific cognitive outcomes.
- [FunCorp shipping](https://www.funcorp.in/pages/shipping-policy) and [returns](https://www.funcorp.in/pages/returns-cancellation-policy): competitor operational benchmarks only, not confirmed Mesh policy.

## Decisions introduced by this handoff

| Decision | Basis | Status |
|---|---|---|
| Eight-board baseline | Latest non-rejected set + homepage-complete instruction | Frozen for documentation |
| Page assembly order | Preserve chronological selected story, place video before growth and messages beforeFAQ | Explicit engineering assembly; no full-page composite approval claimed |
| Outfit/DM Sans candidate | Shape matching to generated typography direction | Proposed implementation match, exact font unconfirmed |
|750/990 breakpoints | Mobile/desktop reference interpolation and existing Dawn conventions | Engineering starting point |
| Preserve original pastel exceptions | No-change instruction + specific earlier chosen menu/cards | Keep those surfaces; no new unrelated palette |
| Preserve video poster≈0.63 ratio | Actual final board over earlier 9:16 prompt target | Visual-fidelity rule |
| Footer inheritance | Existing verified footer, no new board | Readback required |

## Inputs that remain absent

1. Clean selected lifestyle/category masters, genuine video clips and customer screenshots/permissions.
2. Exact current Shopify bindings for new products/collections, current prices/stock and verified product facts.
3. Final logo vector/font files; candidate typefaces need visual matching and license checks.
4. Current footer brand paragraph/menu settings and confirmed support WhatsApp/contact details.
5. Merchant fulfilment/returns/tax/COD policies and online payment provider.
6. Verified 15% prepaid payment-method enforcement path and discount stacking rules.

These gaps are tracked rather than concealed. They do not block development of independent layout, but they prevent an honest claim that the store is launch-ready. All available images are packaged; no missing original was regenerated or substituted.
