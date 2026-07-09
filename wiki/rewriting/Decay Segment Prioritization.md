---
type: spoke
title: "Decay Segment Prioritization"
domain: "Blog Rewriting"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [rewriting, freshness, content-decay, active]
---

# Decay Segment Prioritization

## Prioritization Queue Purpose

This note ranks decay candidates after [[Content Decay Detection]] has identified a credible problem. Its job is to prevent the loudest page, newest complaint, or most recent Google rumor from consuming the rewrite queue.

The scoring basis starts with reader usefulness from `g-helpful-content`: pages that block an important task outrank pages with cosmetic age. Confirmed update context comes from `g-ranking-history` and `g-status-dashboard`, which are official history sources rather than impact-analysis tools. `g-update-2024-06-20-june-2024-spam-update` is useful here as a concrete example of how a dated spam update should be recorded: start date, official source, and no unsupported claim about a specific site.

### Signals This Queue Owns

Prioritization owns severity, confidence, reversibility, source risk, and editorial effort. It does not decide the final treatment. Send treatment choice to [[Refresh Versus Rewrite Decision]], merge candidates to [[Content Consolidation Rules]], and rollback planning to [[Rewrite Rollback Notes]].

### Boundaries Before Scoring

Do not score a page until the decay signal has a named evidence trail. If the only reason is "Google update happened," return the item to monitoring until the update window and affected page pattern are documented. If the page handles a trust-sensitive topic, raise the source-risk score even when traffic is not the largest opportunity.

## Priority Scoring Table

| Candidate segment | Reader value | Evidence basis | Priority action | Owner | Deferral reason |
|---|---:|---|---|---|---|
| High-intent evergreen guide with stale process steps | 5 | `g-helpful-content` supports usefulness review | Refresh sources and examples first | Editor | Defer only if source owner is unavailable |
| Cluster page affected during confirmed rollout window | 4 | `g-ranking-history`; `g-status-dashboard` | Compare changes against confirmed dates before rewriting | Monitoring owner | Defer if timing does not align |
| Thin article with no distinct reader job | 2 | `g-helpful-content` | Move to prune or merge review | Content lead | Defer if a unique audience use case appears |
| Page cited in old spam-update rationale | 3 | `g-update-2024-06-20-june-2024-spam-update` as dated update record pattern | Check for policy-related content risks without claiming causality | SEO strategist | Defer if evidence is only anecdotal |
| Recently published post with short-lived dip | 1 | `g-status-dashboard` for official update context | Hold for another review cycle | Analyst | Defer because evidence is immature |

## Queue Review Procedure

1. Assign each candidate one primary reason for urgency: reader harm, source risk, confirmed update context, business dependency, or technical duplication.
2. Score confidence separately from opportunity so weak evidence cannot outrank a smaller but well-supported fix.
3. Confirm whether the item needs source refresh, editorial rewrite, consolidation, pruning advice, or observation.
4. Record a due date and rollback owner only after the action type is chosen.

## Prioritization Source IDs

`g-helpful-content`; `g-ranking-history`; `g-status-dashboard`; `g-update-2024-06-20-june-2024-spam-update`.

## Related

- [[Freshness and Content Decay]]
- [[Content Decay Detection]]
- [[Refresh Versus Rewrite Decision]]
- [[Rewrite Rollback Notes]]
- [[2026 Google Update Timeline]]
