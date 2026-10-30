# Mesh Toy Shop — Shopify build handoff

Direct folder views: [Final mockups](FINAL-MOCKUPS.html) · [Full technical details](TECHNICAL-HANDBOOK.html) · [Desktop/tablet/mobile wireframes](wireframes/index.html) · [Asset library](ASSET-LIBRARY.html).

Deliver this project as a normal folder. No ZIP/archive unless explicitly requested.

Version 1.1 · receiving-AI audit · 30 October 2026 · India / INR

**Read [HANDOFF-STATUS.md](HANDOFF-STATUS.md) first:** it lists exactly what is present, which 18 initial asset slots lack a confirmed standalone production file, and which store inputs remain unresolved.

**Start here.** This package freezes the homepage design discussed with the merchant. The latest instruction — “home page is done” — is treated as acceptance of the assembled design direction for documentation. It is not evidence that a new theme has been implemented, that operational claims are confirmed, or that every generated asset is production-ready.

Open [START-HERE.html](START-HERE.html) for the visual reference gallery and links. Open [responsive wireframes](wireframes/index.html) for annotated desktop, tablet and mobile structure. These are implementation diagrams, not replacement mockups.

## Read in this order

1. [AI implementation brief](AI-IMPLEMENTATION-BRIEF.md) and [local rules](AGENTS.md).
2. [Design authority and approval register](docs/01-design-authority.md).
3. [Page structure and wireframes](docs/02-page-structure.md).
4. [Design system and responsive rules](docs/03-design-system-responsive.md).
5. [Section-by-section specification](docs/04-section-specifications.md).
6. [Exact content and destination registry](docs/05-content-and-destinations.md).
7. [Asset inventory and gaps](docs/06-assets-and-production.md).
8. [Shopify architecture and editor settings](docs/07-shopify-architecture.md).
9. [Cart, video and interactive states](docs/08-interactions-and-cart.md).
10. [Catalog, payments and policy dependencies](docs/09-commerce-and-launch-dependencies.md).
11. [Performance, accessibility and analytics](docs/10-quality-requirements.md).
12. [Build sequence and acceptance checklist](docs/11-build-and-acceptance.md).
13. [Mistakes not to repeat](docs/12-do-not-repeat.md).
14. [Source evidence and remaining decisions](docs/13-evidence-and-decisions.md).
15. [Receiving-AI audit and coverage](docs/14-receiving-ai-audit.md).
16. [Package verification](verification/REPORT.md) and [deep audit](verification/deep-audit.json).

## Contents

- `assets/mockups/`: eight authoritative combined desktop/mobile section boards, copied without edits.
- `assets/references/`: supporting geometry, menu and colour references; not alternative homepage designs.
- `assets/product-source/`: original available catalog references; not generated packshot replacements.
- `assets/legacy-reference/`: older artwork/brand files where available; explicitly not substitutes for the selected designs.
- `data/`: machine-readable design, content, product and asset manifests.
- `wireframes/`: responsive structural diagrams and readable equivalent.
- `implementation-reference/`: historical partial Dawn files for inspection only, not an upload-ready theme.
- `source-notes/`: historical notes in plain-text snapshot form. New handoff documents take precedence over their outdated statuses.
- `verification/`: file checksums, copy verification, link checks and browser evidence.
- `tools/`: reproducible package validation; no store credentials or API secrets required.

## What is preserved

The V11 shallow mobile hero curve, top ticker, pastel menu pills, four horizontal category tiles, exact selected discovery first render, shared-play section, creative shopping section, latest video/growth/WhatsApp/FAQ boards, and palette 08. Mockup images are not regenerated, cropped, retouched or recoloured. SHA-256 comparisons establish that packaged reference files are byte-identical to their sources.

## Important boundaries

This is a build handoff, not a deployable Shopify theme. Typography identity, tablet breakpoints and some spacing are implementation targets because generated boards do not encode CSS. The complete page order is an explicit assembly decision rather than an invented claim that a full-page composite was approved. Footer is inherited from the existing store; no new footer mockup was supplied.

All available referenced image files are included. Some family scenes, category cutouts and video posters only exist inside flattened mockup boards. They have asset slots and references, not falsely labelled standalone exports. Real videos and genuine customer WhatsApp screenshots have not been supplied. See the asset-gap register before treating the package as launch-ready.

No live Shopify configuration, existing source mockup or product price was changed while preparing this handoff.
