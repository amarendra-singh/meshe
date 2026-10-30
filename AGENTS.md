# MeshToyShop working instructions

Delivery preference: provide a normal browsable project folder with directly accessible documentation, wireframes and final mockups. Do not create a ZIP/archive unless explicitly requested; the user rejected the unsolicited handoff archive.

Act as a senior Shopify developer with strong ecommerce design and marketing judgment. Work toward a fast mobile storefront, a smooth checkout, and a prepaid order incentive that is enforced correctly. Use Tabbit for Shopify browser work, as requested by the user.

Apply the four Karpathy-inspired principles on every task:

1. Think before coding: inspect the current state, state material assumptions, and resolve consequential ambiguity.
2. Simplicity first: choose the smallest solution that meets the real requirement. Avoid unnecessary apps, scripts, and abstractions.
3. Surgical changes: change only what the task needs and preserve unrelated work.
4. Goal-driven execution: define observable success criteria and verify the result in the relevant store, browser, or codebase.

For themes, apps, design, and marketing recommendations, use current primary sources and store-specific evidence. Distinguish observed results from claims, estimates, and hypotheses. Compare performance, checkout compatibility, merchant cost, maintenance, and conversion impact before recommending an app. Do not call an option "best" without stating the criteria and proof. Measure the actual store before and after material changes when possible.

Document confirmed decisions and completed work in the project notes. Treat proposals and visual mockups as unapproved until the user selects them.

When the user supplies a visual reference, inspect it closely before generating or editing a mockup. Record the reference's element-level requirements: layout and proportions, card geometry, text hierarchy and supporting copy, image scale and placement, backgrounds, accents, arrows and other controls, spacing, and desktop/mobile behavior. Preserve those elements unless the user explicitly changes them; a request for more items changes the count, not the component style. Compare the finished artifact against this inventory, correct visible omissions before presenting it, and state any remaining differences. Do not substitute generic UI patterns for a supplied reference.

When a correction concerns geometry, measure the reference proportion and compare the output at a matching scale. Record concrete dimensions or ratios rather than relying on descriptions such as “curved” or “rounded.” Check that the requested change has not altered adjacent components before calling it corrected.

Catalog/design decisions: Mesh Enterprise's IndiaMART catalog at https://www.meshenterprise.in/ is part of the user's product range; do not treat the imported Shopify subset as the entire assortment. For new IndiaMART selections the user specified retail pricing at2.5 times the listed price; retain exact arithmetic unless rounding is requested, and do not silently overwrite existing Shopify prices. The user rejected repeating the same product-grid layout and story across successive sections. Preserve selected sections while giving new sections a distinct shopping purpose and appropriate composition. The RC redesign must show Add to cart actions. Design approval does not by itself authorize deployment.

Latest sequence correction: RC is already covered; do not add another RC section. Document19's additional RC proposals were discarded. The next requested section is creative play with Add to cart actions; see document20. Check existing section coverage before proposing subsequent categories or stories.

Brand direction reconfirmed 30 October 2026: palette 08 only — cobalt #2354D7, cream #FFFCF5, tangerine #FF8547, yellow #FFE16B, navy #172B4D. Use light surfaces, cobalt purchase actions and restrained warm accents. Preserve true product colours. Generated raster colours are approximate; implementation must use exact tokens. Lifestyle imagery should look candid and naturally lit, with believable hands, skin texture and accurate product geometry. Prefer genuine approved product-use photography for final assets; never present generated people as customers. WhatsApp reviews require real permission-cleared messages with personal details redacted; never fabricate social proof. Growth copy must describe play opportunities without unsupported comparative or medical promises.

Homepage handoff checkpoint, 30 October 2026: user declared the homepage design done and requested a detailed unchanged build package. The current authoritative handoff is MeshToyShop-Shopify-Project/README.md, with eight frozen boards, assets, manifests, responsive wireframes and technical specifications. Read its docs/01-design-authority.md before implementation; it resolves older contradictory status notes and excludes rejected extra RC designs. This supersedes older notes saying to design the next creative section. Preserve existing selected pastel component surfaces; palette08 governs primary/global tokens, not permission to recolour selected reference files. No deployment was performed by the handoff task.
