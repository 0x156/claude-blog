---
type: spoke
title: "FLOW Rewrite Stage"
domain: "Blog Workflow"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [flow, active]
confidence: advisory
related:
  - "[[FLOW Framework]]"
  - "[[FLOW Review Stage]]"
  - "[[FLOW Rollback Notes]]"
  - "[[Freshness and Content Decay]]"
  - "[[Google Data Integrations]]"
---

# FLOW Rewrite Stage

## Rewrite Stage Purpose

FLOW Rewrite Stage handles refresh, consolidation, expansion, pruning, and correction work without losing source or rollback discipline. A rewrite is not just a prettier draft. It is a controlled change to an existing content asset, usually because evidence, reader need, internal competition, or policy context has shifted.

## Entry Triggers For Refresh Work

Enter this stage when [[Freshness and Content Decay]] identifies stale information, when [[Google Data Integrations]] surfaces performance movement, when review finds thin or duplicated content, or when a source update changes the advice. Use `g-helpful-content` for usefulness and originality checks. Use `g-spam-policies` when scale, duplication, or low-value generated content shapes the rewrite. Use `g-ranking-history` for confirmed update timing and `g-ga4-data` for property engagement evidence.

## Rewrite Decision Table

| Rewrite trigger | Input | Evidence required | Action | Owner | Handoff |
|---|---|---|---|---|---|
| Stale people-first guidance | Existing page and brief | `g-helpful-content` plus source dates | Refresh explanation around current reader task | Editor | [[FLOW Review Stage]] |
| Unsupported AI Search tactic | Old recommendation | Current source packet and dated caveat | Remove or qualify the tactic | SEO lead | [[FLOW Factcheck Stage]] |
| Visibility planning change | Report cites property movement | `g-ga4-data` with scoped date range | Adjust distribution or measurement note | Strategy owner | [[FLOW Report Stage]] |
| Consolidation need | Overlapping pages or cannibalization note | Property evidence if available | Merge, redirect recommendation, or no-op note | Content owner | [[FLOW Approval Queue]] |
| Pruning candidate | Thin, outdated, or redundant page | `g-spam-policies`, traffic, link, and business context | Recommend prune only with rollback plan | Managing editor | [[FLOW Rollback Notes]] |

## Consolidation And Pruning Controls

The stage may recommend merging or pruning content, but it does not execute that change. When two notes or pages serve the same reader job and no distinct source-backed deliverable exists, prefer consolidation over padding. When evidence is weak, mark the decision advisory and ask for property data instead of substituting public market averages.

## Handoff And Rollback

Every rewrite plan exits with changed sections, removed claims, new source IDs, owner, review date, and rollback trigger. Live changes wait in [[FLOW Approval Queue]] and use [[FLOW Rollback Notes]] before implementation.
