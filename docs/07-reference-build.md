# Desktop reference implementation

Updated: 24 October 2026, Asia/Kolkata.

**Latest status:** [Section audit](08-section-audit.md) records the later saved implementation, repaired product images and nine-image reload assertion. The saved/pending columns and8:30AM blocker below describe the earlier build stage; the current review limit is3:27PM.

## Design authority

The user's attached 848 × 1855 image is the current desktop reference: `output/design-concepts/approved-desktop-reference.png`. It supersedes the earlier four-column desktop concept and compact mobile-v3 recommendation. Keep two category columns and two product columns on desktop. The earlier Kobbo audit supplies context, not permission to replace this selected layout.

## Section comparison and execution plan

Measurements below are approximate reference-image pixels at width 848. They are targets, not verified browser measurements. Scale appropriately at wider desktop widths, then verify at both 848 and 1440 CSS pixels.

| Section | Reference target | Saved Shopify draft | Local refinement / next verification |
|---|---|---|---|
| Announcement | Cobalt field, white centered message, about 51px high; trailing arrow | Correct message, cream background and small text in last screenshot | Set native announcement color scheme, height/type and collection destination; preserve keyboard-accessible link |
| Header | Cream, about 97px high; stacked Mesh wordmark at left; navy search/cart at right | Wordmark SVG uploaded; width 180 set and Save clicked after last screenshot | Confirm upload survived reload; adjust visible logo to reference scale; simplify desktop navigation and account icon; retain working search/cart |
| Hero | y148–738, height ~590px; left copy; warm scene with toys along bottom | Custom Liquid section and generated hero saved; visual capture confirms composition | Local hero height 69.6vw capped at 820px; explicit eyebrow line-height removes inherited excess spacing; compare crop and text position |
| Hero type/action | x47; eyebrow ~18px; heading ~60px over two lines; description ~28px; blue CTA ~275 × 70px | Copy and action saved, readable in screenshot | Refined text widths and line-height; button URL editable; verify exact wrapping and button dimensions |
| Category heading | x40, y770; about 42px | Correct text and navy styling saved | Local 4.95vw heading scale; check alignment |
| Category tiles | x33 and x432; width~384; height146; gap16; pastel blue/yellow/peach/green | Four images assigned; two-column CSS saved; first row seen in capture | Changed 170px minimum to responsive height ~146px at848; collection resource picker added with image/title overrides |
| Product heading | x40, y1185; about42px | Correct title saved | Verify position after category height correction |
| Product cards | x35 and x432; image~380 × 219; 16px radii; names/prices below; two rows | Four actual catalogue photos assigned to editor-only draft cards | Responsive image candidates, variant price range, availability, missing-image fallback; select real products after catalogue activation is approved |
| Footer | Outside the supplied crop | Existing Dawn footer retained | Do not claim unseen reference requirements; review legitimate support links separately |

The generated toy scene is decorative. Real listing photographs intentionally differ from the illustrated reference products. No performance or conversion superiority has been measured.

## Saved versus pending files

- Saved custom section snapshot: `docs/evidence/mesh-reference-home.saved-2026-10-24.liquid`.
- Current local revision, **not uploaded**: `theme-work/sections/mesh-reference-home.liquid`.
- Saved hero: `output/design-concepts/mesh-reference-hero.png`.
- Uploaded wordmark: `output/design-concepts/mesh-wordmark.svg`.
- Existing banner, multicolumn and rich-text sections were hidden, preserving prior work.
- Product preview titles/prices/images are editor-only. Public output requires an available product selected in each block. The local revision suppresses the entire product heading/grid if no usable products exist.

## Dynamic implementation

The section uses Shopify Liquid resource settings; no additional JavaScript or app is required for this layout. Hero copy, image, CTA destination, headings, palette colors, collection tiles and product choices are editable. Selecting a product uses its current title, image, URL, price range and availability. Category collection selection supplies the destination, with merchant title/image overrides. Existing setting IDs are preserved so the saved images and copy survive the update.

Image delivery follows Shopify's [performance guidance](https://shopify.dev/docs/storefronts/themes/best-practices/performance): eager high-priority hero, lazy images below, responsive sizes and native image dimensions. Resource settings follow Shopify's [input settings documentation](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings); product state follows the [Liquid product object](https://shopify.dev/docs/api/liquid/objects/product).

## Verification evidence

- Saved screenshot inspected: `output/design-concepts/dawn-reference-progress-2026-10-24.png`. This precedes logo upload and local revision 2.
- Shopify CLI 4.9.4 Theme Check, executed using cached Node22: **2 files inspected with no offenses found**, exit0. This checks the section and an empty local locale fixture, not the entire remote Dawn theme.
- Bundled Shopify skill validator could not run: missing `@shopify/theme-check-common`. Official CLI Theme Check used as the fallback.
- No full-page screenshot comparison, mobile visual pass, live link/cart pass, or Lighthouse result for revision2 yet.

## Access blocker and resumption

Automatic approval review rejected the next Tabbit action because of a usage limit and reported retry at **8:30 AM**. The rejected action was read-only header markup inspection; it was not executed. Do not bypass via another browser/API. Task tabs remain open. Foreground activation was previously denied by the browser's preserve-focus policy; the user must select the Build Mesh Dawn draft group to see it.

When access resumes:

1. Inspect current logo/save status, then upload local revision2 through the existing code editor. Do not replace Dawn's real locale file with the empty validation fixture.
2. Finish announcement/header using current DOM and native controls. Preserve search/cart functionality.
3. Save/reload. Capture the whole homepage at848 and1440 CSS pixels plus390 mobile. Compare section bounds, typography, gaps, image crops and colors against the attached reference.
4. Check horizontal overflow, keyboard focus, collection destinations and search/cart. Resolve actual failures before adding features.
5. Catalogue activation, gateway setup and prepaid discount remain separate later steps. Do not publish the theme as part of this draft update.
