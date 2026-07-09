---
type: spoke
title: "Claim To Source Mapping"
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
  - "[[Google Algorithm Update Ledger]]"
  - "[[Google Data Integrations]]"
  - "[[Source Confidence Labels]]"
  - "[[Evidence Gap Register]]"
  - "[[research-pack-2026-07-06|Research Pack 2026-07-06]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/updates"
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
  - "https://developers.google.com/search/docs/appearance/preferred-sources"
  - "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing"
  - "https://developers.google.com/search/blog/2023/08/howto-faq-changes"
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
  - "https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect"
  - "https://ai.google.dev/gemini-api/docs/image-generation"
---

# Claim To Source Mapping

## Summary

This spoke is the release-review surface for wiki claims. A claim can enter a brief, audit, scorecard, or delivery note only when this table or the machine ledger can show the claim, note path, source ID, URL, retrieval date, confidence, and refresh trigger.

The machine ledger remains `references/source-ledger.json`. This wiki note does not upgrade missing ledger entries. It names them as `pending:` records and routes them to [[Evidence Gap Register]].

## Active Claim Map

| Claim | Note path | Source ID | URL | Retrieved | Confidence | Refresh trigger |
|---|---|---|---|---:|---|---|
| Google Search does not require special AI files, AI-only schema, Markdown conversion, forced chunking, or llms.txt for generative AI Search visibility. | `wiki/geo-aeo/AI Citation Mechanics.md` | `g-ai-opt-guide`; `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 2026-07-09 | verified | AI optimization guide or Search docs updates change this guidance. |
| The AI optimization guide page date is 2026-06-29; 2026-06-15 is the docs-update event for the llms.txt clarification. | `wiki/geo-aeo/AI Citation Mechanics.md` | `g-ai-opt-guide`; `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | 2026-07-09 | verified, ledger-date repair needed | Ledger stores page `last_updated` and changelog `event_date` separately. |
| The Search Status Dashboard shows no confirmed ranking incident after the 2026-06-24 spam update as of 2026-07-09. | `wiki/monitoring/Google Algorithm Update Ledger.md` | `g-status-dashboard`; `g-update-2026-06-24-june-2026-spam-update` | https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history | 2026-07-09 | verified | Status dashboard adds a new ranking incident. |
| July 1 Search Central docs update removed outdated AMP viewer, AMP Cache, and signed exchange maintenance references from AMP guidance. | `wiki/monitoring/2026 Google Update Timeline.md` | `pending:g-search-docs-updates-2026-07-01-amp` | https://developers.google.com/search/updates#july-2026 | 2026-07-09 | verified, pending ledger entry | AMP docs or Search docs updates change after 2026-07-01. |
| July 7 Search Central docs update added merchant listing guidance for `Product.category` and sale-price effective dates. | `wiki/monitoring/2026 Google Update Timeline.md` | `g-search-docs-updates-2026-07-07-product-structured-data` | https://developers.google.com/search/updates#july-2026 | 2026-07-09 | verified | Merchant listing docs or Search docs updates change after 2026-07-07. |
| Merchant listing `Product.category` accepts `Text` or `CategoryCode` values and can include multiple category values. | `wiki/schema/Structured Data Deprecation Register.md` | `pending:g-merchant-listing` | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing | 2026-07-09 | verified, pending ledger entry | Merchant listing supported-property table changes. |
| The machine ledger currently assigns 2026-07-07 to `g-product-sd`, but the live Product intro page shows last updated 2025-12-10; the July 7 event belongs to merchant listing documentation. | `wiki/sources/research-pack-2026-07-06.md` | `g-product-sd`; `g-search-docs-updates-2026-07-07-product-structured-data`; `pending:g-merchant-listing` | https://developers.google.com/search/docs/appearance/structured-data/product | 2026-07-09 | gap | Ledger is corrected with page-specific dates and URLs. |
| FAQ rich results retired for all sites effective 2026-05-07; FAQ docs removal on 2026-06-15 is a separate documentation event. | `wiki/schema/Structured Data Deprecation Register.md` | `g-update-2026-05-07-faq-rich-results-retired`; `g-faqpage-sd` | https://developers.google.com/search/updates#deprecating-the-faq-rich-result-feature | 2026-07-09 | verified | FAQPage docs, Search Console API, or Search docs updates change status. |
| HowTo rich results are deprecated in Google Search as of 2023-09-13 and should not be scored as a current blog rich-result tactic. | `wiki/schema/Structured Data Deprecation Register.md` | `pending:g-howto-rich-result-deprecated` | https://developers.google.com/search/blog/2023/08/howto-faq-changes | 2026-07-09 | verified, pending ledger entry | Google restores HowTo or adds a replacement feature. |
| Search Analytics API uses `webmasters.readonly` or `webmasters`, is bounded by Search Console limits, and can group by dimensions such as country, device, page, query, date, and search appearance. | `wiki/data-integrations/Credential Boundary Rules.md` | `pending:gsc-searchanalytics-api` | https://developers.google.com/webmaster-tools/v1/searchanalytics/query | 2026-07-09 | verified, pending ledger entry | Search Analytics API scopes, dimensions, or limits change. |
| URL Inspection API can inspect indexed status for a URL under a property but cannot test live indexability. | `wiki/data-integrations/Credential Boundary Rules.md` | `pending:gsc-url-inspection-api` | https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect | 2026-07-09 | verified, pending ledger entry | URL Inspection API response scope changes. |
| Gemini image docs list Nano Banana model families, require rights for uploaded images, state generated images include SynthID watermarking, and say Imagen models shut down on 2026-08-17. | `wiki/media/Generated Media Disclosure Notes.md` | `pending:google-ai-gemini-image-generation`; `pending:google-ai-imagen-deprecation` | https://ai.google.dev/gemini-api/docs/image-generation | 2026-07-09 | verified, pending ledger entry | Google AI image docs, model IDs, SynthID language, or deprecation dates change. |
| Passage length and source-proximity tactics are practitioner heuristics, not official Google requirements. | `wiki/geo-aeo/Passage Citability Checklist.md` | `ziptie-aio-source-selection` | https://ziptie.dev/blog/google-ai-overviews-source-selection/ | 2026-07-08 | practitioner | Practitioner source changes or Google publishes contrary guidance. |

