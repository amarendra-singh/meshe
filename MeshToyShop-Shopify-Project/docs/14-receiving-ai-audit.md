# 14 — Receiving-AI audit and completeness contract

This chapter is the final transfer check, not an additional design. The eight boards remain unchanged. Read HANDOFF-STATUS.md before claiming the package is production-ready.

## Instruction coverage

| Merchant requirement | Handoff location / evidence |
|---|---|
| Senior Shopify developer plus ecommerce/marketing judgment | AGENTS.md role, evidence and app-decision rules |
| Think first, simplicity, surgical changes, verify outcomes | AGENTS.md four working principles; docs11 acceptance stages |
| Blue primary, selected palette08 | data/design-tokens.json; docs03; palette reference |
| Retain ticker and pastel icon-pill menu | M01; docs04 S00–S01; exact copy in data/content.json |
| Mother/child scene and concise emotional/intellectual story | M01/M03/M06; docs04/05; no unsupported medical claims |
| Four horizontal category cards with full reference anatomy | M01; category anatomy reference; docs04 S03 |
| Shallow mobile hero curve, not exaggerated | V11; measured target and tolerance in docs03; diagram geometry checked separately |
| Exact user-selected learning-discovery mockup | M02; immutable source checksum and filename invariant |
| Do not repeat another RC shelf | Rejected-file register; docs12; no extra RC board in manifest |
| Broader IndiaMART assortment | Product map and catalog originals; docs09 |
| Add to cart on later shopping sections | M04/M05; docs08 state machine; routes-and-actions.json |
| New catalog retail =2.5×supplier quote | docs09; reference prices 450/250/625; existing live prices not overwritten |
| Realistic imagery, accurate toys | docs06 photo brief; source image dimensions and missing master list |
| More FAQs | M08; 10 questions, 2 groups, exact first visible answer; 5 operational answers pending |
| WhatsApp customer screenshots | M07; genuine evidence/permission rules; no actual messages supplied |
| Video section | M05; real media requirements, play/cart separation and loading behaviour |
| Detailed desktop/mobile/responsive wireframes | wireframes/index.html; docs02–04; tablet assumptions explicitly marked |
| Preserve final mockups | Eight original files, SHA-256 equality checks; no generated replacement |
| All available assets in an asset folder | assets/ plus exhaustive asset manifest; standalone gaps explicitly listed |
| AI can build without conversation context | AI-IMPLEMENTATION-BRIEF, AGENTS, docs01–14, machine manifests and receiving checklist |
| Folder delivery, no ZIP | README and AGENTS; unsolicited archive removed |

## Findings corrected in this audit

1. The portable AGENTS file did not fully repeat the senior role, evidence standards and four working principles from the parent workspace. These are now explicit inside the handed-over folder.
2. Earlier verification checked listed images but did not reject unlisted image files or cross-check every asset slot/product/mockup reference. Validation now checks both directions and the cross-references.
3. Link validation previously allowed links to files outside the package. Local links now must stay inside the handoff; external source citations remain permitted.
4. Destination requirements existed in prose, but the structured content aliases lacked a central action resolver. data/routes-and-actions.json now records every homepage action and required resource binding.
5. A seed assembly script could overwrite later data edits if rerun. It now refuses to reseed an existing frozen handoff.
6. FINAL-MOCKUPS.html was a separately written page. The viewer builder now regenerates it from the same authoritative eight-board manifest as the overview.
7. The wireframe's curve used the outer preview width as its percentage reference. It now measures against the hero's own width; named layout containers keep this fix from changing desktop/tablet rules. The original V11 image is untouched.
8. Browser QA scripts assumed the author's absolute workspace path. Portable entry points now derive URLs from the current local handoff page or accept a supplied base URL.
9. Asset readiness was spread across files. HANDOFF-STATUS.md and data/readiness-register.json now provide one receiving checklist with available, embedded-only, missing and unresolved items.

## What is complete, and what is not

**Design handoff:** original boards, reference/source files currently available, exact visible copy, section geometry, responsive rules, interaction states, code/data responsibilities and acceptance criteria are present.

**Production media:** not complete. Seven product reference images have standalone files, but some are only 333–500 px across or contain supplier layout text. Eighteen initial asset slots lack a confirmed standalone production-ready file. This count includes the unconfirmed final logo master; a legacy SVG exists but is not equivalent to an approved final logo. Font binaries are also absent and tracked separately. No actual video clip or genuine customer conversation was supplied.

**Store integration:** unresolved current product/variant/collection IDs, support identity, footer readback, confirmed operating policies and payment-method enforcement. These are implementation inputs, not permission to guess. Build independent layout while resolving them; do not publish fabricated placeholders as real commerce or proof.

## Receiving checklist

Audit evidence: all 38 packaged image/vector files decode; 59 visible-copy strings, 44 action contracts and 54 local HTML runtime resources checked. The folder also validates under a different directory name. Browser measurements cover eight widths from 320 to 1280 CSS px, including 749/750 and 989/990 boundaries. All 49 browser assertions passed, with no canvas overflow; the shallow curve measures 6.2% of its own hero width. Updated wireframe/mobile-handbook screenshots are documentation QA, not replacement mockups. See [browser measurements](../verification/receiving-ai-browser-checks.json) and [deep audit](../verification/deep-audit.json).

1. Open README, HANDOFF-STATUS and all eight boards. Read AGENTS and the brief before editing code.
2. Run `python tools/validate_package.py`. For deeper decoding and transfer checks, run `python tools/audit_handoff.py` with Pillow installed. The HTML files themselves need no Python/server/network to open.
3. Check that all local resource links remain inside this folder. Provenance paths may point to the old authoring workspace; they are records, not runtime dependencies.
4. Resolve only required production inputs from the actual store/merchant. Record the returned IDs, permission status and policies with dates. Do not overwrite an existing product's price because the mockup shows another value.
5. Use the original boards for visual checks; the wireframe is structural, not a redesigned storefront. Keep eight board hashes unchanged.
6. Follow docs11 for implementation and test evidence. Package audits do not validate a future Shopify deployment, checkout, real video playback or marketing campaign.

## UI icons and typography

No separate final icon/font package was supplied. Reuse compatible existing theme SVG controls or implement simple code-native icons to match the selected stroke/style; keep accessible labels. Brand wordmark matching needs a confirmed master. Do not use an emoji as a substitute for the selected car/puzzle/bulb menu icons, or fetch an unlicensed font because its name appears as a candidate. Existing Outfit/DM Sans guidance remains a visual-match proposal, not a bundled-font claim.

## Official route reference

The [Shopify routes object](https://shopify.dev/docs/api/liquid/objects/routes) provides locale-aware standard storefront destinations. The [Cart API](https://shopify.dev/docs/api/ajax/reference/cart) uses variant-based cart actions. These references support the resolver contract; actual store IDs and option rules still require readback.
