# 10 — Performance, accessibility, SEO and measurement

## Performance budget — targets, not results

Follow current [Shopify theme performance guidance](https://shopify.dev/docs/storefronts/themes/best-practices/performance): minimise JavaScript, avoid unnecessary libraries, load noncritical assets later and use responsive media. Build on native functionality instead of adding a slider/page-builder library for a few tracks.

Project targets: LCP≤2.5 s, INP≤200 ms and CLS≤0.1 at the 75 th percentile when sufficient real-user data exists. Lab checks are diagnostics, not proof of field performance or sales uplift. Suggested initial transfer budget for incremental homepage JS≤35KBcompressed, mobile hero candidate≤250KBwhere quality permits, below-fold poster≤100KB. These are tunable engineering budgets, not observed current file sizes. Don't compromise product legibility to hit arbitrary bytes.

Only above-fold/LCP image loads eagerly with suitable priority. Below-fold images lazy-load; reserve intrinsic dimensions. Use Shopify [image_url/image_tag](https://shopify.dev/docs/api/liquid/filters/image_tag), responsive candidates and accurate sizes. Avoid downloading both desktop/mobile masters. No full mockup PNG is embedded as the website. Video media bytes should not load until interaction; Shopify-hosted [video_tag](https://shopify.dev/docs/api/liquid/filters/video_tag) supports native video output. Inspect actual network waterfall, not attribute presence alone.

Keep font families/weights limited, use font-display swap or equivalent supported behaviour, verify fallback metrics to reduce shifts. No synchronous third-party requests solely for decoration. Scope event handlers, clean up editor listeners and avoid layout thrashing. Test slow network, CPU throttling and media failures.

## Accessibility

Use [Shopify accessibility guidance](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility). One H1 in hero; H2 per major section; card titles at appropriate lower level. Do not bake UI text into images. Maintain descriptive links, labelled icon buttons, focus visibility and logical keyboard order.

Validate text contrast against actual rendered surfaces, including hover/focus/error/disabled states. White on confirmed cobalt is approximately 6.3:1; navy on cream approximately 13.8:1. Tangerine on cream is not suitable for small text. Minimum 44CSS pxinteraction target is the project standard; do not shrink actual hit areas to match tiny exported mockup controls.

Test keyboard-only navigation,200% text zoom, reduced motion, screen-reader announcements for cart updates, error association, modal focus restoration and meaningful alt text. Avoid duplicate content announced from separate mobile/desktop markup. Screenshot text needs an accessible equivalent or a meaningful summary that preserves the actual approved message; don't invent a quote to fill it. Spoken videos need captions. Essential information cannot rely on colour or hover alone.

## SEO and structured content

Preserve native canonical/meta/title handling and valid semantic page structure. Use product data on real PDPs; do not add fake AggregateRating/Review structured data from placeholders. No homepage medical/developmental keyword stuffing. Image alt text describes the scene/product accurately. Collection links must lead to actual relevant products. Do not leak development labels into production page title/metadata.

## Analytics proposal

Use the existing consent-aware analytics/pixel setup after inspecting it; do not inject duplicate providers. Native purchase/cart events remain the system of record. Proposed custom event names below are project conventions, not claims that Shopify emits them automatically.

| Event | Trigger | Useful nonpersonal parameters |
|---|---|---|
| mesh_section_view | Section≥50% visible once/session or another documented rule | section_id, viewport_bucket |
| mesh_product_click | Product destination selected | section_id, product_id, position |
| mesh_video_start | Playback actually starts | product_id, video_id |
| mesh_video_complete | Actual ended event | product_id, video_id |
| mesh_faq_open | Question changes to open | question_id, group |
| mesh_story_product_click | Genuine story's product link selected | story_id, product_id |

Avoid chat text, names, phone numbers, email or unconsented personal data in events. Deduplicate event listeners after theme-editor/cart updates. For experiments, measure completed purchase/revenue per session and contribution, not only clicks; keep traffic mix and position comparable. No claimed uplift, AOV lift or superiority without measured evidence.
