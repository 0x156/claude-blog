---
type: spoke
title: "Pruning Advisory Checklist"
domain: "Blog Rewriting"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [rewriting, freshness, content-decay, active]
---

# Pruning Advisory Checklist

## Pruning Review Scope

This checklist decides whether pruning can be recommended for review. It does not delete, unpublish, noindex, redirect, or mutate a live system. A pruning recommendation is valid only after the page has failed usefulness, evidence, performance, and consolidation checks.

`g-helpful-content` is the main quality source: a page with weak traffic may still be useful if it serves a clear reader need. `g-gsc-api` supports a first-party evidence check for page and query visibility. `g-ranking-history` keeps algorithm context official, and `g-canonical` prevents pruning a page that actually needs duplicate URL cleanup or consolidation.

### Checks Unique To This Gate

Pruning review asks whether the content has a distinct job, a source-supported claim set, a useful internal-link role, recoverable historical value, or a better canonical home. If any of those remain strong, the page should move to refresh, rewrite, consolidation, or archive planning instead of prune advice.

### Inputs Required Before Review

Bring the candidate URL, current owner, GSC page evidence when available, source age notes, internal-link context, canonical status, and a proposed replacement path if the page is removed from the editorial plan.

## Pruning Pass Fail Table

| Check | Pass or fail evidence | Severity | Owner | Fix status |
|---|---|---|---|---|
| Reader job is absent or redundant | `g-helpful-content` review finds no distinct useful task | Blocker if unreviewed | Editor | Pass only after intent audit |
| Page has no meaningful first-party visibility | `g-gsc-api` page and query review is empty or negligible | Medium unless page has non-search value | Analyst | Pass with date range noted |
| Source trail cannot support current claims | Stale or unsupported claims remain after refresh attempt | Blocker for sensitive topics | Source steward | Fix by refreshing or removing claims |
| Stronger URL can absorb the useful material | `g-canonical` and consolidation review identify owner | Medium | SEO technical owner | Fix by recommending merge path |
| Decline is not solely tied to rumored update | `g-ranking-history` shows no confirmed matching event, or event context is caveated | Medium | Monitoring owner | Fix by removing speculation |
| Rollback owner is named | Advisory note states who can reverse the decision outside V1 | Blocker | Program owner | Pass when owner and cue are recorded |

## Pruning Handoff Rules

1. Send pages with remaining useful claims to [[Source Refresh Workflow]] before prune advice.
2. Send overlapping pages to [[Content Consolidation Rules]] before prune advice.
3. Send confirmed historical traffic questions to [[Historical Performance Review]] before prune advice.
4. Mark "no prune recommendation" when evidence is thin or the page has a retained reader role.

## Pruning Source IDs

`g-helpful-content`; `g-gsc-api`; `g-ranking-history`; `g-canonical`.

## Related

- [[Content Decay Detection]]
- [[Content Consolidation Rules]]
- [[Historical Performance Review]]
- [[Rewrite Rollback Notes]]
- [[Blog Quality Score]]
