---
type: spoke
title: "Metric Export Schema"
status: active
created: 2026-07-06
updated: 2026-07-08
tags: [data-integrations, gsc, ga4, read-only, active]
domain: "Blog Data"
confidence: verified
related:
  - "[[Google Data Integrations]]"
  - "[[Credential Boundary Rules]]"
  - "[[Generative AI Performance Reporting]]"
  - "[[Missing Data Disclosure]]"
source_urls:
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
  - "https://support.google.com/webmasters/answer/16984139"
  - "https://support.google.com/webmasters/answer/7042828"
  - "https://developers.google.com/analytics/devguides/reporting/data/v1"
---

# Metric Export Schema

## Summary

Metric Export Schema defines the minimum columns needed for sanitized, read-only blog performance analysis.

Exports must be deterministic enough to compare over time and limited enough to avoid credentials or private user data.

## Required Common Columns

| Column | Required | Null allowed | Description |
|---|---|---|---|
| `export_id` | yes | no | Stable ID for the export batch. |
| `source_surface` | yes | no | One of `gsc_search`, `gsc_gen_ai_search`, `gsc_discover`, `ga4`, `url_inspection`, `crux`. |
| `export_method` | yes | no | One of `ui_export`, `api_export`, `manual_summary`, `sanitized_client_export`. |
| `property_label` | yes | no | Non-secret label for the property. |
| `date_start` | yes | no | ISO date. |
| `date_end` | yes | no | ISO date. |
| `retrieved_at` | yes | no | ISO date or timestamp of export. |
| `owner` | yes | no | Person or role that produced the export. |
| `confidence` | yes | no | `first-party`, `sampled`, `incomplete`, `advisory`, or `gap`. |
| `notes` | no | yes | Caveats, filters, missing data, or redactions. |

## GSC Search Columns

| Column | Required | Null allowed | Notes |
|---|---|---|---|
| `page_url` | yes | no | Canonical URL where available. |
| `query` | no | yes | Redact if query privacy is sensitive or omitted by export. |
| `country` | no | yes | ISO country or UI label. |
| `device` | no | yes | `desktop`, `mobile`, `tablet`, or blank. |
| `clicks` | yes | no | Numeric. |
| `impressions` | yes | no | Numeric. |
| `ctr` | yes | no | Decimal or percent, specify format in notes. |
| `average_position` | no | yes | Null when not provided or not meaningful. |

## AI Overview And AI Mode Columns

Google's 2026-06-03 announcement and Search Console Help describe subset-only generative AI reporting. Use UI-export language unless Google documents API parity.

| Column | Required | Null allowed | Notes |
|---|---|---|---|
| `source_surface` | yes | no | Use `gsc_gen_ai_search`. |
| `ai_surface` | yes | no | `ai_overviews`, `ai_mode`, `combined`, or `unknown`. |
| `page_url` | yes | no | Page dimension is supported in the Help docs. |
| `country` | no | yes | Supported dimension. |
| `device` | no | yes | Supported for Search results. |
| `date` | yes | no | Day, week, month, or hour if the UI export uses that granularity. |
| `impressions` | yes | no | Links shown in generative AI features. |
| `clicks` | no | yes | Null unless the export explicitly provides click data. |
| `ctr` | no | yes | Null unless computed from available click and impression fields. |
| `query` | no | yes | Do not infer query-level AI feature data unless the report exports it. |
| `export_method` | yes | no | Usually `ui_export` as of this note. |

## Missing Data Labels

- `gap`: report not available for the property.
- `incomplete`: available but filtered, sampled, truncated, redacted, or missing a required dimension.
- `advisory`: market or practitioner estimate, not first-party export.
- `first-party`: owner-provided export with retrieval date and fields intact.

## Related

- [[Google Data Integrations]]
- [[Credential Boundary Rules]]
- [[Generative AI Performance Reporting]]
- [[Missing Data Disclosure]]
