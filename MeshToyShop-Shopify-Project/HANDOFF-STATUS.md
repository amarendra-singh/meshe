# Handoff status — read before implementation

**The design documentation is available. The production media and store setup are not all complete.** Do not confuse a complete file inventory with a launch-ready Shopify store.

## What is present

| Item | Present in this folder |
|---|---|
| Final reference boards | 8 original combined desktop/mobile boards, unchanged |
| Original/reference assets | 34 image/vector files, including those 8 boards |
| Browser evidence | 4 screenshots, separately labelled as documentation QA |
| Technical specification | 14 chapters, plus AGENTS and the AI implementation brief |
| Responsive wireframes | Desktop, tablet, mobile and small-mobile controls |
| Exact visible copy | Markdown registry and structured content JSON |
| Homepage action contracts | 44 links, controls, product actions and inherited form/navigation behaviours |
| Asset mapping | Every board, product image and initial asset slot mapped to an existing file |
| Production readiness | 33 explicit entries: 25 initial image/media/logo slots plus 8 implementation-input groups |
| Historical theme source | Unchanged partial reference files; explicitly not a deployable complete theme |
| Transfer format | Ordinary folder; no ZIP |

## What is not supplied as a final standalone asset

Of the 25 initial asset slots, 7 have standalone catalog-reference images and 18 lack a confirmed standalone production file:

- Hero scene:1 slot covering desktop/mobile art direction.
- Exact selected category cutouts:4 slots.
- Shared-play and creative overhead scenes:2 slots.
- Three real video/poster pairs:3 slots. Still posters inside a board are not video clips.
- Growth activity scenes:4 slots.
- Genuine customer WhatsApp messages:3 slots.
- Confirmed final wordmark master:1 slot. A legacy SVG exists, but it is not verified as the selected final master.

The scenes remain visible inside their original mockup boards. Nothing was silently regenerated, substituted or labelled as a genuine customer image. Clean image masters, actual footage and customer permission cannot be recovered merely by copying a flattened mockup.

Font binaries are absent. Outfit/DM Sans remain matching candidates, not confirmed bundled fonts. UI icons need compatible existing vectors or code-native construction matching the reference. Production use of supplier images still needs rights/SKU verification.

## Product image resolution

| Available reference | Pixels | Implication |
|---|---:|---|
| Colour Coder |500×500| Reference available; avoid pretending it is a high-resolution lifestyle master |
| Magnetic Drawing Board |500×500| Verify sharpness at rendered size/device pixel ratio |
| DIY Screw Drill Puzzle |1000×922| Preserve complete product and original proportions |
|3D Maze Cube |1254×1254| Original source available |
| Sticker book |500×327| Low-resolution landscape source; not a full scene/video |
| Mosaic board |333×500| Particularly limited width; request better source for large use |
| Magnetic tiles |500×500| Supplier layout includes labels; not a clean activity photograph |

## Store facts the next AI must resolve

Current product/variant/collection IDs, actual prices and stock, support destination, footer paragraph/menu readback, final operating-policy answers, media permissions and correct 15% prepaid/COD enforcement. All are tracked in [readiness-register.json](data/readiness-register.json). The layout can be built while these are resolved; public release cannot rely on invented values.

## Start points

- [AI implementation brief](AI-IMPLEMENTATION-BRIEF.md) and [AGENTS rules](AGENTS.md).
- [Final mockups](FINAL-MOCKUPS.html), [technical handbook](TECHNICAL-HANDBOOK.html), [wireframes](wireframes/index.html), [asset library](ASSET-LIBRARY.html).
- [Receiving-AI audit](docs/14-receiving-ai-audit.md), [package checks](verification/REPORT.md), [deep audit results](verification/deep-audit.json).
- [Asset inventory](data/asset-manifest.csv), [asset slots](data/asset-slots.json), [routes/actions](data/routes-and-actions.json).

The automated checks distinguish portable-file integrity from production readiness. No genuine review, real video playback, live checkout or deployed theme was created by the handoff audit.
