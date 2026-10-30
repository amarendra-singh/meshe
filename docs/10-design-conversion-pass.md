# Design and conversion pass — 26 October 2026

## Working brief

Senior Shopify development and ecommerce marketing collaboration. Design first. Think before coding, keep the solution simple, make focused changes, verify observable outcomes. Keep content merchant-editable, product/collection data dynamic, image loading appropriate to viewport, and save progress continuously.

The intended page flow is clear offer → browse by play style → latest products → reason to make time for shared play → category showcases → genuine demonstrations/reviews → practical FAQ. Improved conversion is a hypothesis until measured with store traffic.

## Completed saves

- Four original category cutouts uploaded to Shopify Files and assigned with native image pickers: remote-control truck, friendly robot, wooden puzzle, ring stacker.
- All four persisted in storefront HTML after reload, with correct category destinations and loaded images.
- Updated mesh-reference-home.liquid: category label has separate text/arrow spans; desktop arrow stays beside label; mobile tiles place a larger illustration above a readable full-width label; category images keep their original colours instead of multiplying into the pastel background.
- Category images use lazy loading and Shopify sizes=auto so selection follows the actual rendered width. Primary documentation: https://shopify.dev/docs/storefronts/themes/best-practices/performance/implement-responsive-design
- Shopify AI Toolkit validator could not run (missing @shopify/theme-check-common). Official Shopify CLI Theme Check passed: 7 files, no offenses. Updated section uploaded through Shopify's native code-editor file upload.
- Moved Mesh screen-free story before Mesh category showcases using native drag controls; verified order and saved.

## In progress

- Refine the story copy to give a concrete reason and next step, using emotional relevance without invented stock scarcity, countdowns, testimonials, or medical/developmental claims.
- Verify final desktop/mobile visuals, image fit, headings, native editor ordering and all relevant links after reload.

## Plugin decision

User authorized required plugins. No extra page builder is required for this design pass: the existing Dawn sections support the work. Evaluate any later app against the specific feature, maintenance, cost and measured performance impact.


## Saved copy and verification

Story heading: **Make time for the moments you can’t replay.**

Introduction: A screen-free play break is a chance to try something, swap ideas and share a little win. Pick a puzzle or hands-on kit, put it on the table and join in.

CTA: **Find a hands-on favourite**, retaining the working all-products destination.

- Revised story copy persisted after a second storefront reload. Initial reload served the previous text while the save was settling; the later read confirmed the new heading.
- Desktop section order persisted: reference hero/categories/new arrivals → family story → category showcases → media rails → FAQ.
- Desktop category screenshot inspected: matching original artwork on pastel backgrounds, navy labels and aligned arrows; all four correct collection links retained.
- Mobile preview: 360px document and viewport width, no horizontal overflow or Liquid errors. Four tiles measured 160 × 180px; labels fit without horizontal clipping; all four images loaded with responsive 400px sources and sizes=auto.
- Evidence saved under docs/evidence/homepage-2026-10-26/.
- No artificial urgency badge, timer, stock claim, fabricated review or prepaid promotion was added.

## Remaining design work

The category artwork and story flow are completed. Product-card photography still uses real supplier images with mixed composition; improve source photography without changing product identity. Real product videos and permission-cleared customer screenshots remain needed before their rails can show genuine content to shoppers. Continue checking the lower-page rhythm and footer once those assets are supplied. No pixel-perfect equivalence, speed score or conversion uplift is claimed.

Final crosscheck: 15 dynamically rendered homepage product cards, five FAQ disclosures, no empty/hash-only main-content links; story image loaded, CTA targets /collections/all, no story overflow. Empty/demo video and review rails have zero public height. Final story screenshot saved as desktop-story.png.
