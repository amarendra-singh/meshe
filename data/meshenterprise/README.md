# Mesh Enterprise public catalogue capture

Captured on 22 October 2026 (Asia/Kolkata) from [meshenterprise.jdwebshop.com](https://meshenterprise.jdwebshop.com/).

- [products.csv](products.csv): 17 public product listings with names, categories, prices, stock labels, descriptions, source links, and image URLs. This is a research export, not a Shopify import CSV.
- [products.json](products.json): the same records with gallery image URLs and related-product URLs as arrays, plus the displayed description HTML.
- [shopify-import.csv](shopify-import.csv): 17 products with 83 image rows, transformed for Shopify import with draft status and online-store publication disabled. [build-shopify-import.ps1](build-shopify-import.ps1) generates it from the capture.

Coverage was checked against all four category pages: Others (2), EXCLUSIVE GADGETS (7), Educational Toys (1), and Remote control Toys (7). The related-product links across these pages pointed only to these 17 products. There are 83 gallery image URLs; images were linked, not downloaded. No variant selectors were observed on the product pages, and all 17 displayed “In stock” when captured.

Two product pages rendered without a title: `SKU1791297933569505` and `SKU179120992137366`. Their titles come from the corresponding category listings, identified by `title_source`. Prices, availability, and product copy can change. Descriptions are copied from the source site and their marketing claims have not been independently verified.

The 17 products were imported to `meshtoyshop` as **drafts**. The source descriptions, compare-at prices, image rights, and product facts must be checked before activation. See the [Dawn build status](../../docs/05-dawn-build-status.md) for the quality gate.
