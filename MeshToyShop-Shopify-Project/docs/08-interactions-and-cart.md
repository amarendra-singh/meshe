# 08 — Interactions, cart and failure states

These contracts fill states not visible in static mockups. They do not add new homepage sections.

## Navigation/search/menu

Ticker/category links are real anchors. Header search opens current native predictive search where available; Enter/search submit reaches results. Handle no results and network failure without trapping users. Mobile menu opens via labelled button, traps focus while modal, closes with Escape/close/backdrop as appropriate and restores focus to trigger. Keep cart count synchronised. No hover-only essential navigation.

## Add to cart state machine

Applies to creative and video shopping footers. Discovery retains View toy.

| State | UI and action |
|---|---|
| Single available variant | Add to cart submits selected variant and quantity 1 |
| Multiple required options | Open accessible option picker or route to PDP; do not silently choose colour/size |
| Adding | Prevent duplicate submissions; show busy feedback and retain readable context |
| Success | Update native cart drawer/count/subtotal; announce added item; preserve section position |
| Sold out | Disabled Sold out state; no fabricated stock count or urgency |
| Stock/quantity rejected | Show server message near action; restore control; don't show success |
| Network timeout | Explain retry; reconcile cart before blind retry to avoid duplicate quantities |
| Product missing/unpublished | Editor configuration notice; no dead public purchase form |
| Cart-render failure after successful add | Reconcile cart and expose a working View cart path; never double-add to repair HTML |

Reuse the active Dawn product form/cart components where compatible. If custom AJAX is required, use Shopify's locale-aware [Cart API](https://shopify.dev/docs/api/ajax/reference/cart). Add uses variant identity, not product ID. Distinct lines with properties must be updated by the correct line key. Do not assume a storefront line remains at the same numeric index after another change.

Use bundled section rendering for the cart surfaces already present. A null returned section is a rendering failure, not necessarily a failed cart mutation. Shopify's [Section Rendering API](https://shopify.dev/docs/api/ajax/section-rendering) supports partial UI refresh; maintain event/focus handling after replacement. Verify current section IDs and locale routes rather than copying examples blindly.

Cart controls: quantity changes and removal update totals, discount lines and badge consistently; empty cart has useful browse link. Announce errors accessibly. Checkout goes to Shopify checkout, with the actual server totals. Don't calculate a prepaid discount in browser CSS/JS and present it as an enforced total.

## Video playback

Initial state loads posters, not three full video downloads. Play fetches/initialises only chosen video. Play/pause/mute controls are independently labelled; never autoplay sound. Pause other clips when a new one starts and pause when a player leaves active view, document is hidden or section removed. Respect reduced-motion preferences and avoid automatic looping previews by default.

Native inline controls or accessible expanded player are acceptable if the visible initial card matches M05. If modal: Escape/close, focus containment/restoration and no background scroll leak. Caption meaningful speech, offer fallback text describing the action. Poster failures should not remove product purchase information. Video failures display a retry/fallback and working PDP link.

Product footer remains tied to the demonstrated SKU. Price/availability may differ from the historical reference; report data differences without altering merchant prices. Don't display fictional engagement metrics or invent a length label.

## Video/customer carousel

Prefer native horizontal scroll with scroll-snap and small scoped navigation logic. One gesture must not hijack vertical page scrolling. Previous/next move a predictable card step, disabled at boundaries; no infinite duplication of fake items. Dots reflect actual visible item and are labelled when interactive. Keyboard arrows/Home/End may operate a focused track; don't intercept page-wide keys. Hide redundant controls when there is no overflow. Keep 44 px targets and visible focus.

For screenshot enlargement, retain full original aspect ratio, readable text and an obvious close control. A screenshot is not automatically a link to buy; matching-product footer has its own real PDP link. No automatic WhatsApp ingestion or message sending is part of the design.

## FAQ/support/newsletter

First FAQ open, others closed by default. Use semantic disclosures with full question in summary and plus/minus as decorative state cue. Multiple answers may remain open unless merchant explicitly requests an exclusive accordion. Do not animate height in a way that clips content or ignores reduced motion. Order FAQs require verified answers before public release.

Ask Mesh uses confirmed contact page or business WhatsApp link. It must not trigger an outgoing message automatically. Existing newsletter form shows clear success/error feedback and appropriate consent handling; no automatic marketing enrolment from cart interactions.

## No-JS / offline degradation

Primary links remain usable. Native product forms route to cart where supported. FAQ remains readable via native disclosure. Video exposes a useful fallback link/message. Never make the entire homepage dependent on a client-side render or a third-party widget being available.