## Claim Intake Procedure

1. Quote the operational claim exactly as it will appear in the recommendation.
2. Prefer a current official, primary, standards, government, regulator, API, or first-party source when one exists.
3. Record one source row per claim. Do not reuse one date across unrelated pages.
4. Split `published`, `last_updated`, `event_date`, and `retrieved` in [[research-pack-2026-07-06|Research Pack 2026-07-06]] when the machine ledger cannot yet represent the distinction.
5. Use `pending:` source IDs only when the source is real but the ledger cannot be edited in this slice.
6. Send every `pending:` or `gap` source to [[Evidence Gap Register]] before the claim is used in release-critical material.
7. Downgrade confidence when the claim stretches beyond the source coverage.

## Release Blockers From This Map

| Blocker | Why it matters | Owning note |
|---|---|---|
| Pending source IDs remain for AMP, Preferred Sources, merchant listing, HowTo, Google API docs, Google AI image docs, Imagen shutdown, and C2PA. | Wiki notes can be useful, but release-grade source evidence must also exist in `references/source-ledger.json`. | [[Evidence Gap Register]] |
| `g-product-sd` has a live page-date mismatch. | Product intro and merchant listing documentation are separate pages; mixing them hides the July 7 change scope. | [[research-pack-2026-07-06|Research Pack 2026-07-06]] |
| Raw source snapshots are incomplete outside this edit scope. | Source URLs alone do not satisfy the immutable provenance gate. | [[Research Release Gate Notes]] |

## Related

- [[Research Pack Index]]
- [[Evidence Gap Register]]
- [[Source Confidence Labels]]
- [[research-pack-2026-07-06|Research Pack 2026-07-06]]
- [[Google Algorithm Update Ledger]]
- [[Current Requirements Digest]]
