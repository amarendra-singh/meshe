# 05 — Content and destination registry

Machine-readable exact UI copy: [content.json](../data/content.json). Keep punctuation and British/Indian English: colours, favourite, practise. Do not add SEO keyword strings or developmental claims to concise visible titles. Content strings are merchant-editable; this registry is the initial approved-design baseline.

## Header/hero/category copy

- Ticker: Discover toys for every kind of play →
- Logo text: Mesh Toy Shop
- Desktop menu: RC Toys / Puzzles / Gadgets
- Hero: Let curiosity lead.
- Hero support: RC adventures, puzzles and hands-on play to discover together.
- Hero actions: Explore toys / Shop RC toys

| Category | Supporting copy | Destination binding |
|---|---|---|
| Remote Control | Simple joys. Big adventures indoors and out. | Selected Remote Control collection |
| Puzzles & Play | Hands-on fun for everyday moments. | Selected puzzles collection |
| Gadgets | Little surprises to explore and share. | Selected gadgets collection |
| Educational | Build, try and discover together. | Selected educational collection |

## Discovery

Little hands. Big discoveries.

Match a pattern. Make a shape. Try a new way.

| Chip | Product title | Supporting sentence | Action |
|---|---|---|---|
| MATCH | Colour Coder | Slide colours to match a pattern. | View toy |
| DRAW | Magnetic Drawing Board | Lift beads with the magnetic pen. | View toy |
| BUILD | DIY Screw Drill Puzzle | Build pictures with shapes and screws. | View toy |
| SOLVE | 3D Maze Cube | Guide the ball through the maze. | View toy |

Section action: Explore learning toys.

## Shared play

A PLAY IDEA TO SHARE

The joy of figuring it out.

A pattern to solve. A little encouragement. A moment to share.

Steps: Pick a pattern / Slide to match / Swap turns.

Explore Colour Coder.

## Creative shopping

THE CREATIVE CORNER

Made by little hands.

Peel a sticker. Place a bead. Make it their own.

Sticker-by-Number Book — Match numbers to make animal pictures. — ₹250.

Mosaic Bead Board — Place colourful beads to create a pattern. — ₹625.

Both Add to cart; section Explore creative play. Product body sentences are not shown in the selected mobile purchase rows.

## Video shopping

Watch them play.

See how it works. Find their next favourite.

| Toy | Poster caption | Reference price |
|---|---|---|
| Colour Coder | Slide. Match. Try again. | ₹450 |
| Sticker-by-Number Book | One sticker at a time. | ₹250 |
| Mosaic Bead Board | Build a colourful pattern. | ₹625 |

Add to cart for each; mobile Swipe to explore. Mockup warning is outside shopper UI.

## Growth

Play that gives them room to grow.

Ways to practise, create and connect.

| Heading | Body | Label |
|---|---|---|
| Attention & patience | Follow a pattern, one move at a time. | Pattern play |
| Problem-solving | Test a piece. Change the plan. Try again. | Building play |
| Creative expression | Choose colours. Make a picture their own. | Art & making |
| Connection & emotions | Take turns, name feelings and celebrate effort. | Playing together |

Explore ways to play.

## Customer stories

Your playtime stories.

A closer look at everyday play.

Matching toy / View toy are placeholder footer labels. Actual customer content is absent; never create testimonial text from these headings. Preview labels are 'LAYOUT PREVIEW — REAL CUSTOMER SCREENSHOTS NEEDED', 'Customer screenshot' and 'PLACEHOLDER — NOT A CUSTOMER MESSAGE'.

## FAQ

A few things before playtime.

Choosing, ordering and getting ready to play.

Choosing a toy:

1. **How do I choose the right toy?** Start with what they enjoy: puzzles, building, art or imaginative play. Check the toy’s age guidance before choosing. This exact answer is visible in M08.
2. **Can play support focus and patience?** Draft: Matching a pattern or trying a puzzle gives children opportunities to stay with a task and try again. Follow their pace and keep play enjoyable; outcomes vary.
3. **Which toys work without batteries?** Draft: Many puzzles, art activities and building sets work without batteries. Check each product’s power requirements and included accessories.
4. **What comes in the box?** Draft: Contents vary by product. Check the listing for pieces, accessories and any batteries needed. Ask us if anything is unclear before ordering.
5. **Can you help me choose a gift?** Draft: Tell us the child’s age, interests and your budget, and we can help you compare suitable options. Follow the manufacturer’s age guidance.

Orders & support — questions locked, answers require operational confirmation:

6. When will my order arrive?
7. How much does shipping cost?
8. Can I pay on delivery?
9. What if an item arrives damaged?
10. Can I cancel or return an order?

Proposed answers are in docs 09, not approved merchant promises. Keep placeholders clearly identified in editor previews and do not publish empty or misleading answers.

Contact strip: Still have a question? / Send us the product names and what you’re looking for. / Ask Mesh.

## Destination requirements

Use Shopify route objects, selected product/collection objects and menu links; avoid hardcoded guessed handles. Data/product-map.json gives identifiers only where historical evidence exists. Resolve current IDs before implementation. A product title may have a shorter editorial label without changing its official catalog title. Link the label/image to its actual PDP.

No '#' destinations, empty hrefs, unrelated collection fallbacks, duplicate purchase nested inside links, or dead play buttons. Missing support number means use the verified contact page rather than inventing a WhatsApp number. External chat opens only after a user action; don't send messages automatically.
