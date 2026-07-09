---
type: spoke
title: "Credential Boundary Rules"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [data-integrations, gsc, ga4, read-only, active]
domain: "Blog Data"
confidence: verified
related:
  - "[[Google Data Integrations]]"
  - "[[Metric Export Schema]]"
  - "[[Read Only Data Access Pattern]]"
  - "[[Missing Data Disclosure]]"
  - "[[Data Confidence Labels]]"
source_urls:
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
  - "https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect"
  - "https://developers.google.com/analytics/devguides/reporting/data/v1"
  - "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
  - "https://developers.google.com/search/docs/fundamentals/third-party-seo"
---

# Credential Boundary Rules

## Summary

Credential Boundary Rules define what may enter the vault when GSC, URL Inspection, GA4, CrUX, or reporting exports support a blog audit.

The vault is read-only. It stores recommendations and sanitized exports, never live credentials.

## Hard Boundaries

| Boundary | Rule | Failure action |
|---|---|---|
| Secrets | Do not store API keys, OAuth tokens, cookies, service-account JSON, refresh tokens, client secrets, `.env` files, or browser session exports. | Reject the import, delete the artifact from working memory, and record a gap without the secret value. |
| Private data | Do not store raw user identifiers, emails, form submissions, paid customer lists, or private query logs. | Redact before import or keep the evidence outside the vault. |
| Scopes | Prefer read-only scopes when data is exported for analysis. Search Console Search Analytics and URL Inspection support `https://www.googleapis.com/auth/webmasters.readonly`; full `webmasters` is accepted by the APIs but is not the preferred vault evidence path. | If write-capable scopes are present, block the export and request a read-only export or a sanitized UI export. |
| Paths | Do not write absolute local paths into wiki notes or reports. | Replace with vault-relative paths or source IDs. |
| External systems | Do not submit URLs, mutate Search Console settings, change CMS fields, edit GA4, or update sitemaps from this vault. | Convert the action into an approval note with rollback conditions. |

## API Boundary Table

| Source | Official capability | Read-only boundary | Vault note |
|---|---|---|---|
| Search Analytics API | Queries Search traffic data, groups by dimensions, and returns rows with clicks, impressions, CTR, and position. Google documents that the API is bounded by Search Console limits and does not guarantee all rows. | Use `webmasters.readonly` when possible; store only sanitized exports or aggregate summaries. | Do not present API output as complete query truth. |
| URL Inspection API | Inspects the indexed status of a URL under a Search Console property. Google states it shows the version in the Google index and cannot test live indexability. | Use `webmasters.readonly` when possible; inspect only URLs owned by the property. | Do not use this vault to request indexing or mutate URL state. |
| GA4 Data API | Programmatically accesses Analytics report data and respects the property reporting identity settings. | Use exports that exclude user-level identifiers and private event payloads. | GA4 evidence supports engagement analysis, not Search query evidence. |
| Search Console generative AI reports | Google announced AI Overviews and AI Mode reporting for some properties. | Treat availability as property-specific and UI/API-scope-sensitive until exact export routes are documented in the ledger. | Missing reports get a missing-data note, not an estimate. |

## Approved Evidence Shapes

| Evidence | Allowed fields | Disallowed fields | Confidence |
|---|---|---|---|
| GSC Search Analytics export | Property label, date range, page, query, country, device, clicks, impressions, CTR, average position, export timestamp. | Tokens, account email, OAuth metadata, hidden rows copied from UI. | first-party when export owner and date are recorded. |
| URL Inspection evidence | Canonical URL, index status, crawl time, page fetch state, rich result state, inspection timestamp. | Credentials, live API request payload with auth headers. | first-party for inspected URL only. |
| GA4 export | Landing page, channel grouping, sessions, engaged sessions, engagement rate, conversions if already sanitized, date range. | User IDs, client IDs, transaction PII, raw event payloads. | first-party but not a replacement for Search query data. |
| Generative AI report export | Page, country, device, date, impressions, surface, export timestamp. | Unsupported query-level claims or API-equivalent claims unless Google documents them. | first-party when the property has the report. |

## Redaction Standard

- Replace account names with stable labels such as `property_a` when client confidentiality matters.
- Keep query strings only when the owner confirms they are safe to store.
- Remove URL parameters that expose campaign secrets, emails, IDs, or draft tokens.
- Store aggregate metrics, not row-level user behavior.
- Add a missing-data note when redaction removes a field needed for analysis.

## Export Handling

1. Confirm the source owner and read-only basis.
2. Verify the export date range, property, and canonical URL handling.
3. Scan filenames and content for secrets before adding source notes.
4. Store only sanitized summaries in wiki notes.
5. Record unavailable fields in [[Missing Data Disclosure]].

## Source Notes

- Search Analytics API, last updated 2026-05-20, retrieved 2026-07-09: https://developers.google.com/webmaster-tools/v1/searchanalytics/query
- URL Inspection API, last updated 2024-07-23, retrieved 2026-07-09: https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect
- GA4 Data API overview, retrieved 2026-07-09: https://developers.google.com/analytics/devguides/reporting/data/v1
- Search Console generative AI reports announcement, published 2026-06-03, retrieved 2026-07-09: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports

## Related

- [[Google Data Integrations]]
- [[Metric Export Schema]]
- [[Read Only Data Access Pattern]]
- [[Missing Data Disclosure]]
