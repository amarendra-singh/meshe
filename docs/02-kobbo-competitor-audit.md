# Kobbo competitor audit

Research date: 22 October 2026  
Method: Tabbit browser inspection, rendered-page styles/content, screenshots, and reversible UI interaction.

## 1. Scope and limits

Inspected:
- Homepage on desktop and at a 390 × 844 mobile viewport.
- Desktop age menu, homepage age buttons, and mobile navigation.
- Search with the term puzzle.
- General catalogue and ascending-price sorting.
- Age 2–3 collection.
- Little Explorer Kit and Splash & Play Water Sink product pages.
- Cart drawer, cart page, and checkout entry.
- About, Contact, FAQ, Shipping, and Return pages.
- Selected rendered-page metadata.
- CSS animation behaviour under reduced-motion emulation.

Desktop inspections included a wide browser viewport and a 1440 × 900 viewport. These were browser viewport tests, not physical-device tests.

Not established:
- Sales, AOV, conversion rate, return rates, profitability, or customer satisfaction.
- Payment completion, final discount eligibility, or successful delivery.
- Every product, browser, device size, or assistive technology.
- Search ranking/indexing, controlled loading benchmarks, or field performance metrics.
- Correctness of developmental/safety claims or legal enforceability of policies.

Some UI reads occurred during loading; final observations were checked again where necessary. Loading-state screenshots must not be treated as final functional failures.

## 2. Overall assessment

Kobbo's strengths are coherent visual branding, a focused age-based kit proposition, clear kit imagery, product demonstrations, and a functional mobile purchase path.

Its most useful lessons for Mesh are:
1. Keep the catalogue and homepage promise aligned.
2. Give shoppers concrete product and service information.
3. Keep policy messages consistent across pages.
4. Explain offers through the cart/checkout journey.
5. Combine strong visuals with useful discovery controls.

These are design and merchandising judgments, not claims about commercial performance.

## 3. Positioning and catalogue alignment

The homepage concentrates on play kits for ages 2–5 and simplifies the choice into two age groups. The broader catalogue includes products for older users and adults. Homepage videos include an office punching ball and table-tennis equipment alongside children's play products.

The About page explicitly describes individual toys as well as kits, so a broad catalogue is not inherently contradictory. However, the first-screen proposition is narrower than the range later presented.

Mesh implication: align the hero, product selection, videos, category labels, and audience. Decide the breadth of the brand before finalising navigation.

