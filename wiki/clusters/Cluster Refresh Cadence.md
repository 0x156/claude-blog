---
type: spoke
title: "Cluster Refresh Cadence"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Cluster Refresh Cadence

## Cadence Owner

This note sets review timing for a cluster's hub, spokes, links, evidence, and outcome metrics. It prevents a cluster from looking complete while its source posture or internal links quietly decay.

### Event Driven Refreshes

Refresh immediately when Google changes relevant Search guidance, a cluster page loses its canonical role, a source ID passes its refresh window, or first-party data contradicts a recommendation. The official ranking-history source is for confirmed Google rollout status, not third-party impact analysis. Source ID: `g-ranking-history`.

### Scheduled Refreshes

For stable clusters, use a monthly source scan, quarterly link and intent review, and annual hub rewrite review. Faster cadence is justified for YMYL, volatile AI guidance, or pages that inform revenue decisions. Source IDs: `g-helpful-content`, `g-ai-opt-guide`.

## Refresh Timing Table

| Asset or signal | Normal cadence | Triggered cadence | Evidence to check | Source IDs |
|---|---|---|---|---|
| Hub page | Quarterly | Major Search guidance change or cannibalization flag | Reader promise, source dates, spoke map | `g-helpful-content`; `g-ranking-history` |
| Spoke page | Quarterly to semiannual | Query shift, stale claim, or duplicate intent | Intent fit and cited source freshness | `g-helpful-content` |
| AI guidance caveat | Monthly | Google updates AI optimization wording | llms.txt and special-file language | `g-ai-opt-guide`; `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` |
| Market context | Monthly while volatile | New zero-click or AI visibility study | Caveats in [[AI Citation Mechanics]] | `sparktoro-zero-click-2026` |
| Internal links | Quarterly | Hub, URL, or owner changes | Anchor, direction, and destination | `g-helpful-content` |

## Cadence Runbook

1. Open [[Research Pack Index]] and list source IDs whose refresh date is due.
2. Check whether [[2026 Google Update Timeline]] changes the cluster's assumptions.
3. Inspect hub and spoke anchors for stale ownership language.
4. Compare recent property data with the prior review period when available.
5. Assign each page keep, refresh, consolidate, monitor, or source-needed.

## Staleness Signals

A cluster is stale when it cites outdated Search guidance, uses a market study as if it were property evidence, or still points readers to a page whose intent has changed. Cadence is a risk control, not a license to rewrite pages on a calendar when no evidence changed.
