---
type: source
title: "Research Pack 2026-07-06"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [sources, research-pack, active]
domain: Sources
confidence: advisory
related:
  - "[[Research Pack Index]]"
  - "[[Claim To Source Mapping]]"
  - "[[Evidence Gap Register]]"
  - "[[Current Requirements Digest]]"
  - "[[Source Ledger Reading Guide]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
---

# Research Pack 2026-07-06

## research-pack-2026-07-06 Evidence Job

This note is the human-readable governance record for the source pack generated on 2026-07-06 and rechecked for this folder on 2026-07-09. The complete machine-readable source list remains in `references/source-ledger.json`.

The pack should be read as evidence infrastructure, not as a claim that every downstream note is release-complete. When a source ID is missing, stale, or too broad, the gap belongs in [[Evidence Gap Register]].

## Source Types This Note Owns

- Official Google Search content guidance.
- Official Google AI Search guidance.
- Official Google structured data support inventory.
- Official Google ranking history and update status.

## Claims This Note Must Not Validate Alone

- Current API, media, or model claims that lack source IDs in this folder.
- Client-specific results or first-party analytics.
- Practitioner study conclusions without claim-ledger verdict handling.

## research-pack-2026-07-06 Source Table

| Source ID | URL | Ledger date | Claim coverage | Limitation | Refresh cadence |
|---|---|---:|---|---|---|
| `g-helpful-content` | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | last updated 2025-12-10, retrieved 2026-07-09 | People-first content and E-E-A-T self-review guidance. | Does not certify page quality or ranking outcomes. | Monthly and before release. |
| `g-ai-opt-guide` | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | last updated 2026-06-15, retrieved 2026-07-08 | Google Search AI feature optimization guidance. | Google Search only. Non-Google assistants need separate evidence. | On documentation change. |
| `g-search-gallery` | https://developers.google.com/search/docs/appearance/structured-data/search-gallery | last updated 2026-07-01, retrieved 2026-07-08 | Current supported rich-result inventory. | Does not validate every structured data vocabulary choice. | Before schema release. |
| `g-ranking-history` | https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history | last updated 2026-06-24, retrieved 2026-07-09 | Confirmed ranking update history and rollout state. | Does not prove local impact or recovery cause. | Weekly during rollouts, monthly otherwise. |

## Source ID, URL, Date, Claim Coverage, And Limitation

This pack's operating value is traceability. A source row should let a reviewer find the original page, see when it was checked, understand what it covers, and know what it does not prove.

## research-pack-2026-07-06 Refresh Procedure

1. Check source IDs in the machine ledger before trusting a wiki summary.
2. Compare page date and retrieval date against the table above.
3. Keep source-family changes in this note and claim wording in [[Claim To Source Mapping]].
4. Send source absence, date mismatch, or missing raw provenance to [[Evidence Gap Register]].
5. Avoid adding broad source bundles to frontmatter unless the body cites them directly.

## Related

- [[Research Pack Index]]
- [[Claim To Source Mapping]]
- [[Evidence Gap Register]]
- [[Current Requirements Digest]]
- [[Source Ledger Reading Guide]]
