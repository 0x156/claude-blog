---
type: spoke
title: "Citation Readiness Decision Tree"
domain: "Blog Content Optimization"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [dual-optimization, geo, decision-tree]
confidence: advisory
related:
  - "[[Dual Optimization]]"
  - "[[AI Citation Mechanics]]"
  - "[[Reader Value Versus Extraction Value]]"
  - "[[Classic SEO And GEO Tradeoffs]]"
source_urls:
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/docs/appearance/ai-features"
---
# Citation Readiness Decision Tree

## Citation Readiness Decision Tree Distinct Job

This note decides whether a section deserves citation-readiness work before an editor rewrites it. The goal is selection, not blanket formatting. A passage should earn GEO attention when it answers a durable question, carries evidence that can survive extraction, and still serves the reader inside the article.

The source posture is intentionally narrow. `g-ai-opt-guide` and `g-ai-features` define the Google-facing eligibility baseline. `seer-aio-impact-ctr-2026` supports interest in cited passages, but only as reported practitioner evidence. `sparktoro-zero-click-2026` keeps the planning frame honest: some value may happen without a click, which belongs in [[AI Citation Mechanics]] and [[Search Visibility Versus Citation Exposure]] rather than in a ranking promise.

### Candidate Passage Inputs

- The exact passage or section being considered.
- Query intent, entity names, source claims, and visible supporting evidence.
- Reader task served by the passage.
- Existing crawl, index, and preview restrictions.

### Decisions Returned

- `ready`: improve the passage for citation without changing the article's job.
- `revise first`: fix reader clarity, evidence, or entity context before GEO work.
- `defer`: leave the passage alone because the query, evidence, or benefit is too weak.

## Readiness Routing Table

| Branch signal | Required check | Source IDs | Decision outcome | Owner action |
|---|---|---|---|---|
| Answer is self-contained | Can the passage stand alone without losing qualifiers? | `g-ai-opt-guide`, `g-ai-features` | Ready or revise first | Editor tightens context and visible sourcing |
| Citation value is plausible | Does the section address a likely answer-surface question? | `seer-aio-impact-ctr-2026` | Ready only with caveat | Strategist marks evidence as as-reported |
| Click value may be limited | Does the page still need non-click success metrics? | `sparktoro-zero-click-2026` | Add measurement note | Analyst links to [[Zero Click Planning Baseline]] |
| Reader value is fragile | Would extraction formatting harm flow or trust? | `g-ai-opt-guide` | Revise first or defer | Content lead protects the article experience |

## Branch Procedure

1. Identify one candidate passage, not the whole article.
2. Write the reader question that the passage answers.
3. Check whether the evidence is visible, dated, and specific enough for reuse.
4. Choose ready, revise first, or defer.
5. Send ready passages to [[Reader Value Versus Extraction Value]] for final editing.

## Evidence Refresh Rules

Refresh this decision tree when Google changes AI feature documentation, when a new AIO cited-page study enters the source ledger, or when first-party reporting proves that a passage class performs differently from market expectations.
