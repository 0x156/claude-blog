---
type: hub
title: "Freshness and Content Decay"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [rewriting, freshness, content-decay, active]
domain: "Blog Rewriting"
confidence: verified
related:
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Dual Optimization]]"
  - "[[Google Algorithm Update Ledger]]"
  - "[[E-E-A-T for Blog Content]]"
  - "[[Google Data Integrations]]"
  - "[[Blog Quality Score]]"
  - "[[Research Pack Index]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/updates/ranking"
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
  - "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
---

# Freshness and Content Decay

## Summary

Freshness and content decay work decides when a blog post should be refreshed, merged, expanded, pruned, or left alone.

This hub keeps rewriting evidence-led and prevents stale recommendations from being presented as current.

## Current fact anchors

- Google helpful content guidance, retrieved 2026-07-06, supports quality review against usefulness, originality, and reader satisfaction.
- The Google ranking update history source in the ledger is dated 2026-05-21.
- The Google Search Status Dashboard is the authority route for confirmed ranking update history in the substrate.
- Search Console generative AI performance reports were announced in June 2026 for AI Overviews and AI Mode surfaces.
- The substrate records no Google-owned ranking, spam, schema, QRG, or AI search update from 2026-07-01 through 2026-07-06.

## Scope

- Detect traffic decay with [[Google Data Integrations]].
- Detect content staleness with source dates and changed requirements.
- Detect intent drift through [[SERP-Informed Briefs and Outlines]].
- Detect schema drift through [[Blog Schema Stack]].
- Detect trust gaps through [[E-E-A-T for Blog Content]].
- Detect AI citation gaps through [[AI Citation Mechanics]].
- Decide refresh, rewrite, consolidate, prune, or no action.
- Record update rationale in [[log]].

## Future spoke notes

- [[Content Decay Detection]]
- [[Refresh Versus Rewrite Decision]]
- [[Source Refresh Workflow]]
- [[Intent Drift Audit]]
- [[Historical Performance Review]]
- [[Content Consolidation Rules]]
- [[Pruning Advisory Checklist]]
- [[Update Timestamp Policy]]
- [[Stale Claim Register]]
- [[Rewrite QA Checklist]]

## Rewrite triggers

- A current claim has a source older than its refresh cadence.
- Google guidance or structured data eligibility changed.
- GSC shows declining impressions or CTR for target queries.
- GA4 engagement declines after traffic mix changes.
- AI Overview or AI Mode impressions change in available GSC reporting.
- SERP intent no longer matches the article angle.
- Internal links point to obsolete cluster priorities.
- The post lacks visible author, source, or update signals.

## Source posture

- Date every freshness claim.
- Prefer first-party property data over market studies.
- Quarantine unconfirmed volatility until [[Google Algorithm Update Ledger]] has a Google-owned source.
- Treat rewrite actions as advisory until approved outside V1.
- Preserve old evidence through source URLs rather than deleting context.

## Related themes

- [[Dual Optimization]]
- [[6-Pillar Dual Optimization]]
- [[E-E-A-T for Blog Content]]
- [[AI Citation Mechanics]]
- [[Semantic Topic Clusters]]
- [[Google Data Integrations]]
- [[Google Algorithm Update Ledger]]
- [[Blog Quality Score]]

## Sources

- Google helpful content guidance, retrieved 2026-07-06.
- Google ranking update history, dated 2026-05-21.
- Google Search Status Dashboard, retrieved 2026-07-06.
- Search Console generative AI reports, 2026-06-03.

## Next actions

- Fill [[Content Decay Detection]] before automation rules.
- Fill [[Refresh Versus Rewrite Decision]] before rewrite playbooks.
- Link rewrite scoring to [[Blog Quality Score]].
