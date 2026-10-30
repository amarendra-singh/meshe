# Next section: product discovery — 29 October 2026

Status: merchant selected the attached first-render visual direction on 29 October 2026. Exact selected reference: [merchant-selected discovery image](../output/design-concepts/mesh-discovery-user-selected.png). This selection takes precedence over v3 below; do not silently substitute the later refinement. No deployment authorized or performed by this selection.

Artifact: [desktop/mobile discovery mockup](../output/design-concepts/mesh-next-section-discovery-v3.png). Built-in imagegen with real catalog image references; original [prompt](../output/design-concepts/next-section-prompt-v1.txt).

## Corrected catalog scope

The 17 active Shopify listings are the currently imported subset, not the full Mesh range. The merchant supplied https://www.meshenterprise.in/ during this task. Its educational category displays 16 listings, with colour sorting, a wooden Colour Coder, magnetic drawing boards, construction sets and other activities. These public listing counts are not unique SKU counts or stock verification. The site also includes non-toy categories; do not import its entire taxonomy into Mesh Toy Shop automatically.

The educational page uses quote prices and minimum quantities (for example Colour Coder: 40 pieces; magnetic drawing board: 50). These are not approved Shopify retail prices. Its age information can conflict between tables and descriptions. Do not carry age, safety or developmental claims into the mockup without verification.

Sources: https://www.meshenterprise.in/learning-and-educational-toy.html ; https://www.meshenterprise.in/puzzle-game.html ; https://www.meshenterprise.in/kids-remote-control-car.html . Shopify catalog tools independently verified 17 active products and their prices today.

## Reference inventory and scope

Inspected mesh-mobile-shallow-curve-v11.png. Preserve the hero, ticker, pastel menu pills, mother/child photo, four horizontal category cards and approximately 6% mobile curve dip. This artifact depicts only the next section; these existing elements are outside its viewport and are not regenerated.

Carry forward cobalt primary actions, warm cream surfaces, navy headings, slate supporting type, gentle peach/yellow/mint/ice-blue image surfaces and restrained orange accents. Use Outfit-like headings and DM Sans-like body. Exact fonts need code implementation.

New product-card geometry is a proposal, distinct from the existing horizontal category cards: desktop four equal vertical cards, mobile two columns/two rows; square photo areas, approximately 14px corners; consistent title/description slots, aligned actions; no hidden carousel items. Desktop target about 220px/card with 18px gutters, mobile about 180px/card with 12px gutters. Page heading is smaller than the hero. Straight section boundaries, no additional curves.

## Proposed content

Headline: Little hands. Big discoveries.
Subline: Match a pattern. Make a shape. Try a new way.
Link: Explore learning toys.

| Activity | Display title | Description | Source |
|---|---|---|---|
| Match | Colour Coder | Slide colours to match a pattern. | Mesh Enterprise Kids Learning Toys listing; wooden board photo |
| Draw | Magnetic Drawing Board | Lift beads with the magnetic pen. | Mesh Enterprise Baby Toy Magnetic Drawing Board listing; pineapple photo |
| Build | DIY Screw Drill Puzzle | Build pictures with shapes and screws. | Shopify DIY Screw Drill Puzzle Toy; turquoise case photo |
| Solve | 3D Maze Cube | Guide the ball through the maze. | Shopify 3D Maze Cube; olive/yellow/white cube photo |

All cards link to a product with View toy. Display titles are proposed concise merchandising labels, not catalog edits. Source product photography was inspected before generation. AI rendering remains a concept approximation; production must use original verified product photos.

Retail prices intentionally omitted from this discovery proposal because two added products have no confirmed retail price or published Shopify product. This sacrifices immediate budget comparison; final purchasable product cards should show confirmed live retail prices and actual availability. No wishlist, ratings, discount, urgency, age, bestseller or cognitive-outcome claims. No cart action before the new products exist in Shopify.

## Why this proposal fits and how to judge it

The hero establishes emotion, category cards establish routes, and this section connects curiosity to four concrete activities and products. It offers a clearer activity comparison than a row of ambiguous product names. It is not proven to outperform competitors or the current store.

Compared with the existing newest-first all-RC shelf, this editorial selection makes the educational range visible. Compared with immediately adding another family banner, it gives an interested parent product destinations sooner. Compared with repeating another category grid, it exposes actual products. Risk: shoppers focused on RC may prefer the RC shelf; product mix and position require testing.

Smartivity currently exposes age filters, product prices and age labels in its bestseller shelf (https://www.smartivity.in/). Its useful pattern is decision support; Mesh needs its own verified age data before matching that feature. There is no evidence that this proposal is universally better than Smartivity.

Review loop: initially considered four mixed Shopify products with current prices. Merchant supplied the wider catalog, invalidating the assumption that 17 represented the full range. Revised to a focused educational discovery selection with two additional real listings; removed unconfirmed retail prices. Replaced developmental benefit labels with observable play actions.

Validate later using section exposure-to-product-click rate, add-to-cart per exposed session and completed purchases per exposed session, split by mobile/desktop. Compare the same positions and traffic mix, ideally randomized. More clicks alone is not success; monitor purchase conversion, revenue per session, speed and returns. No uplift or AOV forecast is justified from a mockup.

## Visual review and remaining differences

Three renders were inspected. Final includes all four products with complete titles/descriptions/actions, four desktop columns and two mobile columns, no prices or fabricated proof, cream/pastel/blue styling. The existing hero was not included or altered. Labels were darkened; desktop headline and photo panels were reduced. Approximate final desktop photo panel is 250 by 295px (1:1.18), compared with initial about 255 by 325px (1:1.27); square target was not achieved exactly. Magnetic Drawing Board's extra title line still shifts its description baseline. Mobile buttons are about40px tall in the rendering; implementation target remains at least44px. These are explicit remaining geometry refinements, not verified implementation details. Product typography and package markings are AI approximations, so use original media in production.

Refinement prompt summary: reduce desktop heading width, shorten desktop photo zones, align all card text slots and buttons, darken activity labels, retain mobile2x2 structure and all product content. Last pass confined geometry changes to desktop. Exact raster geometry was only partially followed by the generator; no claim of pixel-exact correspondence.
