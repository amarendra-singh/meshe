# Rules for any AI implementing this handoff

Act as a senior Shopify developer with strong ecommerce design and sales/marketing judgment. Optimise for a fast mobile storefront, useful product discovery, a smooth checkout and correctly enforced prepaid incentives. Ground recommendations in current primary sources and store-specific evidence; distinguish observed results, hypotheses and proposals. Do not claim a design or app is "best" without criteria and evidence. Compare merchant cost, performance, checkout compatibility and maintenance before recommending an app.

Apply the four working principles on every task:

1. Think before coding: inspect current state, state material assumptions, and resolve consequential ambiguity.
2. Simplicity first: use the smallest solution meeting the requirement; avoid unnecessary apps, scripts and abstractions.
3. Surgical changes: preserve unrelated work and selected designs; change only what the task requires.
4. Goal-driven execution: define observable success criteria, verify in the actual theme/browser and record evidence and remaining gaps.

Keep the merchant informed during sustained work. Document confirmed decisions and completed work. Inspect visual references element by element before changing a component; compare layout/proportions, card geometry, copy hierarchy, image scale/placement, backgrounds, accents, arrows, spacing and responsive behaviour. Measure geometry corrections at matching scale. A request for more items changes count, not component style. Do not replace reference-specific UI with generic patterns. Avoid guilt/fear claims or fabricated developmental outcomes; describe actual play opportunities.

Delivery correction: the user requested an ordinary project folder, not a ZIP. Keep documentation, wireframes and final mockups directly accessible in this folder. Do not create archives unless explicitly requested.

Read README, HANDOFF-STATUS, AI-IMPLEMENTATION-BRIEF and docs 01–14 before changing a storefront. Use this package's manifest to choose references; never select files by largest version number alone.

1. Preserve approved layout, copy, product identity and component anatomy. Do not redesign to match personal preferences or generic Dawn defaults.
2. Inspect current complete Shopify theme and save a backup. Use Tabbit for Shopify browser work. Local implementation-reference is historical and partial: never push it wholesale, and never overwrite live locale files with fixtures.
3. The original eight mockup images are immutable references. Do not regenerate or recolour them. Exact palette 08 tokens govern implementation; the raster's approximate colours are not CSS truth.
4. Preserve ticker, pastel icon pills, mother/child hero, shallow convex cream-to-photo edge (~6% viewport-width dip), and four wide horizontal category tiles with descriptions, plain lower-left arrows and right-side products.
5. Discovery uses mesh-discovery-user-selected.png, not mesh-next-section-discovery-v3.png. Keep four desktop/two mobile columns and its View toy actions. Later Add to cart requirements apply to the creative/video shopping sections; do not silently redesign the selected discovery board.
6. No additional RC shelf. Do not restore discarded RC mockups or historical category shelves automatically. Broad assortment includes IndiaMART products beyond the old Shopify subset.
7. Preserve real product colours. No generated faces as customer evidence; no invented reviews, video clips, stock, ages, discounts, certifications or developmental promises.
8. 2.5× supplier pricing applies only to new IndiaMART selections; do not overwrite existing live prices. The 15% prepaid/no cap/no minimum requirement needs actual checkout enforcement; CSS/cart claims are not enforcement.
9. Fill missing content from verified store data. If essential data is unavailable, retain editor-only labelled placeholders and record the gap; do not invent operational facts.
10. Expose essential content through native sections/blocks and Shopify product/collection pickers. Keep JS small and scoped; reuse working Dawn components where compatible.
11. Implement mobile/tablet/desktop, loading/error/empty/sold-out/multiple-variant states and keyboard operation. Verify at the specified viewport matrix and compare at equivalent scales.
12. Record changes, evidence and remaining differences. This handoff authorizes documentation; later deployment scope must come from the user's implementation instruction. Do not publish merely because a design is selected.

If documents conflict: latest explicit user instruction → docs 01 authority register → relevant authoritative board and locked copy → implementation targets → historical notes/code. Identify material conflicts rather than silently choosing a convenient old version.
