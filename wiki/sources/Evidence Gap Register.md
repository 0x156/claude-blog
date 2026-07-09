---
type: spoke
title: "Evidence Gap Register"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [sources, research-pack, active]
domain: "Source Evidence"
confidence: verified
related:
  - "[[Research Pack Index]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Claim To Source Mapping]]"
  - "[[Current Requirements Digest]]"
  - "[[Source Confidence Labels]]"
  - "[[research-pack-2026-07-06|Research Pack 2026-07-06]]"
source_urls:
  - "https://developers.google.com/search/updates"
  - "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
  - "https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect"
  - "https://ai.google.dev/gemini-api/docs/image-generation"
  - "https://ai.google.dev/gemini-api/docs/imagen"
  - "https://c2pa.org/"
---

# Evidence Gap Register

## Summary

This register holds evidence problems that would otherwise leak into recommendations as overconfident claims. A gap is closed only when the affected source, date, claim, and note path are fixed in the relevant machine or wiki layer.

The wiki can document a real source inside the owned path, but release-grade evidence still needs `references/source-ledger.json` and raw-source provenance outside this edit scope.

## Open Gaps

| Gap ID | Gap | Owner | Due | Affected notes | Severity | Blocking rule |
|---|---|---|---:|---|---|---|
| GAP-2026-07-09-01 | Source ledger needs separate `published`, `last_updated`, `retrieved`, `event_date`, and `date_precision` fields for Google documentation pages that currently mix page dates and event dates. | source steward | 2026-07-16 | [[research-pack-2026-07-06|Research Pack 2026-07-06]], [[Claim To Source Mapping]], [[Current Requirements Digest]] | blocker | Blocks release-grade citation integrity. |
| GAP-2026-07-09-02 | `g-product-sd` is date-mismatched: the live Product intro page shows last updated 2025-12-10, while the July 7 change is on Search docs updates and merchant listing documentation. | source steward | 2026-07-16 | [[research-pack-2026-07-06|Research Pack 2026-07-06]], [[Structured Data Deprecation Register]], [[Product Mentions In Blog Schema]] | blocker | Blocks trustworthy ecommerce schema guidance. |
| GAP-2026-07-09-03 | July 1 AMP documentation update has a real Google source but no machine-ledger source ID or raw snapshot in this edit scope. | source steward | 2026-07-16 | [[2026 Google Update Timeline]], [[Google Algorithm Update Ledger]], [[Current Requirements Digest]] | high | Blocks release claims that the ledger is current through July 2026. |
| GAP-2026-07-09-04 | Preferred Sources 2026-05-27 AI Mode and AI Overviews availability has a real Google source but no dedicated ledger source ID in this edit scope. | source steward | 2026-07-16 | [[2026 Google Update Timeline]], [[AI Citation Mechanics]], [[Distribution and Repurposing]] | high | Blocks source-ID completeness for AI distribution guidance. |
| GAP-2026-07-09-05 | HowTo rich result deprecation is sourced to Google Search Central, but the source is not yet represented as a machine-ledger source ID. | schema steward | 2026-07-16 | [[Structured Data Deprecation Register]], [[Blog Schema Stack]], [[Quality Score Rubric]] | medium | Blocks a fully auditable deprecated-schema register. |
| GAP-2026-07-09-06 | Search Console Search Analytics and URL Inspection API scope claims are sourced to official docs, but exact API pages need machine-ledger entries. | data steward | 2026-07-16 | [[Credential Boundary Rules]], [[Metric Export Schema]], [[Read Only Data Access Pattern]] | medium | Blocks verified credential-boundary source IDs. |
| GAP-2026-07-09-07 | Search Console generative AI report Help Center pages need ledger entries for subset availability, dimensions, UI export behavior, and API caveats. | data steward | 2026-07-16 | [[Google Data Integrations]], [[Metric Export Schema]], [[Generative AI Performance Reporting]] | high | Blocks API-equivalent export claims. |
| GAP-2026-07-09-08 | Gemini image generation, Nano Banana model families, SynthID, Imagen shutdown, and C2PA sources need machine-ledger entries and raw snapshots. | media steward | 2026-07-23 | [[Generated Media Disclosure Notes]], [[Images Audio and Charts]] | medium | Blocks model-specific media guidance from being release-verified. |
| GAP-2026-07-09-09 | Raw provenance remains incomplete outside owned paths, while wiki notes cite live URLs and source pools. | release owner | 2026-07-23 | [[Research Pack Index]], [[Source Ledger Reading Guide]], [[Research Release Gate Notes]] | blocker | Blocks immutable evidence claims and market-ready release. |
| GAP-2026-07-09-10 | The relationship map generator lives outside owned paths and still hard-codes a generic SVG. This pass replaces the attachment only. | vault maintainer | 2026-07-23 | [[dashboard]], [[overview]], [[index|Index]] | medium | Blocks repeatable graph generation until the script is fixed. |

## Triage Rules

| Severity | Meaning | Allowed use before closure |
|---|---|---|
| blocker | The gap can make release claims, maturity gates, or source integrity false. | Use only as a named blocker. Do not use in release claims. |
| high | The gap can make current operating guidance stale or incomplete. | Use with explicit caveat and refresh trigger. |
| medium | The source is real, but ledger, raw provenance, or scope detail is incomplete. | Use in advisory wiki guidance, not as a release-verified claim. |
| low | Navigation, hygiene, or presentation issue that does not change claim truth. | Fix opportunistically. |

## Closure Checklist

- Add or correct the machine-ledger entry outside this owned path.
- Capture immutable raw source material and hash it when the release gate requires raw provenance.
- Update [[Claim To Source Mapping]] with the final source ID and date fields.
- Update affected operating notes and remove `pending:` source IDs.
- Run `python3 scripts/lint_vault.py` and any broader release audit requested by the owner.

## Related

- [[Research Pack Index]]
- [[Claim To Source Mapping]]
- [[Current Requirements Digest]]
- [[Source Confidence Labels]]
- [[research-pack-2026-07-06|Research Pack 2026-07-06]]
