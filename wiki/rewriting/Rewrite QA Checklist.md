---
type: spoke
title: "Rewrite QA Checklist"
domain: "Blog Rewriting"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [rewriting, freshness, content-decay, active]
---

# Rewrite QA Checklist

## Rewrite QA Gate

Rewrite QA reviews a drafted change before it enters an editorial or publishing queue. It checks whether the rewrite preserved the approved reader job, updated dated claims, respected source limits, and kept technical handoffs visible.

`g-helpful-content` is the quality and usefulness source. `g-gsc-api` supplies the before-and-after measurement fields the analyst should preserve for later review. `g-ranking-history` controls update references, and `g-canonical` covers any canonical or duplicate URL note that the rewrite mentions.

### Checks Unique To Rewrite QA

This gate reviews the changed draft, not the old page. It asks whether the new structure improves the answer, whether removed sections were intentionally retired, whether source IDs still match the claims, and whether any technical recommendation is routed to the correct owner.

### Inputs Required Before QA

Bring the approved action decision, original page snapshot or excerpt, changed draft, claim list, source IDs, internal-link changes, affected URL, and measurement cue from [[Rewrite Rollback Notes]].

## Rewrite QA Pass Fail Table

| QA check | Evidence to inspect | Severity | Owner | Fix status |
|---|---|---|---|---|
| Reader job stayed intact or was deliberately changed | Approved decision note and rewritten intro | Blocker | Editor | Fix by aligning promise and headings |
| Updated claims have source IDs beside them | Claim list and source ledger IDs | Blocker | Source steward | Fix before approval |
| Rewrite does not invent update causality | Any Google update sentence checked against `g-ranking-history` | Blocker | Monitoring owner | Remove or caveat unsupported claims |
| Measurement baseline is preserved | `g-gsc-api` fields, date range, page filter | Medium | Analyst | Add baseline before handoff |
| Canonical or redirect language is only advisory | `g-canonical` cited beside technical note | Medium | SEO technical owner | Route to technical review |
| Removed content has a reason | Diff notes or editor annotation | Medium | Content lead | Restore, merge, or document removal |
| Rollback trigger is specific | [[Rewrite Rollback Notes]] entry | Blocker | Program owner | Add cue and review date |

## QA Exit Rules

1. Block the rewrite when a factual claim has no dated source ID.
2. Return the draft to the decision owner when the action no longer matches the approved plan.
3. Send canonical, redirect, and duplicate URL concerns to technical review rather than hiding them in prose.
4. Approve only with an explicit measurement window and rollback cue.

## QA Source IDs

`g-helpful-content`; `g-gsc-api`; `g-ranking-history`; `g-canonical`.

## Related

- [[Refresh Versus Rewrite Decision]]
- [[Source Refresh Workflow]]
- [[Rewrite Rollback Notes]]
- [[Stale Claim Register]]
- [[Blog Quality Score]]
