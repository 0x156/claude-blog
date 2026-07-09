---
type: spoke
title: "FLOW Rollback Notes"
domain: "Blog Workflow"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [flow, active]
confidence: advisory
related:
  - "[[FLOW Framework]]"
  - "[[FLOW Approval Queue]]"
  - "[[FLOW Rewrite Stage]]"
  - "[[FLOW Report Stage]]"
  - "[[Google Data Integrations]]"
---

# FLOW Rollback Notes

## Rollback Note Purpose

FLOW Rollback Notes attaches a review and reversal plan to recommendations that could affect live content, reporting, or stakeholder expectations. The note does not perform the rollback. It tells the human owner what signal would make the change suspect and what earlier state or alternate recommendation should be restored.

## Trigger Types Captured

Capture triggers for changed quality advice, AI Search caveats, source corrections, market-context assumptions, consolidation decisions, and pruning recommendations. `g-ai-opt-guide` supports rolling back unsupported Google AI file claims. `g-ranking-history` is the official route for confirmed update timing. `g-gsc-api` and `g-ga4-data` support property-specific observation windows when the owner supplies exported evidence.

## Rollback Step Table

| Change type | Input | Evidence required | Rollback trigger | Owner | Handoff |
|---|---|---|---|---|---|
| Usefulness rewrite | Approved rewrite note | Reader task and accepted source packet | Updated section reduces clarity or removes necessary proof | Editor | [[FLOW Review Stage]] |
| AI Search correction | Removed or changed AI tactic | `g-ai-opt-guide` | New official Google guidance changes the caveat | SEO lead | [[2026 Google Update Timeline]] |
| Property-data report note | GSC or GA4 planning caveat | `g-gsc-api`, `g-ga4-data` | First-party data shows a different planning constraint | Strategy owner | [[Google Data Integrations]] |
| Consolidation recommendation | Merge or redirect plan | Source map and property data | Important query, link, or reader segment is harmed | Content owner | [[FLOW Approval Queue]] |
| Pruning recommendation | Removal candidate and evidence | Traffic, links, source freshness | Business or search evidence proves retained value | Managing editor | [[FLOW Report Stage]] |

## Observation Window Rules

Set the observation window before implementation. Some changes need a source refresh date; others need a property-data check after enough impressions or engagement data exists. Use `g-ranking-history` only for confirmed Google update timing, not for client impact claims. If the owner cannot name a reasonable review signal, the change should remain advisory.

## Approval Attachment

Rollback notes attach to [[FLOW Approval Queue]] rows and appear in [[FLOW Report Stage]] only when the report asks someone to act. They should be short, specific, and reversible: what changed, who owns it, what signal matters, and what gets restored.
