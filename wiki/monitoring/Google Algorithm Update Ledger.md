---
type: hub
title: "Google Algorithm Update Ledger"
status: active
created: 2026-07-06
updated: 2026-07-08
tags: [monitoring, google-updates, active]
domain: "Google Update Monitoring"
confidence: verified
related:
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Freshness and Content Decay]]"
  - "[[E-E-A-T for Blog Content]]"
  - "[[Blog Schema Stack]]"
  - "[[Google Data Integrations]]"
  - "[[Blog Quality Score]]"
  - "[[Research Pack Index]]"
source_urls:
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
  - "https://developers.google.com/search/updates/ranking"
  - "https://developers.google.com/search/updates"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/docs/appearance/preferred-sources"
  - "https://developers.google.com/search/docs/crawling-indexing/amp"
  - "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
---

# Google Algorithm Update Ledger

## Summary

Google Algorithm Update Ledger is the monitoring hub for confirmed Google-owned updates, schema changes, AI search guidance, and QRG status.

This hub mirrors the source discipline from `data/google-updates.json` without editing that data file.

## Current fact anchors

- The verified local update ledger contains 34 Google-owned update entries through the 2026-06-30 Merchant Center product videos entry, but that data file is stale for July 2026 Search documentation updates.
- Google Search documentation updates add 2026-07-01 AMP guidance changes and 2026-07-07 merchant listing structured-data guidance changes.
- The Search Status Dashboard records no confirmed Google-owned ranking incident after the 2026-06-24 spam update as of 2026-07-08.
- FAQ rich results retired for all sites effective 2026-05-07.
- Google AI optimization guidance has current page date 2026-06-29; the llms.txt clarification was added 2026-06-15 and says Google Search does not use llms.txt.
- Preferred Sources availability for AI Mode and AI Overviews is confirmed by Google Search documentation dated 2026-05-27.
- QRG status remains tied to the 2025-09-11 version, with no newer revision recorded as of 2026-07-08.

## Scope

- Track confirmed Google ranking, spam, schema, AI, and QRG changes.
- Quarantine third-party volatility reports until Google-owned confirmation exists.
- Connect updates to [[Freshness and Content Decay]].
- Connect schema changes to [[Blog Schema Stack]].
- Connect QRG changes to [[E-E-A-T for Blog Content]].
- Connect measurement changes to [[Google Data Integrations]].
- Connect quality implications to [[Blog Quality Score]].
- Keep update notes source-dated.

## Future spoke notes

- [[Confirmed Update Entry Template]]
- [[Unverified Volatility Quarantine]]
- [[Core Update Response Playbook]]
- [[Spam Update Response Playbook]]
- [[Schema Deprecation Watch]]
- [[QRG Revision Watch]]
- [[AI Search Update Watch]]
- [[Update Impact Review]]
- [[Monthly Source Refresh]]
- [[Monitoring Confidence Labels]]

## Monitoring rules

- Use Google-owned sources for confirmed updates.
- Use third-party volatility only as advisory context.
- Do not rewrite guidance from volatility chatter alone.
- Add exact dates to all update claims.
- Connect affected pages to first-party data where available.
- Preserve the distinction between ranking updates and documentation updates.
- Keep no-current-update claims dated.
- Append durable changes to [[log]].

## Source posture

- Use Search Status Dashboard for confirmed incidents and histories.
- Use Search Central documentation for policy and schema changes.
- Use [[Research Pack Index]] for source-ledger routes.
- Keep local data files read-only in this slice.
- Keep recommendations advisory until approved elsewhere.

## Related themes

- [[Freshness and Content Decay]]
- [[E-E-A-T for Blog Content]]
- [[AI Citation Mechanics]]
- [[Blog Schema Stack]]
- [[Google Data Integrations]]
- [[Blog Quality Score]]
- [[FLOW Framework]]
- [[Research Pack Index]]

## Sources

- Google Search Status Dashboard, retrieved 2026-07-08.
- Google Search documentation updates, retrieved 2026-07-08.
- Google ranking update history, dated 2026-05-21 in the ledger.
- Google FAQPage documentation, effective 2026-05-07 for retirement.
- Google AI optimization guide, last updated 2026-06-29, with llms.txt clarification dated 2026-06-15 in Search docs updates.
- Google Preferred Sources documentation, last updated 2026-05-27.
- Google AMP documentation, last updated 2026-07-01.
- Google Merchant listing structured data, last updated 2026-07-07.
- Search Quality Rater Guidelines, 2025-09-11.

## Next actions

- Fill [[Unverified Volatility Quarantine]] before monitoring imports.
- Fill [[Monthly Source Refresh]] before recurring operations.
- Link update impact to [[Freshness and Content Decay]].
