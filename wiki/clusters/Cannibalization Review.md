---
type: spoke
title: "Cannibalization Review"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Cannibalization Review

## Cannibalization Triage Job

Use this note when two or more pages may be competing for the same reader task, entity, conversion role, or search result. The output is a decision record for [[Semantic Topic Clusters]], not a publishing command.

### Competing Intent Signal

Treat cannibalization as a claim that needs page-level evidence. Matching keywords alone is weak evidence. A real review compares the query, landing page, title promise, entity focus, internal links, and the job the reader can complete. If GSC exports exist, use [[Google Data Integrations]] to separate query-page impressions, clicks, CTR, and position before making a merge or keep decision. Source IDs: `g-gsc-api`, `g-helpful-content`.

### False Positive Filters

Do not collapse pages that serve different funnel stages, locales, product versions, or levels of expertise. Healthy overlap is allowed when a hub explains the field and a spoke solves a narrower task. If the issue is a technical duplicate, the canonical URL decision belongs beside the Google canonicalization record rather than in a content-only rewrite. Source ID: `g-canonical`.

## Review Decision Register

| Decision case | Required inputs | Evidence state | Owner | Next action |
|---|---|---|---|---|
| Merge into one owner | GSC query-page pairs, same reader task, same conversion role | Confirm API fields, then make an advisory merge call | Content lead | Draft consolidation brief and rollback cue |
| Keep both pages | Distinct stage, entity, audience, or page promise | Advisory unless backed by query and engagement split | Cluster editor | Rewrite intros to state different jobs |
| Canonical owner unclear | Similar title and anchor text, mixed internal links | Needs canonical and internal link review | SEO lead | Pick owner or escalate to [[Cluster Canonical Page Rules]] |
| No content change | Volatility appears market-wide or zero-click related | Use `sparktoro-zero-click-2026` only as context from [[AI Citation Mechanics]] | Analyst | Monitor with property data instead of forecasting |

## Evidence Collection Procedure

1. List every candidate page, URL, target query, and intended reader outcome in one review sheet.
2. Pull GSC rows by page and query for the same date window; label missing data instead of guessing.
3. Compare headings, title tags, entities, internal anchors, and conversion calls.
4. Decide whether the reader would benefit more from merge, differentiation, canonical cleanup, or monitoring.
5. Record source IDs, confidence, owner, and the metric that would reverse the decision.

## Escalation And Monitoring

Send link-role conflicts to [[Internal Link Matrix]], missing support coverage to [[Cluster Gap Analysis]], and stale-page questions to [[Freshness and Content Decay]]. Keep the decision probabilistic: market click behavior from `sparktoro-zero-click-2026` is `AS-REPORTED` practitioner evidence, while GSC and canonicalization docs provide the stronger operating sources for page-level review.
