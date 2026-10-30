# 07 — Shopify architecture and editor contract

## Recommended implementation surface

Use the existing Dawn-based Online Store 2.0 theme with native Liquid sections and Shopify product data. This is a design-handoff recommendation grounded in the existing project, not a proposal to migrate to headless, install a page builder or replace checkout. Shopify [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) provide reusable merchant-editable modules; [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) organise their settings and order.

Current state must be read again before coding. Historical evidence says Dawn was active by 25 October, theme 198870106278, with 17 published products and password protection. Earlier 23 October notes saying Horizon current/Dawn draft are stale. This package performed no live readback or theme deployment.

## File responsibility map — proposed names, not generated code

| File / area | Responsibility |
|---|---|
| Existing announcement/header/footer groups | Preserve native structure; implement selected branding/menu treatment |
| sections/mesh-hero.liquid | One H1; responsive hero image/copy and shallow mobile transition |
| sections/mesh-category-links.liquid | Four horizontal collection cards |
| sections/mesh-learning-discovery.liquid | Four editorial product cards, activity tags and View toy |
| sections/mesh-shared-play.liquid | Photo, editorial copy, ordered steps, product link |
| sections/mesh-creative-play.liquid | One shared image, two commerce rows |
| sections/mesh-shoppable-video.liquid | Product-linked video blocks and responsive track |
| sections/mesh-play-growth.liquid | Four activity modules and collection CTA |
| sections/mesh-customer-stories.liquid | Genuine screenshot blocks with optional related product |
| sections/mesh-buying-help.liquid | Two FAQ groups, ten questions, contact strip |
| snippets/mesh-purchase-control.liquid | Reuse native product form/variant/error behaviour consistently |
| snippets/mesh-media-poster.liquid | Responsive poster, accessible play control |
| assets/mesh-theme.css or scoped component styles | Tokens and component-specific rules without breaking Dawn globals |
| Scoped component JS | Carousel, video, optional cart integration; no global reinitialisation leaks |
| templates/index.json | Section order and resource settings after mapping real IDs |
| locales | Merge new UI state labels into existing dictionaries; don't replace files |

Names may adapt to current source to avoid duplication. The existing mesh-reference-home.liquid bundles an older hero/category/new-arrivals design. Inspect and refactor only where needed; don't keep its old product shelf in addition to the selected discovery section. The existing mesh-category-shelves.liquid is not an instruction to restore rejected RC content.

## Theme editor settings

Use resource pickers for products/collections/images/videos, plain or rich text where appropriate, and constrained settings. Merchant-editable does not mean dozens of unrelated style switches. Preserve fixed approved layout defaults.

| Section | Settings | Blocks / limits | Empty handling |
|---|---|---|---|
| Hero | Heading, emphasis phrase, support text, desktop/mobile image, focal positions,2CTA labels/destinations | None | Explicit editor image placeholder; don't substitute random product |
| Categories | Spacing/container |4 category blocks: title, description, collection, image, surface | Editor warns missing destination; don't ship dead links |
| Discovery | Heading, subline, collection CTA |4 product blocks: product, short title, activity, description, image override, tint | Missing product flagged in editor; no arbitrary newest-first fallback |
| Shared | Eyebrow, heading, subtext, desktop/mobile photo, product, CTA |3 ordered text steps | Missing product CTA disabled only in development; resolve before release |
| Creative | Heading/subtext, desktop/mobile scene, collection CTA |2 product blocks: product, short title, description, thumbnail | Public purchase action only for actual available variant |
| Videos | Heading/subline, preview mode |3 initial blocks; optional future expansion: video, poster, product, caption | No fake play control; hide unfilled public block |
| Growth | Heading/subline, CTA collection |4 blocks: title, body, image, label, icon | Preserve 4 in preview; complete approved imagery for release |
| Stories | Heading/subline, preview mode |3 initial blocks: screenshot, alt, optional product, permission status | Public output only for verified real entries |
| FAQ | Heading/subline, contact text/route |10 blocks: question, answer, group, initially_open | Non-empty approved answers required for public questions |
| Footer | Existing native menus/brand/signup/policies | Preserve | No guessed links or merchant details |

Block wrappers must support Shopify editor selection; handle editor load/unload/select events where scripts need reinitialisation. Unique element IDs use section/block identity. Remove listeners/observers and pause video on unload. Check duplicate instances do not interfere.

## Data boundaries

Content settings hold editorial labels/copy; Shopify product objects own title source, URL, selected variants, price, compare-at price, media and inventory state. Reference prices in screenshots are not hardcoded storefront truth. Use current currency formatting. Product handles/IDs in manifests are nullable until verified.

No new app/metafield system is required just to store this small homepage set. Native blocks suffice for screenshot/video curation. If the merchant later needs reusable multi-page records, design that data model separately against current Shopify docs; do not add abstractions pre-emptively.

## Existing source safeguards

implementation-reference contains an unchanged snapshot of historical partial source, not a valid complete theme. It lacks required base layouts/settings/templates. The original theme-work/locales/en.default.json was an empty lint fixture and is deliberately excluded from reusable locale files. Never upload that fixture or push the partial directory as a theme.

Read the complete current checkout before choosing cart integration. Retain base content_for_header/content_for_layout and native assets. Do not remove established translations, tracking consent integration, apps or working cart code as part of a visual refactor.

No new Liquid code is delivered in this package. Future code must pass Theme Check and appropriate schema validation plus browser checks; historical lint success does not validate future changes.
