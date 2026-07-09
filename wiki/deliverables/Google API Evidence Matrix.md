---
type: deliverable
title: "Google API Evidence Matrix"
domain: "Blog Content Brain"
status: active
created: 2026-07-09
updated: 2026-07-09
tags: [deliverables, data-integrations, evidence]
source_urls:
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
  - "https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect"
  - "https://developers.google.com/speed/docs/insights/v5/get-started"
  - "https://developers.google.com/analytics/devguides/reporting/data/v1"
---

# Google API Evidence Matrix

## Evidence Comparison Job

This matrix tells [[Google Data Integrations]] which exported fields can support a blog recommendation, which credentials would be needed outside the vault, and which surfaces are blocked because this ledger has no source ID for them. It is advisory and read-only. It never stores tokens, request headers, account IDs, or raw private exports. The source IDs wired here are `g-gsc-api`, `g-urlinspect`, `g-psi`, and `g-ga4-data`.

## Credential Tiers And Evidence Rows

Tier 0 means public documentation only. Tier 1 means a redacted export supplied by an operator. Tier 2 means live API access held outside the vault. V1 notes may describe Tier 2 requirements, but they do not perform the request.

## API Evidence Matrix

| Data surface | Credential tier | Accepted evidence | Decision it can support | Source state |
|---|---|---|---|---|
| GSC Search Analytics | Tier 1 or 2 | Clicks, impressions, CTR, position by query or page | Decay triage, query fit, cluster demand | `g-gsc-api` |
| URL Inspection | Tier 2 | Index state, canonical, rich result status | Indexing diagnosis and canonical review | `g-urlinspect` |
| PageSpeed Insights and CrUX | Tier 0 to 2 | Lighthouse lab data and available field data | Technical risk notes for page quality | `g-psi` |
| GA4 Data API | Tier 1 or 2 | Organic engagement and post-click behavior | Content usefulness review after the click | `g-ga4-data` |
| Natural Language API | Tier 2 | Entity extraction export if separately sourced | Entity audit only after ledger addition | Source ID missing |
| YouTube API | Tier 2 | Video metadata if separately sourced | Repurposing evidence, not blog ranking proof | Source ID missing |
| Keyword Planner | Tier 2 | Operator export with account caveats | Demand planning, never exact traffic promise | Source ID missing |
| Joined evidence view | Tier 1 | Page URL, canonical, query, engagement join | Recommendation confidence label | Uses all wired IDs |

## Interpretation Rules For Mixed API Evidence

First-party property exports outrank market averages for the property under review, but missing exports must be disclosed. GSC and GA4 answer different parts of the journey, so clicks and engagement should not be merged without a canonical URL key. URL Inspection evidence can explain index state for a specific URL, not the overall quality of the page. PSI can identify performance risk, but it should not replace editorial review through [[Blog Quality Score]].
