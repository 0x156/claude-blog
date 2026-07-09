---
type: spoke
title: "Cluster Performance Score"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Cluster Performance Score

## Scoring Purpose

Use this note to judge whether a topic cluster is healthy enough to brief, refresh, or report on. The score is an editorial operating score, not a Google ranking model and not a traffic forecast.

### Criteria This Score Owns

The score owns coverage completeness, helpfulness, evidence freshness, link clarity, and visible outcome tracking. A cluster can score well only when the hub and spokes help readers complete distinct jobs. Source ID: `g-helpful-content`.

### Criteria Delegated Elsewhere

Query-page overlap belongs to [[Cannibalization Review]], owner selection belongs to [[Cluster Hub Selection]], and AI feature measurement belongs to [[Google Data Integrations]] when Search Console generative AI reports are available. Source ID: `g-genai-reports`.

## Score Evidence Table

| Criterion | Points | Required proof | Blocking failure | Source IDs |
|---|---:|---|---|---|
| Reader-job coverage | 25 | Hub and spokes map to distinct tasks | Multiple pages solve the same job | `g-helpful-content` |
| Evidence currency | 20 | Current source IDs and refresh dates on volatile claims | Undated Search or AI claim | `g-ai-opt-guide`; `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` |
| Link architecture | 20 | Hub-to-spoke, spoke-to-hub, and sibling anchors are intentional | Orphaned support page | `g-helpful-content` |
| Measurement readiness | 20 | GSC or generative AI reporting path named when available | Market stat treated as property data | `g-genai-reports`; `sparktoro-zero-click-2026` |
| Caveat discipline | 15 | No ranking, traffic, or AI inclusion promise | Unqualified forecast or guarantee | `sparktoro-zero-click-2026` |

## Review Procedure

1. Score only a named cluster, never a folder in the abstract.
2. Subtract points for missing evidence before adding points for polish.
3. Mark any criterion blocked when the evidence source is stale or outside the ledger.
4. Convert the total into one action: refresh, expand, consolidate, monitor, or escalate.
5. Record the weakest source type because that sets confidence for the whole score.

## Interpretation Bands

Use 85 to 100 for ready, 70 to 84 for refresh before scale, 50 to 69 for structural repair, and below 50 for consolidation or research. The zero-click source remains an `AS-REPORTED` market signal owned by [[AI Citation Mechanics]], so it should influence caveats more than scoring math.
