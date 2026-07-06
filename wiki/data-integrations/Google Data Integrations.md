---
type: hub
title: "Google Data Integrations"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [data-integrations, gsc, ga4, active]
domain: "Blog Data"
confidence: verified
related:
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Dual Optimization]]"
  - "[[Freshness and Content Decay]]"
  - "[[AI Citation Mechanics]]"
  - "[[Semantic Topic Clusters]]"
  - "[[Blog Quality Score]]"
  - "[[Research Pack Index]]"
source_urls:
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
  - "https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect"
  - "https://developers.google.com/analytics/devguides/reporting/data/v1"
  - "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
  - "https://developers.google.com/search/docs/fundamentals/third-party-seo"
---

# Google Data Integrations

## Summary

Google Data Integrations defines how GSC, URL Inspection, GA4, and related APIs inform blog planning and audits.

This hub is read-only and does not grant credentials, mutate properties, or fetch private data in V1.

## Current fact anchors

- Search Console Search Analytics API documentation, retrieved 2026-07-06, covers clicks, impressions, CTR, and position by query dimensions.
- URL Inspection API documentation, retrieved 2026-07-06, covers index status, coverage, and rich-results state per URL.
- GA4 Data API documentation, retrieved 2026-07-06, covers organic traffic and engagement reporting.
- Search Console generative AI performance reports were announced by Google on 2026-06-03 for AI Overviews and AI Mode reporting on a subset of properties.
- Google third-party SEO guidance, 2026-06-05, says third-party tools do not access Google's internal ranking systems.

## Scope

- Define approved data sources.
- Define required credential boundaries.
- Define read-only query patterns.
- Define metrics for [[Freshness and Content Decay]].
- Define query and page inputs for [[Semantic Topic Clusters]].
- Define AI feature reporting inputs for [[AI Citation Mechanics]].
- Define quality score evidence for [[Blog Quality Score]].
- Define missing-data language.

## Future spoke notes

- [[GSC Search Analytics Query Plan]]
- [[URL Inspection Evidence Plan]]
- [[GA4 Blog Engagement Metrics]]
- [[Generative AI Performance Reporting]]
- [[First Party Versus Market Data]]
- [[Query Dimension Hygiene]]
- [[Page URL Canonical Data Checks]]
- [[Credential Boundary Rules]]
- [[Data Confidence Labels]]
- [[Missing Data Disclosure]]

## Metric families

- Impressions.
- Clicks.
- CTR.
- Average position.
- AI Overview impressions when available.
- AI Mode impressions when available.
- Landing page engagement.
- Freshness deltas.
- Query overlap.
- Index and rich-results state.

## Source posture

- Prefer first-party Google data when the site has access.
- Use market studies only as context for absent property data.
- Do not store credentials in notes.
- Do not run mutations or submissions from V1.
- Make missing API access explicit.

## Related themes

- [[Dual Optimization]]
- [[Freshness and Content Decay]]
- [[AI Citation Mechanics]]
- [[Semantic Topic Clusters]]
- [[Distribution and Repurposing]]
- [[Blog Quality Score]]
- [[Google Algorithm Update Ledger]]
- [[Research Pack Index]]

## Sources

- Search Console Search Analytics API, retrieved 2026-07-06.
- URL Inspection API, retrieved 2026-07-06.
- GA4 Data API, retrieved 2026-07-06.
- Search Console generative AI reports, 2026-06-03.
- Google third-party SEO guidance, 2026-06-05.

## Next actions

- Fill [[Credential Boundary Rules]] before any importer work.
- Fill [[Generative AI Performance Reporting]] before AI feature reports.
- Link metric confidence to [[Blog Quality Score]].
