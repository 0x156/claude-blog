---
type: spoke
title: "Citation Exposure Metrics"
domain: "GEO and AEO"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [geo-aeo, ai-citation, evergreen]
---

# Citation Exposure Metrics

## Citation Exposure Metrics Measurement Scope

This note defines what can be measured when a blog team asks whether content appears in AI answer surfaces. It separates directly available property data from manually observed citations and from market context. Google documentation is the basis for how AI features and preview controls are understood (`g-ai-features`, `g-ai-opt-guide`). Search Console generative AI performance reporting, when available to the property, is the preferred evidence lane (`g-genai-reports`).

The Google `llms.txt` clarification (`g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`) is included because a file request is not a metric for Google Search visibility. `blog-io2026` is useful for product-scale context, but it should not be used as a KPI target.

### Metrics This Note Counts

Count impressions, clicks, query, page, surface label, observed citation presence, citation URL, date, locale, and device when the data source can provide them.

### Metrics This Note Refuses

Do not count "AI optimized" badges, llms.txt existence, unverified screenshots, or generic AI traffic estimates as citation exposure.

## Citation Exposure Metrics Table

| Metric | Accepted source | Source IDs | Evidence state | Owner | Reporting action |
|---|---|---|---|---|---|
| AI feature impressions | Search Console generative AI report if enabled | `g-genai-reports`, `g-ai-features` | CONFIRMED feature reporting for eligible properties | Analyst | Export with date range and filters |
| Observed citation | Manual SERP or assistant capture with URL and date | `g-ai-features`, `blog-io2026` | Observation, not guaranteed repeatability | GEO reviewer | Store query, locale, device, and screenshot reference |
| Preview-control exposure risk | Snippet setting and page rule | `g-ai-opt-guide`, `g-ai-features` | Official guidance context | Technical SEO | Link to [[AI Feature Preview Controls]] |
| llms.txt request | File exists or stakeholder asks for one | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | CONFIRMED no Google Search visibility effect | Researcher | Report as caveat, not KPI |

## Citation Exposure Metrics Procedure

1. Choose the surface before exporting or sampling.
2. Label the evidence as first-party, official documentation, observation, market study, or unsupported.
3. Keep AI Overview and AI Mode rows separate even when the same URL appears.
4. Add "not available" instead of substituting third-party market data for property reporting.
5. Escalate trend claims to [[Google Data Integrations]] when GSC or GA4 exports are needed.

## Citation Exposure Metrics Review Loop

Refresh this note when `g-genai-reports` changes, when the property gains or loses access to the report, or when [[2026 Google Update Timeline]] records a relevant Google Search documentation update.
