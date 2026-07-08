---
type: source
title: "Research Pack 2026-07-06"
status: active
created: 2026-07-06
updated: 2026-07-08
tags: [sources, research-pack, evidence]
domain: Sources
confidence: advisory
related: ["[[index|Index]]", "[[hot|Hot]]", "[[Research Pack Index]]", "[[Google Algorithm Update Ledger]]", "[[AI Citation Mechanics]]", "[[Blog Schema Stack]]", "[[E-E-A-T for Blog Content]]", "[[6-Pillar Dual Optimization]]", "[[Evidence Gap Register]]", "[[Claim To Source Mapping]]"]
source_urls: ["https://developers.google.com/search/updates", "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide", "https://developers.google.com/search/docs/appearance/structured-data/faqpage", "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing", "https://developers.google.com/search/docs/crawling-indexing/amp"]
---

# Research Pack 2026-07-06

Human-readable source pack for the Claude Blog Brain. The complete machine-readable list remains in `references/source-ledger.json`, which is outside this edit scope.

This note is marked advisory because the 2026-07-06 source pack assigned many documentation pages a generic published date. Use the table below for priority claims until the machine ledger is normalized with separate `published`, `last_updated`, `retrieved`, `event_date`, and `date_precision` fields.

## Priority Source Dates

| Source ID | Claim route | URL | Published | Last updated | Event date | Retrieved | Date precision | Confidence |
|---|---|---|---|---|---|---|---|---|
| `g-ranking-history` | Confirmed ranking updates | https://developers.google.com/search/updates/ranking |  | 2026-05-21 |  | 2026-07-06 | page-last-updated | verified |
| `g-status-dashboard` | Ranking incident history | https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history |  |  | 2026-06-24 latest listed incident | 2026-07-08 | retrieved-page-state | verified |
| `g-ai-opt-guide` | Generative AI Search guidance | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 2026-05-15 | 2026-06-29 | 2026-06-15 llms.txt clarification | 2026-07-08 | mixed | verified for Google guidance |
| `g-faqpage-sd` | FAQPage status | https://developers.google.com/search/docs/appearance/structured-data/faqpage |  |  | 2026-05-07 rich result retirement | 2026-07-06 | event-date | verified |
| `g-search-docs-updates` | Documentation change log | https://developers.google.com/search/updates |  |  | 2026-07-01 AMP, 2026-07-07 merchant listing | 2026-07-08 | event-date | verified |
| `g-amp-docs` | AMP maintenance guidance | https://developers.google.com/search/docs/crawling-indexing/amp |  | 2026-07-01 | 2026-07-01 docs update | 2026-07-08 | page-last-updated | verified |
| `g-merchant-listing` | Merchant listing structured data | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing |  | 2026-07-07 | 2026-07-07 category and sale duration docs update | 2026-07-08 | page-last-updated | verified |
| `g-genai-reports` | Search Console generative AI reporting | https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | 2026-06-03 |  | 2026-06-03 launch | 2026-07-06 | published-date | verified |
| `sparktoro-zero-click-2026` | Zero-click market context | https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/ | 2026-06-09 |  | 2026-01 to 2026-04 study window | 2026-07-06 | study-window | advisory |
| `seer-aio-impact-ctr-2026` | AIO CTR market context | https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update | 2026-04-24 |  | 2025-12 to 2026-02 study window | 2026-07-06 | study-window | advisory |
| `ziptie-aio-source-selection` | Passage extraction heuristic | https://ziptie.dev/blog/google-ai-overviews-source-selection/ | 2026-03-25 |  |  | 2026-07-06 | published-date | practitioner |

## FAQPage Split

| Record | URL | Event date | Retrieved | Use |
|---|---|---:|---:|---|
| FAQ rich result retirement | https://developers.google.com/search/docs/appearance/structured-data/faqpage | 2026-05-07 | 2026-07-06 | Stops treating FAQPage as a current visual rich result tactic. |
| FAQ documentation removal from Search docs updates | https://developers.google.com/search/updates | 2026-06-15 | 2026-07-08 | Records that documentation was removed after the feature retired. |
| Visible Q and A content policy | [[Visible Q And A Without FAQ Rich Results]] |  | 2026-07-08 | Keeps helpful visible Q and A patterns separate from rich result claims. |

## Ledger Repair Notes

- Do not copy a generic `published: 2026-06-30` date into new wiki claims unless the specific source proves that date.
- Use blank `published` when a page only exposes a last-updated date.
- Use `event_date` for changelog entries, deprecations, rollout starts, and retirements.
- Use `date_precision` values such as `published-date`, `page-last-updated`, `event-date`, `study-window`, `month-only`, or `unknown`.
- Split official Google guidance from third-party market behavior in claim tables.
- Add missing machine-readable ledger entries for July 2026 docs updates before any market-ready release.

## Related

- [[Research Pack Index]]
- [[Claim To Source Mapping]]
- [[Evidence Gap Register]]
- [[Google Algorithm Update Ledger]]
- [[AI Citation Mechanics]]
- [[Blog Schema Stack]]
