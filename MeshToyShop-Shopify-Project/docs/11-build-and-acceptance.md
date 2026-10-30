# 11 — Build sequence and acceptance checklist

## Build stages

1. **Inspect and freeze:** complete current theme pull/read, backup, screenshot current desktop/mobile, read all eight reference boards, confirm product/menu bindings. Record current source revision and theme ID.
2. **Foundation:** add scoped tokens, font matching, header/ticker/menu controls. Preserve base theme and native cart. No payment work yet.
3. **Hero/category pass:** implement M01, measure shallow mobile curve, verify four category descriptions/arrows/image positions. Compare at same effective width before moving on.
4. **Product/editorial pass:** M02/M03/M04 with native data, no extra RCshelf. Verify exact discovery first render and distinct creative composition.
5. **Media/benefit/help pass:** M05/M06/M07/M08 with genuine-media gates and full error/empty states. Preserve footer.
6. **Commerce verification:** every product route, variant path, Add to cart, drawer quantity/removal, duplicate-click/network failure, checkout entry. Keep operations test-safe.
7. **Responsive/accessibility/performance pass:** matrix below; verify no regressions to already-accepted sections.
8. **Review and release preparation:** screenshots, short change log, residual gaps, rollback reference. Deployment depends on current user instruction, not this document alone.

## Viewport matrix

| CSS width | Intent | Main checks |
|---|---|---|
| 320 | Small-phone edge | Header fit, no clipped copy,44 pxcontrols, readable discovery |
| 375 | Baseline mobile | V11 curve,2×2 discovery,4 horizontal categories |
| 390 | Common mobile | Media rails 1+peek, CTA fit, no page overflow |
| 430 | Large mobile | Natural line wraps, images not overcropped |
| 749/750 | Breakpoint boundary | No disappearing content or abrupt duplicate controls |
| 768 | Tablet portrait | Defined interpolation,2 column where appropriate |
| 989/990 | Desktop boundary | Menu mode and hero overlay transition |
| 1024 | Small desktop/tablet landscape | No compressed heading/photo collision |
| 1280/1440 | Desktop |4 discovery,3 video/story cards,2×2 categories/growth |
| 1920 | Wide desktop | Max-width restraint, no stretched product photos |

Test mobile portrait/landscape, modern Chromium plus Safari/WebKit and Firefox when available; document any environment not exercised. All dimensions refer to CSS viewport, not screenshot file pixel count or scrollbar-inclusive desktop window.

## Visual acceptance by section

| ID | Pass evidence |
|---|---|
| S00–01 | Ticker visible; full brand; correct pastel icon pills; search/cart/menu functional |
| S02 | Woman/child scene; exact short copy;2 CTAs; continuous shallow mobile edge 5.5–7.0% |
| S03 | Exactly 4 wide cards, correct order/copy, plain lower-left arrows, large right products |
| S04 | Exact M02 selection;4 desktop / 2 mobile; full titles/descriptions; View toy; no extra RCitems |
| S05 | Desktop photo≈63% split; mobile copy/photo/steps/CTA sequence;3 steps |
| S06 | One shared scene,2 purchase areas, correct products/prices, Add to cart states |
| S07 |3 portrait demos; mobile 1+peek; product footers; actual playback only with actual media |
| S08 |4 distinct modules; exact action-based copy; no unsupported outcome claims |
| S09 |3 desktop/1+peek; real screenshots or explicit development placeholders; no fake reviews |
| S10 |10 questions in 2 groups; first open; all text readable; verified answers |
| S11 | Existing footer readback preserved; legitimate links and functional signup |

## Interaction acceptance

- All visible links resolve to intended resources; no '#' or unbound objects.
- Multiple-variant products require selection; unavailable variants cannot be added.
- Add succeeds once, shows server-confirmed result and correct cart count. Errors remain recoverable.
- Quantity/removal and empty cart work; no stale subtotal or line mismatch.
- Video starts only on action, pauses other players, exposes pause/audio controls; video failure leaves product action usable.
- Carousel previous/next/boundaries, touch, keyboard and reduced-motion behaviour verified; no unwanted page scroll lock.
- FAQ and modal focus behaviour pass keyboard testing;200% text zoom remains usable.
- Theme-editor reorder/add/remove/reload works without duplicated handlers or lost content.

## Evidence and regression procedure

For each viewport, record screenshot, DOM viewport/document width, selected media dimensions and visible section order. Compare source board's desktop/mobile region at matching scale. Measure curve endpoint/centre positions and calculate dip/width. For category corrections, check adjacent hero/header and all four descriptions again.

Run official Theme Check and relevant current schema validation on generated code. Fix genuine errors, then browser-check actual data because lint does not catch empty collections or stale cart UI. Performance screenshots/reports must state environment and date. Do not repeat tests after passing unless new changes or unresolved risks justify it.

Package verification in verification/REPORT.md validates this handoff's files/links/copies, not a future Shopify build. Never cite package checks as proof that storefront checkout or video playback works.
