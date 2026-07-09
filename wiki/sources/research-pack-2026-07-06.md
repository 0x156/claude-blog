---
type: source
title: "Research Pack 2026-07-06"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [sources, research-pack, active]
domain: Sources
confidence: advisory
related: ["[[index|Index]]", "[[hot|Hot]]", "[[Research Pack Index]]", "[[Google Algorithm Update Ledger]]", "[[AI Citation Mechanics]]", "[[Blog Schema Stack]]", "[[E-E-A-T for Blog Content]]", "[[6-Pillar Dual Optimization]]", "[[Evidence Gap Register]]", "[[Claim To Source Mapping]]"]
source_urls: ["https://developers.google.com/search/updates", "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide", "https://developers.google.com/search/docs/appearance/structured-data/faqpage", "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing", "https://developers.google.com/search/docs/crawling-indexing/amp"]
---

# Research Pack 2026-07-06

Human-readable source pack for the Claude Blog Brain. The complete machine-readable list remains in `references/source-ledger.json`, which is outside this edit scope.

This note is marked advisory because the 2026-07-06 source pack assigned some documentation pages generic or mismatched dates. Use the table below for priority claims until the machine ledger is normalized with separate `published`, `last_updated`, `retrieved`, `event_date`, and `date_precision` fields.

## Priority Source Dates

| Source ID | Claim route | URL | Published | Last updated | Event date | Retrieved | Date precision | Confidence |
|---|---|---|---|---|---|---|---|---|
| `g-ranking-history` | Confirmed ranking updates | https://developers.google.com/search/updates/ranking |  | 2026-05-21 |  | 2026-07-09 | page-last-updated | verified |
| `g-status-dashboard` | Ranking incident history | https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history |  |  | 2026-06-24 latest listed incident | 2026-07-09 | retrieved-page-state | verified |
| `g-ai-opt-guide` | Generative AI Search guidance | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 2026-05-15 | 2026-06-29 | 2026-06-15 llms.txt clarification | 2026-07-09 | mixed | verified for Google guidance |
| `g-faqpage-sd` | FAQPage status | https://developers.google.com/search/updates#deprecating-the-faq-rich-result-feature |  |  | 2026-05-07 rich result retirement | 2026-07-09 | event-date | verified |
| `g-search-docs-updates-2026-07-07-product-structured-data` | July 7 merchant listing docs event | https://developers.google.com/search/updates#july-2026 |  |  | 2026-07-07 `Product.category` and sale duration docs update | 2026-07-09 | event-date | verified |
| `pending:g-search-docs-updates-2026-07-01-amp` | July 1 AMP docs event | https://developers.google.com/search/updates#july-2026 |  |  | 2026-07-01 AMP docs update | 2026-07-09 | event-date | verified, pending ledger entry |
| `pending:g-merchant-listing` | Merchant listing structured data page | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing |  | 2026-07-07 | 2026-07-07 category and sale duration docs update | 2026-07-09 | page-last-updated | verified, pending ledger entry |
| `g-product-sd` | Product structured data intro page | https://developers.google.com/search/docs/appearance/structured-data/product |  | 2025-12-10 |  | 2026-07-09 | page-last-updated | gap: ledger date mismatch |
| `pending:g-preferred-sources` | Preferred Sources availability | https://developers.google.com/search/docs/appearance/preferred-sources |  | 2026-05-27 | 2026-05-27 AI Mode and AI Overviews availability | 2026-07-09 | page-last-updated | verified, pending ledger entry |
| `g-genai-reports` | Search Console generative AI reporting | https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | 2026-06-03 |  | 2026-06-03 launch | 2026-07-09 | published-date | verified |
| `pending:google-ai-gemini-image-generation` | Gemini native image generation and SynthID | https://ai.google.dev/gemini-api/docs/image-generation |  | 2026-07-08 | 2026-07-08 model/provenance docs state | 2026-07-09 | page-last-updated | verified, pending ledger entry |
| `pending:google-ai-imagen-deprecation` | Imagen deprecation and shutdown | https://ai.google.dev/gemini-api/docs/image-generation |  | 2026-07-08 | 2026-08-17 scheduled shutdown | 2026-07-09 | page-last-updated plus future event | verified, pending ledger entry |
| `sparktoro-zero-click-2026` | Zero-click market context | https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ | 2026-06-08 |  | 2026-01 to 2026-04 study window | 2026-07-08 | study-window | advisory |
| `seer-aio-impact-ctr-2026` | AIO CTR market context | https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update | 2026-04-24 |  | 2025-12 to 2026-02 study window | 2026-07-08 | study-window | advisory |
| `ziptie-aio-source-selection` | Passage extraction heuristic | https://ziptie.dev/blog/google-ai-overviews-source-selection/ | 2026-03-25 |  |  | 2026-07-08 | published-date | practitioner |

## FAQPage Split

| Record | URL | Event date | Retrieved | Use |
|---|---|---:|---:|---|
| FAQ rich result retirement | https://developers.google.com/search/updates#deprecating-the-faq-rich-result-feature | 2026-05-07 | 2026-07-09 | Stops treating FAQPage as a current visual rich result tactic. |
| FAQ documentation removal from Search docs updates | https://developers.google.com/search/updates | 2026-06-15 | 2026-07-09 | Records that documentation was removed after the feature retired. |
| Visible Q and A content policy | [[Visible Q And A Without FAQ Rich Results]] |  | 2026-07-09 | Keeps helpful visible Q and A patterns separate from rich result claims. |

## Product Structured Data Date Split

| Record | URL | Last updated | Event date | Retrieved | Use |
|---|---|---:|---:|---:|---|
| Product intro page | https://developers.google.com/search/docs/appearance/structured-data/product | 2025-12-10 |  | 2026-07-09 | General Product structured data overview. Do not use for the July 7 event date. |
| Search docs July 7 event | https://developers.google.com/search/updates#july-2026 |  | 2026-07-07 | 2026-07-09 | Changelog source for `Product.category` and sale duration guidance. |
| Merchant listing page | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing | 2026-07-07 | 2026-07-07 | 2026-07-09 | Operational source for ecommerce markup review. |

## Ledger Repair Notes

- Do not copy a generic `published: 2026-06-30` date into new wiki claims unless the specific source proves that date.
- Use blank `published` when a page only exposes a last-updated date.
- Use `event_date` for changelog entries, deprecations, rollout starts, and retirements.
- Use `date_precision` values such as `published-date`, `page-last-updated`, `event-date`, `study-window`, `month-only`, or `unknown`.
- Split official Google guidance from third-party market behavior in claim tables.
- Add missing machine-readable ledger entries for July 2026 docs updates, Preferred Sources, Google API docs, Google AI image docs, Imagen shutdown, and C2PA before any market-ready release.

## Related

- [[Research Pack Index]]
- [[Claim To Source Mapping]]
- [[Evidence Gap Register]]
- [[Google Algorithm Update Ledger]]
- [[AI Citation Mechanics]]
- [[Blog Schema Stack]]
