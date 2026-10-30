# Reviews on the development homepage — 27 October 2026

The user requested: “show me on home page, this is my own project and dev like production”. This explicitly authorizes showing the labeled design samples on the actual development homepage. It supersedes document 12's editor-only review visibility. The storefront remains password protected, observed in Shopify's storefront preview bar.

## Saved implementation

- Added a native section checkbox, **Show labeled demos on storefront**, default false, to `mesh-media-rail.liquid`.
- Enabled it only for **Mesh customer screenshots** in active Dawn theme 198870106278. All four blocks retain their demo flags and disclosures. Video posters remain editor-only.
- Visibility counting and rendering use the same condition, avoiding an empty section when samples are hidden.
- Uploaded only the changed section file; the local theme directory is partial and must not be pushed wholesale.
- Backed up the previous file in `output/backups/mesh-media-rail-before-home-demo-2026-10-27.liquid`.
- Verified the enabled setting persisted after reloading the theme editor. The first immediate storefront refresh was stale; a subsequent refresh displayed the saved section.

Homepage section: https://2zs0x1-0z.myshopify.com/#shopify-section-template--29809640046758__mesh_media_rail_aecRWK

## Verification

- Official Shopify CLI Theme Check: seven files inspected, no offenses. The bundled skill validator could not run because `@shopify/theme-check-common` is missing; the official CLI supplied validation instead.
- Actual desktop homepage: four loaded square screenshot cards, about 316px each, centered heading, cream background, visible demo disclosures. Document width 1394px inside a 1409px viewport including scrollbar; no horizontal overflow.
- Actual mobile homepage at 390px viewport: one approximately 327px card, red side arrows, no page overflow (375px document including layout scrollbar exclusion). Next moves the carousel; End disables Next at the end; Home returns to start and disables Previous.
- Desktop and mobile screenshots visually inspected and saved under `docs/evidence/homepage-reviews-2026-10-27/`. Orange mobile border is keyboard focus from testing.
- Reloaded actual homepage contains one review rail with four sample cards and no Liquid error text.

## Preserved scope

This is production theme code with native editable settings, not a separate static mockup. The samples remain fictional design assets. Genuine customer screenshots and real product videos are still needed before launch. Existing product/collection data connections, FAQ, footer and checkout settings were not changed in this pass. Product imagery and payment/prepaid incentive work remain deferred.
