---
type: spoke
title: "Refresh Versus Rewrite Decision"
domain: "Blog Rewriting"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [rewriting, freshness, content-decay, active]
---

# Refresh Versus Rewrite Decision

## Decision Split Job

This note chooses between a targeted refresh and a deeper rewrite. A refresh preserves the article's core promise while updating evidence, examples, dates, links, or small structural gaps. A rewrite changes the answer architecture because the current page no longer satisfies the reader job.

`g-helpful-content` anchors the user-value question. `g-gsc-api` helps show whether the page is losing a small set of queries, a whole intent class, CTR, or visibility. `g-ranking-history` prevents a rewrite plan from leaning on unconfirmed update stories, and `g-canonical` keeps duplicate URL problems out of the editorial rewrite bucket.

### Signal Owned By This Decision

The decision owns action class, not diagnosis. It should receive inputs from [[Content Decay Detection]], [[Historical Performance Review]], [[Intent Drift Audit]], and [[Stale Claim Register]]. If those inputs are missing, the correct outcome is "not ready to decide."

### Boundary Between Refresh, Rewrite, Consolidate, And Prune

Choose refresh when the core article is sound. Choose rewrite when the page needs a new structure, reader promise, or evidence model. Choose consolidate when another URL should own the answer. Choose prune only after usefulness, data, source, and canonical checks have failed.

## Action Decision Table

| Candidate URL | Dominant signal | Source freshness | Action | Owner | Rollback note |
|---|---|---|---|---|---|
| Evergreen guide with outdated examples | Source age, small gaps | `g-helpful-content` and source review current | Refresh | Editor | Restore prior example if new source weakens clarity |
| Article losing one query group | Query mix shift, limited scope | `g-gsc-api` export tied to date range | Refresh section and heading promise | SEO strategist | Revert if target query relevance drops |
| Page no longer matches current reader job | Intent drift and structural mismatch | `g-helpful-content`; [[Intent Drift Audit]] | Rewrite | Content lead | Compare new outline to old job statement |
| Two pages cover one answer | Split signals or duplicate URL issue | `g-canonical`; `g-gsc-api` | Consolidate, not rewrite | SEO technical owner | Keep separate if intents prove distinct |
| Decline near confirmed rollout | Official update timing overlaps | `g-ranking-history` | Review cautiously, avoid causal claim | Monitoring owner | Remove update framing if evidence diverges |
| Page lacks usefulness and replacement value | Failed prune gate | `g-helpful-content`; [[Pruning Advisory Checklist]] | Prune recommendation for approval | Program owner | Restore if a retained reader job is found |

## Decision Procedure

1. Require a diagnosis note before selecting an action.
2. Identify the smallest change that can restore usefulness and source support.
3. Check whether the problem is editorial, source-related, technical, or measurement-related.
4. Assign one primary action and one fallback action.
5. Write the rollback cue in the same record as the recommendation.

## Decision Source IDs

`g-helpful-content`; `g-gsc-api`; `g-ranking-history`; `g-canonical`.

## Related

- [[Content Decay Detection]]
- [[Intent Drift Audit]]
- [[Content Consolidation Rules]]
- [[Pruning Advisory Checklist]]
- [[Rewrite Rollback Notes]]
