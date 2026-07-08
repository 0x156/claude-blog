---
type: spoke
title: "Generative AI Performance Reporting"
status: active
created: 2026-07-06
updated: 2026-07-08
tags: [data-integrations, gsc, ga4, read-only, active]
domain: "Blog Data"
confidence: verified
related:
  - "[[Google Data Integrations]]"
  - "[[Metric Export Schema]]"
  - "[[Credential Boundary Rules]]"
  - "[[Missing Data Disclosure]]"
  - "[[AI Citation Mechanics]]"
source_urls:
  - "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
  - "https://support.google.com/webmasters/answer/16984139"
  - "https://support.google.com/webmasters/answer/7042828"
---

# Generative AI Performance Reporting

## Summary

This spoke records how to use Search Console generative AI reports for AI Overviews and AI Mode when a property has access.

Use this note only for read-only analysis. It does not change the Search generative AI control or any Search Console setting.

## Verified Availability

| Question | Current answer |
|---|---|
| Who has the report? | A subset of website owners during rollout. |
| Which Search surfaces are included? | AI Overviews and AI Mode. |
| Which dimensions are documented? | Pages, countries, dates, and devices for Search. |
| Which metric is required in this vault? | Impressions. |
| Are Search Labs experiments included? | No, Search Console Help excludes Search Labs experiment data. |
| Is API export supported? | Not claimed here. Use UI export unless Google publishes API support. |
| What if values export as `~` or `-`? | Search Console Help says downloaded values may become zeros, so record this caveat. |

## Review Sequence

1. Confirm the property has the generative AI Search report.
2. Export only sanitized UI data or record that no report is available.
3. Identify whether the row represents AI Overviews, AI Mode, a combined view, or an unknown UI grouping.
4. Preserve page, country, device, date, impressions, export date, and property label.
5. Do not infer query-level AI metrics from ordinary Search Analytics.
6. Compare with classic GSC Search Analytics and GA4 only after canonical URL alignment.
7. Label missing reports as `gap` and market-only context as `advisory`.

## Output Fields

| Field | Required | Notes |
|---|---|---|
| `property_label` | yes | Non-secret label. |
| `ai_surface` | yes | `ai_overviews`, `ai_mode`, `combined`, or `unknown`. |
| `page_url` | yes | Canonical page when the UI provides it. |
| `country` | no | Use only if exported. |
| `device` | no | Use only if exported. |
| `date` | yes | Preserve UI granularity. |
| `impressions` | yes | Required metric. |
| `clicks` | no | Null unless exported. |
| `ctr` | no | Null unless exported or computed from exported clicks and impressions. |
| `confidence` | yes | `first-party`, `incomplete`, `gap`, or `advisory`. |

## Related

- [[Google Data Integrations]]
- [[Metric Export Schema]]
- [[Credential Boundary Rules]]
- [[Missing Data Disclosure]]
- [[AI Citation Mechanics]]