Sources: [homepage](https://www.kobbo.in/), [shop](https://www.kobbo.in/shop), [about](https://www.kobbo.in/about).

## 4. Actual visual design system

### Colours

| Role | Observed value |
|---|---|
| Main accent | Yellow #FFC700 |
| Warm surfaces | Cream #FFF8E8 |
| Main text / dark surfaces | Charcoal #1F1F1F |
| Hero text | Near-black #1A1A1A |
| Secondary text | Grey #6B6B6B |
| Card surfaces | White #FFFFFF |
| Supporting green | #16A34A |

The palette feels warm and playful. Repeating yellow in the logo, primary actions, active states, and small graphics makes it recognisable. White cards separate products from cream surfaces. The dark footer provides a clear page ending.

Computed contrast examples:
- #1F1F1F against #FFC700: approximately 10.53:1.
- White against #FFC700: approximately 1.56:1.

These are calculations for the specified solid colour pairs, not a complete accessibility audit.

### Typography

- Headings: Baloo 2, commonly weight 800.
- Body and UI: Inter.
- Desktop hero: approximately 72px.
- Mobile hero: approximately 53px in the tested viewport.
- Desktop section headings: approximately 30–48px.
- Common UI/body sizes: 14–16px.
- Some small footer text: 11–12px.

Assessment: expressive headings are balanced by conventional body typography. Mesh should use fewer, consistently defined heading sizes and preserve readable mobile product titles.

### Shapes, spacing, and surfaces

- Pill-like primary buttons and selection controls.
- Rounded product cards and gallery surfaces.
- Cream/white section contrast.
- Generous desktop content margins.
- A centred content area around 1280px in the wide desktop inspection.
- A white founder-message panel with a noticeable shadow.
- Large lower-page spacing and several sections repeating kit benefits.

Mesh implication: define spacing, radius, typography, and button rules as a system rather than styling sections independently.

## 5. Header and navigation

Observed:
- Compact header with logo, age navigation, About/Contact, search, account, and cart.
- Simple age dropdown.
- Mobile menu with large rows, approximately 56px high.
- Header icon targets around 40px.
- Header remains accessible while scrolling in tested states.
- Homepage older-age CTA correctly switched the featured kit.

Announcement strip:
- Repeats shipping, age suitability, and payment reassurance.
- Continuously moving content adds activity above the hero.

Mesh implication:
- Prioritise the shopping routes that match the real catalogue.
- Keep search easy to reach.
- Prefer concise announcements.
- Use comfortable icon targets and clear active/focus states.
- Consider interest and gift navigation for a broad catalogue.

## 6. Hero and homepage sequence

Hero:
- Lifestyle photography with a child.
- Short headline and explanatory copy.
- Two prominent age actions.
- Supporting benefit statements.
- Desktop image/text split, adapted to stacked mobile content.

At 390 × 844, age actions appeared before the large lifestyle image finished. The first product-section heading began around 933px down the page, so the first viewport did not include a purchasable product with price.

This is a trade-off between storytelling and immediate product visibility, not evidence of poor conversion.

Sequence:
1. Hero and age selection.
2. Featured kit.
3. Development-oriented messaging.
4. Video demonstrations.
5. Founder story.
6. Further kit benefits.
7. Footer.

Assessment:
- Strong consistency and visual rhythm.
- Repetition between introductory benefits and lower kit-benefit sections.
- A developmental statistic has a broad research attribution rather than a specific linked study visible in inspected content. It does not establish the effectiveness of the products.

Mesh implication: every section should answer a different buying question. Use sourced, specific claims where evidence is needed.

## 7. Photography, video, and motion

Strong:
- Kit main image shows contents, packaging, and guide together.
- Multiple gallery images support inspection.
- Demonstrations show use.
- Branded packaging helps make a set feel tangible.

Less consistent:
- General catalogue mixes lifestyle images, cutouts, and busy promotional compositions.
- Long product titles and varied images make a two-column mobile grid harder to scan.
- Some homepage video subjects are broader than the main age proposition.

Motion:
- Announcement marquee.
- Hero image entrance and slow movement.
- Floating decorative elements.
- Train divider and other playful details.

Verified positive: enabling reduced motion stopped the running CSS animations observed in the test. This does not cover every possible video or JavaScript animation.

Mesh implication: consistent image ratios, actual product demonstrations, modest animation, and reduced-motion support.

## 8. Product discovery

Verified:
- A puzzle search returned a relevant product.
- Ascending-price sorting eventually settled into the expected order.
- Search and sort controls are present.
- Product cards offer wishlist and quick-add actions.
- Some cards display real-looking rating/count UI; authenticity was not independently verified.
- The mobile grid has two columns.
- Incremental product loading is available.
- The inspected age 2–3 collection had one product.

Not observed on the general shop:
- Dedicated age, price-range, category, or interest filters.

Mesh implication:
- Add useful filters based on product data.
- Keep display titles short.
- Include suitable age where supported.
- Show reviews only where genuine data exists.
- Test search relevance, synonyms, no-result states, and sorting.

Sources: [shop](https://www.kobbo.in/shop), [age collection](https://www.kobbo.in/shop-by-age/year-2).

## 9. Product-page findings

### Little Explorer Kit

Observed price: ₹2,999.

Strengths:
- Nine gallery images.
- Linked age information.
- Clear price and quantity controls.
- Primary purchase actions.
- Illustrated explanations of kit contents.
- Parent guide included in the presentation.
- Related products and recently viewed section.
- Fixed mobile price-and-add-to-cart bar.

Gaps/opportunities:
- Short introduction partly hidden by an expansion control.
- General benefit language rather than a concise technical/service summary near the purchase controls.
- No customer-review section observed during the inspected kit-page session.
- No direct service links observed within the kit's main content in the targeted check.
- More complete materials, size, care, warnings, and delivery information would help shoppers assess suitability.

### Splash & Play Water Sink

Observed price: ₹1,299, with a crossed-out ₹1,499.

Strengths:
- Demonstration section.
- Description, features, and specification tabs.
- Specifications identify age 3+, dimensions 28 × 23.5 × 21cm, battery operation, and batteries not included.
- Stock information.
- Mobile fixed purchase bar.

Concern:
- A seven-day replacement message is not clearly reconciled with general policy/FAQ reporting windows.

Both sampled pages displayed the same four related products. This is an observation of those sessions, not proof that recommendations are always static.

Sources: [kit](https://www.kobbo.in/products/the-little-explorer-kit), [water sink](https://www.kobbo.in/products/splash-play-water-sink).

## 10. Pricing, offers, and AOV

Observed:
- Little Explorer Kit: ₹2,999.
- Older-age Tinker Kit: ₹3,499.
- Kit page promotes ₹150 off prepaid orders plus a free gift.
- Four related products on the inspected kit page were each ₹499.
- Free shipping is advertised.

Interpretation:
- Curated sets give customers a reason to buy multiple products together.
- Related products create a potential add-on route.
- Prepaid incentives encourage payment choice and affect margins; they are not inherently an AOV increase.
- Free shipping on all orders reduces delivery friction but does not establish a threshold-based incentive.

Unknown:
- Whether these tactics improve sales or profit.
- Whether the free gift or prepaid reduction is applied later.
- Product costs or contribution margins.

## 11. Service promises and trust

| Page | Observed statement | Concern |
|---|---|---|
| Return policy | Damage/missing-part reports within 24 hours | Short reporting window |
| FAQ | Damage/missing-part support with reporting within 24–48 hours | Different window |
| Water-sink product | Seven-day replacement message | Relationship to other windows unclear |

These may be intended product-specific conditions, but the inspected pages did not clearly explain the distinction.

Other observations:
- Phone and email support are visible.
- Contact page uses hello@kobbo.in and also references support@kobbo.in.
- No support hours or reply-time commitment observed on that page.
- Founder content adds personality.
- A founder story and generic payment reassurance do not replace product-specific evidence.

Mesh implication:
- One consistent source of policy content.
- Explicit product-specific exceptions.
- Clear reporting methods and support hours.
- Real photos, actual reviews, and supported claims.
- No fabricated scarcity, reviews, certification badges, or guarantees.

Sources: [returns](https://www.kobbo.in/return-policy), [FAQ](https://www.kobbo.in/faqs), [contact](https://www.kobbo.in/contact).

## 12. Shipping

Observed policy:
- Free shipping across India.
- Dispatch usually within five business days, subject to availability.
- Delivery generally 7–15 days after dispatch.
- Tracking after shipment.

Dispatch and transit are separate periods. The wording matters for date-sensitive gift purchases.

Mesh implication: show realistic dispatch/delivery estimates near the purchase decision, ideally location-aware if operations and tooling support it. Do not promise faster delivery before confirming capability.

Source: [shipping policy](https://www.kobbo.in/shipping-policy).

## 13. Cart and checkout

Test:
1. Confirmed cart was empty.
2. Added one Little Explorer Kit.
3. Verified cart drawer and cart page.
4. Opened checkout entry without entering personal data.
5. Returned to storefront cart, removed test item, and verified empty-cart content.

Observed cart:
- Item, image, quantity, remove action.
- Subtotal and total ₹2,999.
- Free shipping.
- Clear checkout and continue-shopping actions.
- No complementary-product, gift-option, or prepaid-offer explanation observed in the tested cart.
- Gift not displayed as a separate cart item.

Observed checkout:
- Redirected to a separate myshopify.com hostname.
- Simplified branding.
- GoKwik COD and Razorpay choices displayed.
- Final payment/discount behaviour was not tested.

Mesh implication:
- Maintain brand continuity where the platform allows.
- Explain conditional offers and their application point.
- Show accurate totals and shipping.
- Keep cart extras selective and relevant.
- Test provider handoff and return navigation before launch.

No purchase was completed.

## 14. Accessibility, metadata, and performance

Positive:
- Labelled icon controls.
- Large main purchase buttons.
- Mobile fixed purchase bar.
- No page-level horizontal overflow in tested views.
- Observed CSS animations respected reduced motion.

Opportunities:
- Some cart quantity buttons around 28px.
- Some wishlist buttons around 32px.
- Small secondary text and long titles need deliberate mobile treatment.
- Full keyboard/focus/screen-reader testing remains outstanding.

Metadata:
- Home and kit titles/descriptions were present.
- No canonical link found in the rendered DOM checks.
- No JSON-LD script found in those checks.
- Kit description metadata appeared truncated mid-word.

Limits:
- Other structured-data formats were not comprehensively checked.
- These observations do not prove indexing or ranking outcomes.
- No Lighthouse/field performance score was measured.
- Navigation timing from a single browser session would not establish general customer experience.

Mesh implication: verify metadata, appropriate structured data, image loading, layout movement, interaction responsiveness, keyboard access, and real mobile performance.

## 15. Priorities for Mesh

| Priority | Action |
|---|---|
| P1 | Align positioning, catalogue, and homepage |
| P1 | Make service promises consistent |
| P1 | Provide complete product-specific buying information |
| P1 | Verify cart, offers, shipping, payment, and checkout |
| P2 | Improve age/interest/price discovery where catalogue supports it |
| P2 | Standardise photography and product cards |
| P2 | Maintain clear mobile hierarchy and touch targets |
| P2 | Build genuine proof and accessible support |
| P3 | Add restrained animation and optional enhancements |

## 16. Evidence files

Selected browser screenshots are archived in [evidence/kobbo](evidence/kobbo/). See its index for context and caveats.

They are competitor research references, not assets licensed for Mesh's website. The full-home capture includes a transient hero animation state; use the earlier desktop hero capture for the visible hero design.
