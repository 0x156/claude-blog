---
type: spoke
title: "Source Refresh Workflow"
domain: "Blog Rewriting"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [rewriting, freshness, content-decay, active]
---

# Source Refresh Workflow

## Source Refresh Stage Purpose

Source refresh replaces or revalidates evidence before a page is refreshed or rewritten. It is a source-steward workflow, not a prose-polish step. The output should make clear which claims are confirmed, caveated, removed, or escalated.

`g-helpful-content` supports the requirement that content be reliable and useful to readers. `g-gsc-api` can identify which pages or queries make a claim worth prioritizing when property data exists. `g-ranking-history` is the official path for ranking-update dates, and `g-canonical` supplies the technical evidence path when a source refresh reveals duplicate URL or canonical issues.

### Trigger And Entry Criteria

Start this workflow when a claim has an aging source, a Google policy reference, a dated statistic, a page-level traffic dependency, a source-ledger gap, or a rewrite request that changes the evidence basis. Do not start it just to decorate a draft with more citations.

### Output Artifact And Exit Criteria

The exit artifact is a claim-level source record with source ID, retrieval date, confidence, limitation, and recommended prose treatment. It is complete when each claim has one of four outcomes: keep with citation, update with newer source, remove, or route to approval.

## Source Refresh Step Table

| Step | Input | Evidence required | Action | Owner | Handoff |
|---|---|---|---|---|---|
| Inventory claims | Draft or live page section | Claim text, current source ID, date | Split compound claims into reviewable rows | Source steward | [[Stale Claim Register]] |
| Check source fit | Source ledger record | `g-helpful-content` quality lens | Mark whether source proves the claim | Editor | Keep, caveat, or replace |
| Prioritize by page value | Candidate page and query context | `g-gsc-api` if available | Refresh high-impact claims first | Analyst | [[Decay Segment Prioritization]] |
| Verify update references | Google update statement | `g-ranking-history` | Replace rumor language with dated official context | Monitoring owner | [[Google Algorithm Update Ledger]] |
| Route duplicate URL evidence | Claim tied to alternate URLs | `g-canonical` | Move URL signal questions to consolidation review | SEO technical owner | [[Content Consolidation Rules]] |
| Close the source record | Reviewed claim row | Source ID, date, confidence, limitation | Mark keep, update, remove, or escalate | Source steward | [[Rewrite QA Checklist]] |

## Control Points

1. Do not cite a source unless it proves the sentence beside it.
2. Keep old source IDs in the review trail when removing or replacing a claim.
3. Record the source limitation before drafting new prose.
4. Escalate contested or high-risk claims to [[Research Pack Index]] instead of smoothing over uncertainty.

## Source Refresh IDs

`g-helpful-content`; `g-gsc-api`; `g-ranking-history`; `g-canonical`.

## Related

- [[Stale Claim Register]]
- [[Rewrite QA Checklist]]
- [[Research Pack Index]]
- [[Google Data Integrations]]
- [[Content Consolidation Rules]]
