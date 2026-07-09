---
type: spoke
title: "Spoke Note Inventory"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Spoke Note Inventory

## Inventory Job

Use this note to list every support page attached to one cluster and mark each page as existing, missing, stale, duplicate, consolidated, or retired. The inventory is the source of truth before gap analysis, link mapping, or performance scoring begins.

### Required Fields

Each row needs page title, URL or note name, intended spoke job, canonical owner, source readiness, freshness state, internal link state, and next action. A page that lacks source-backed usefulness should not stay in the inventory just to increase coverage count. Source ID: `g-helpful-content`.

### Inventory Boundaries

Do not create AI-only spokes, llms.txt support pages, or thin pages for every query variant. The Google AI guidance and June 2026 clarification belong in [[2026 Google Update Timeline]] when a stakeholder asks for AI-file work. Source IDs: `g-ai-opt-guide`, `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`.

## Spoke Inventory Table

| Inventory state | Required inputs | Evidence state | Owner | Next action |
|---|---|---|---|---|
| Existing and healthy | Page title, role, sources, links | Useful content and current source IDs | Cluster editor | Keep and monitor |
| Existing but stale | Page role, expired source, affected claim | Needs source refresh before reuse | Source steward | Refresh or mark caveat |
| Missing but justified | Reader job, hub relationship, source availability | Advisory until evidence is attached | Content lead | Send to [[Cluster Gap Analysis]] |
| Duplicate or overloaded | Two pages share task or owner | Needs query-page and canonical review | SEO lead | Send to [[Cannibalization Review]] |
| Retired or consolidated | Old URL, replacement owner, link route | Requires rollback and redirect discussion outside this note | Human owner | Update inventory after approval |

## Inventory Procedure

1. Start with the hub and list all pages currently linked from it.
2. Add known pages that rank or receive impressions for cluster queries.
3. Mark each page's reader job before assigning a status.
4. Attach source IDs and note whether GSC evidence exists. Source ID: `g-gsc-api`.
5. Route market visibility context to [[AI Citation Mechanics]] instead of using `sparktoro-zero-click-2026` as a page-level forecast.

## Handoff Rules

The inventory is not a content calendar. It feeds [[Intent Coverage Matrix]], [[Internal Link Matrix]], and [[Cluster Performance Score]] after duplicates, missing evidence, and stale sources are visible.
