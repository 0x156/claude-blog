---
type: spoke
title: "Current Requirements Digest"
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
  - "[[Evidence Gap Register]]"
  - "[[Source Confidence Labels]]"
  - "[[Google Algorithm Update Ledger]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/updates"
  - "https://developers.google.com/search/docs/appearance/preferred-sources"
  - "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing"
  - "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
  - "https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect"
  - "https://ai.google.dev/gemini-api/docs/image-generation"
---

# Current Requirements Digest

## Summary

This digest names the current operating requirements that affect blog briefs, audits, schema reviews, data exports, AI-citation work, and generated media review as of the 2026-07-09 official-source check.

It is a routing note, not a substitute for `references/source-ledger.json`. Requirements with `pending:` source IDs are usable as advisory wiki guidance but remain release-blocked until the machine ledger and raw provenance are repaired.

## Requirements Table

| Requirement ID | Requirement | Affected workflows | Source ID | Current as of | Confidence | Refresh trigger |
|---|---|---|---|---:|---|---|
| REQ-GOOGLE-AI-001 | Use SEO foundations for Google generative AI features; do not require special AI files, AI-only schema, Markdown conversion, forced chunking, or inauthentic mentions. | [[AI Citation Mechanics]], [[Passage Citability Checklist]], [[6-Pillar Dual Optimization]] | `g-ai-opt-guide` | 2026-07-09 | verified | AI optimization guide changes. |
| REQ-GOOGLE-AI-002 | Treat llms.txt as unused by Google Search. It may exist for non-Google systems but is not a Google visibility lever. | [[llms.txt Caveat Note]], [[AI Citation Mechanics]] | `g-ai-opt-guide`; `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | 2026-07-09 | verified | Search docs update changes llms.txt language. |
| REQ-GOOGLE-AI-003 | Preferred Sources can appear in AI Mode and AI Overviews in available languages and locales, but this is user preference and distribution guidance, not a citation guarantee. | [[Distribution and Repurposing]], [[AI Citation Mechanics]] | `pending:g-preferred-sources` | 2026-07-09 | verified, pending ledger entry | Preferred Sources docs change availability or eligibility. |
| REQ-MONITORING-001 | No confirmed Google ranking incident appears after the 2026-06-24 spam update on the Search Status Dashboard as of 2026-07-09. | [[Google Algorithm Update Ledger]], [[2026 Google Update Timeline]] | `g-status-dashboard`; `g-update-2026-06-24-june-2026-spam-update` | 2026-07-09 | verified | Status dashboard adds a new ranking incident. |
| REQ-SCHEMA-001 | Do not sell FAQPage as a current Google visual rich result tactic after the 2026-05-07 retirement. | [[Blog Schema Stack]], [[Structured Data Deprecation Register]] | `g-update-2026-05-07-faq-rich-results-retired` | 2026-07-09 | verified | FAQPage docs, Search Console API support, or Search docs updates change status. |
| REQ-SCHEMA-002 | Do not score HowTo as a current Google blog rich-result tactic after its 2023-09-13 deprecation. | [[Blog Schema Stack]], [[Structured Data Deprecation Register]], [[Blog Quality Score]] | `pending:g-howto-rich-result-deprecated` | 2026-07-09 | verified, pending ledger entry | Google restores HowTo or creates replacement guidance. |
| REQ-SCHEMA-003 | For ecommerce blog pages with real product content, merchant listing review must include July 7 guidance for `Product.category` and sale-price effective dates. | [[Product Mentions In Blog Schema]], [[Schema Deprecation Watch]] | `g-search-docs-updates-2026-07-07-product-structured-data`; `pending:g-merchant-listing` | 2026-07-09 | verified, pending ledger entry | Merchant listing docs update again. |
| REQ-AMP-001 | Remove old AMP viewer, AMP Cache, and signed exchange maintenance language from current AMP advice. | [[Google Algorithm Update Ledger]], [[Monthly Source Refresh]] | `pending:g-search-docs-updates-2026-07-01-amp` | 2026-07-09 | verified, pending ledger entry | AMP docs update again. |
| REQ-DATA-001 | Use read-only Search Console scopes when possible, and record that the Search Analytics API is bounded by Search Console limits rather than complete query truth. | [[Credential Boundary Rules]], [[Metric Export Schema]] | `pending:gsc-searchanalytics-api` | 2026-07-09 | verified, pending ledger entry | Search Analytics API scope, limit, or dimension docs change. |
| REQ-DATA-002 | URL Inspection API evidence applies to the Google-indexed version of a URL under the property, not live URL indexability testing. | [[Credential Boundary Rules]], [[URL Inspection Evidence Plan]] | `pending:gsc-url-inspection-api` | 2026-07-09 | verified, pending ledger entry | URL Inspection API docs change scope. |
| REQ-MEDIA-001 | Generated media must record model or source, prompt or edit summary, input rights, consent status when people or voices appear, disclosure text, provenance signal, and reviewer. | [[Generated Media Disclosure Notes]], [[Media QA For Blog Posts]] | `pending:google-ai-gemini-image-generation`; `pending:c2pa-standard` | 2026-07-09 | verified, pending ledger entry | Google AI image docs, SynthID language, C2PA docs, or publication policy changes. |
| REQ-MEDIA-002 | Do not start new image workflows on Imagen without a migration note because Gemini API docs say Imagen models are deprecated and will shut down on 2026-08-17. | [[Generated Media Disclosure Notes]], [[Images Audio and Charts]] | `pending:google-ai-imagen-deprecation` | 2026-07-09 | verified, pending ledger entry | Gemini API image-generation docs change Imagen shutdown guidance. |
| REQ-SOURCES-001 | Current claims need source ID, URL, retrieval date, confidence, and refresh trigger before release use. | [[Claim To Source Mapping]], [[Evidence Gap Register]] | local convention | 2026-07-09 | advisory | Linter or audit contract changes. |

## Use Rules

- Use `verified` only when the source directly supports the claim scope and date.
- Use `pending:` source IDs only inside wiki notes and only with a matching gap entry.
- Do not upgrade pending, raw-missing, or date-mismatched claims into release evidence.
- Refresh this digest whenever Google Search documentation updates, the Search Status Dashboard, Google AI docs, QRG, or relevant API docs change.

## Related

- [[Research Pack Index]]
- [[Claim To Source Mapping]]
- [[Evidence Gap Register]]
- [[Source Confidence Labels]]
- [[Google Algorithm Update Ledger]]
