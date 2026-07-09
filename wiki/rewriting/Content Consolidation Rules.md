---
type: spoke
title: "Content Consolidation Rules"
domain: "Blog Rewriting"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [rewriting, freshness, content-decay, active]
---

# Content Consolidation Rules

## Consolidation Rule Scope

This note decides when two or more blog URLs should become one editorial asset. It does not approve a redirect, CMS edit, or publication change. It gives the content lead a source-cited recommendation that can be reviewed beside [[Freshness and Content Decay]], [[Content Decay Detection]], and [[Intent Drift Audit]].

Use consolidation only when overlap is harming reader clarity or measurement. `g-helpful-content` supports the people-first test: if separate pages force readers to stitch together the answer, the split is suspect. `g-gsc-api` gives the query, page, click, impression, CTR, and position dimensions needed to compare pages before recommending a retained URL. `g-canonical` is the technical source for canonical and redirect signal handling, while `g-ranking-history` keeps broad update narratives tied to confirmed Google history rather than rumor.

### Merge Actions And Blocks

Allowed advisory outputs: keep one URL as the owner, merge unique evidence into it, recommend internal-link updates, recommend a canonical or redirect review, or defer because the pages serve different jobs.

Disallowed outputs: deleting content because it is old, overwriting experience evidence without a source trail, treating canonicalization as a substitute for editorial fit, or promising ranking recovery after a merge.

### Consolidation Exceptions Requiring Approval

Escalate before recommending consolidation when a URL has external backlinks, revenue attribution, legal review history, paid campaign dependencies, or a distinct audience segment. These cases need a rollback owner and a live-system approver outside this V1 brain.

## Consolidation Rule Table

| Rule | Evidence source | Applies to | Exception | Approval path |
|---|---|---|---|---|
| Merge only when pages answer the same reader task | `g-helpful-content` | Duplicate explainers, overlapping comparisons, old update posts | Different intent or funnel stage | Content lead plus editor |
| Pick the retained URL from first-party performance and fit | `g-gsc-api` | URLs with query and page history | No clean winner in data | Analyst documents tie and defers |
| Preserve unique sourced sections before draft merge | `g-helpful-content` | Experience, examples, dated claims | Unsupported or stale evidence | Source steward refreshes first |
| Route canonical or redirect notes to technical review | `g-canonical` | Duplicate URLs, syndicated variants, protocol or path variants | Editorial overlap without URL duplication | SEO technical owner |
| Do not blame an unconfirmed update for overlap | `g-ranking-history` | Consolidation triggered after volatility | Confirmed rollout window matches decline | Monitoring owner checks [[Google Algorithm Update Ledger]] |

## Consolidation Review And Reversal

1. Confirm the current reader job for every candidate URL.
2. Pull page-level GSC comparisons for the same date range and locale.
3. List claims and examples that would be lost if the weaker URL disappeared.
4. Name the retained URL, the absorbed sections, and the links that need review.
5. Define rollback as restoring the separated editorial plan if the merge damages the reader path or measurable query coverage.

## Source IDs Used

`g-helpful-content`; `g-gsc-api`; `g-ranking-history`; `g-canonical`.

## Related

- [[Freshness and Content Decay]]
- [[Content Decay Detection]]
- [[Intent Drift Audit]]
- [[Google Data Integrations]]
- [[Google Algorithm Update Ledger]]
