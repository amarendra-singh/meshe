# 06 — Assets, provenance and production gaps

Every included image is under assets/. [asset-manifest.json](../data/asset-manifest.json) records original location, package path, SHA-256, byte size, dimensions, role and readiness. [asset-slots.json](../data/asset-slots.json) maps each image need to the available source or a specific missing standalone asset. [asset-manifest.csv](../data/asset-manifest.csv) is the spreadsheet-readable inventory.

## Four distinct asset classes

1. **Authoritative mockups:** eight complete boards. Immutable visual references; never use them as full-page storefront backgrounds or clickable image maps.
2. **Supporting reference images:** colour board, corrected category anatomy, older shallow curve, supplied header/menu crop and original attached detail images where accessible. Their filename/manifest states which detail they support. Never apply their obsolete parts.
3. **Catalog source images:** original available product files. These are the closest evidence for exact toy identity, but may be low-resolution, collaged or contain supplier text. Their presence does not establish reproduction rights, safety certification, current stock or final product specs.
4. **Legacy references:** older logo/category/campaign files, isolated and explicitly non-authoritative. They are included to prevent a builder from mistaking a convenient existing file for the selected design.

## Available versus embedded-only

| Required media | Available separately? | Required action |
|---|---|---|
| M01 hero mother/boy/RC scene | No clean selected export | Obtain clean approved master or shoot; preserve composition and safe zones |
| Four exact M01 category cutouts | No | Obtain selected masters; do not substitute older robot/stacker art |
| Discovery four products | Yes, catalog references | Verify resolution/rights; use source originals and contained fitting |
| M03 mother/daughter Colour Coder scene | No clean selected export | Real shoot or approved clean master, preserving scene/layout |
| M04 creative overhead scene | No clean selected export | Photograph both actual products with matching composition |
| Creative purchase thumbnails | Yes, sticker-book/tiger-board source images | Confirm exact SKU and composition |
| M05 three poster scenes | Embedded only | Use frames from genuine matching videos |
| M05 actual videos | No | Film/upload; never animate still mockups as fake demos |
| M06 four activity photos | Embedded only | Capture actual play photos with consent and accurate product mechanics |
| M07 WhatsApp screenshots | No | Genuine messages, publish permission, redact personal details |
| Wordmark master/font files | Legacy SVG only, not verified against M01 | Confirm final master; do not silently replace the selected wordmark |
| Footer assets | Existing store inheritance | Read current theme settings before reuse |

All embedded scenes remain visible in the original boards. They have not been cropped, retouched or regenerated to create apparently genuine assets. Transparent silhouettes or masked photo exports require a separate asset-production step; a background-bearing JPEG is not a transparent cutout.

## Image preparation contract

- Preserve originals; export derivatives under a new production subfolder with provenance and approval recorded.
- Product image target: sufficiently large for its maximum rendered dimension and device pixel ratio; don't upscale a 500 px supplier image and claim new detail. Source inventory exposes actual dimensions.
- Hero desktop target clean 2400 px-wide master; mobile 1200 px-wide art-directed master if needed. These are acquisition targets, not files currently supplied.
- Video source target 1080×1920 portrait, stable light, no baked price/promo text. Selected visual display may crop to M05 ratio≈0.63; keep action central. Short useful demonstrations, duration based on actual footage rather than fabricated labels.
- Serve responsive candidates through Shopify CDN, set width/height to reserve space, provide accurate sizes, and lazy-load below-fold media. Do not load desktop and mobile images simultaneously when only one is visible.
- Meaningful alt text describes product/activity; decoration uses empty alt. Avoid claiming that a generated family is a customer.
- Real screenshot original remains intact except privacy redaction; enlargement must retain meaning. Do not transcribe/forge chat bubbles to simulate social proof.

## Photography brief

Natural window light, ordinary home setting, varied relaxed expressions, believable hands and actual child/toy scale. Avoid waxy skin, uniformly perfect smiles, dramatic golden glow and impossible product mechanics. Adult/guardian permission for identifiable children; source records for all published media. Photograph the actual Colour Coder 4×4 tokens and sliding action, the sticker book being used as sold, and the tiger-board stylus/parts accurately. Loose decorative props are not promised inclusions.

## Preview versus release

Layout implementation can proceed with explicit development placeholders. Production release depends on real media and verified rights. No synthetic review or nonfunctional video should silently be shown as genuine. Asset gaps do not authorize redesigning the selected layout.
