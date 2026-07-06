---
type: spoke
title: "Schema Deprecation Watch"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [monitoring, google-updates, active]
domain: "Google Update Monitoring"
confidence: verified
related:
  - "[[Google Algorithm Update Ledger]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Research Pack Index]]"
  - "[[Google Data Integrations]]"
  - "[[QRG Revision Watch]]"
  - "[[AI Search Update Watch]]"
  - "[[Update Impact Review]]"
  - "[[Monthly Source Refresh]]"
  - "[[Monitoring Confidence Labels]]"
  - "[[Spam Update Response Playbook]]"
  - "[[Core Update Response Playbook]]"
source_urls:
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
  - "https://developers.google.com/search/updates/ranking"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/essentials/spam-policies"
  - "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://blog.google/products-and-platforms/products/search/search-io-2026/"
  - "https://ziptie.dev/blog/google-ai-overviews-source-selection/"
---

# Schema Deprecation Watch

## Summary
This spoke tracks structured data support changes and prevents deprecated rich result tactics from entering briefs.
It belongs to [[Google Algorithm Update Ledger]] and supports confirmed Google updates, volatility quarantine, update response, and dated source refresh.
Primary working inputs: schema type, Google support page, effective date, impacted templates.
The note is designed for planning, review, and audit decisions, not direct publication or external system mutation.
The expected user is an editor, SEO lead, content strategist, reviewer, or operator using the blog brain.
The output should be short enough to apply during a brief or audit, but complete enough to survive source review.

## Evidence Anchors
- The local update ledger contains 34 Google-owned update entries through the 2026-06-30 Merchant Center product videos entry.
- No Google-owned ranking, spam, schema, QRG, or AI search update is recorded from 2026-07-01 through 2026-07-06.
- FAQ rich results retired for all sites effective 2026-05-07, which makes Article or BlogPosting the blog schema priority.
- Google AI optimization guidance updated 2026-06-15 says Google Search does not use llms.txt for Search, AI Overviews, or AI Mode.
- QRG status remains tied to the 2025-09-11 version as of 2026-07-06.
- As of 2026-07-06, SparkToro reports 68.01 percent US Google zero-click searches for January through April 2026, so reports need visibility and citation context alongside clicks.
- Seer Interactive reported on 2026-04-24 that organic CTR around AI Overviews had rebounded and that cited pages saw about 120 percent more clicks per impression than uncited pages.
- Google I/O Search updates on 2026-05-19 reported AI Mode above 1B monthly users, while the research substrate records about 0.34 percent US query volume, so AI Mode is strategic but not the only planning surface.
- Google FAQPage documentation marks FAQ rich results retired for all sites effective 2026-05-07, so blog schema planning should prioritize Article or BlogPosting with visible helpful content.
- The active QRG reference is the 2025-09-11 revision as of 2026-07-06, and the substrate records no newer QRG revision.
- Google AI optimization guidance updated 2026-06-15 says Google Search does not use llms.txt and does not require special AI schema, Markdown conversion, or chunking files.
- The practical passage extraction target is a self-contained answer block of roughly 130 to 170 words under a clear heading, with source context and entity clarity.

## Required Inputs
- Confirmed Google-owned source URL or explicit unverified status.
- Exact date, update name, kind, and affected search surface.
- Local page set or content class that could plausibly be affected.
- GSC or GA4 date windows before and after the update when property data is available.
- Policy, schema, AI search, QRG, or ranking route for interpretation.
- Decision note that separates observation from recommended action.
- Refresh owner and next check date when an update is still rolling out.
- Quarantine note for third-party volatility until Google confirms it.

## Workflow
- Define the decision this note supports: tracks structured data support changes and prevents deprecated rich result tactics from entering briefs.
- Open [[Google Algorithm Update Ledger]] and confirm the hub rule that applies before using this spoke.
- Classify the event as core, spam, schema, QRG, product, AI search, guidance, tooling, or policy.
- Wait for a Google-owned source before changing durable guidance from volatility reports.
- Compare affected pages with first-party data only after the relevant rollout window is understood.
- Record no-current-update claims with exact dates so they can be invalidated later.
- Start from the parent hub and confirm the article, locale, data set, or source family affected by this note.
- List the claims that the draft or audit output will make before editing style, media, or schema.
- Attach a source URL, retrieval date, and confidence label to each current or risky claim.
- Separate reader-facing advice from implementation notes so the brain stays advisory in V1.
- Check whether first-party property data exists before leaning on market averages or practitioner studies.
- Record any missing evidence as a gap instead of converting it into a confident recommendation.
- Route schema decisions through visible page content and current Google-supported rich result documentation.
- Route AI citation decisions through answer-first passages, clear entities, and source-backed wording.
- Route multilingual and persona decisions through human review when local facts, legal terms, or YMYL sensitivity appear.
- Keep all external system changes outside this note and write only the recommendation, rationale, and rollback condition.

## Review Checks
- The note names exact dates when guidance can become stale.
- The recommendation does not promise rankings, traffic, AI citations, or rich results.
- FAQPage is not framed as a current rich result tactic after 2026-05-07.
- FID is not used as a current Core Web Vital, and INP is used when performance enters the decision.
- llms.txt is not presented as a Google Search visibility requirement.
- The cited source is appropriate for the claim strength and not just a convenient example.
- The output tells the reader what to do when first-party data is unavailable.
- The advice can be reversed or refreshed if Google documentation changes.
- The body links back to the parent hub, Index, and sibling spokes for graph health.
- The note stays inside the assigned folder and does not mutate references, data, scripts, or external platforms.

## Risk Controls
- Evidence currency risk: Schema Deprecation Watch decisions can go stale when a source, date, or requirement changes.
- Claim scope risk: keep Schema Deprecation Watch advice tied to the source coverage named in this note.
- Operational boundary risk: do not turn Schema Deprecation Watch into CMS, analytics, Search Console, API, or publishing mutation steps.
- Proof gap risk: when the note lacks direct evidence, record the gap instead of upgrading confidence.
- Audience fit risk: adjust Schema Deprecation Watch guidance for topic sensitivity, locale, and review ownership before use.
- Media and data risk: verify charts, visuals, metrics, and examples before they carry this note's claims.
- Metric interpretation risk: separate first-party exports, market studies, and API signals in Schema Deprecation Watch outputs.
- Monitoring risk: quarantine unconfirmed volatility until a dated source in the ledger supports it.

## Output Shape
- A Schema Deprecation Watch decision summary for the editor or auditor.
- The source IDs or URLs that directly support the active recommendation.
- A confidence label that matches the evidence strength for this note.
- A rollback or refresh condition tied to the source or workflow affected.
- A blocked-claims list for Schema Deprecation Watch gaps that need more evidence.
- A handoff note naming the writer, editor, reviewer, or data owner next action.
- Links back to the parent hub and sibling notes that keep the graph navigable.
- A no-action statement when Schema Deprecation Watch evidence is incomplete or outside this brain.

## Related
- [[Google Algorithm Update Ledger]]
- [[index|Index]]
- [[hot|Hot]]
- [[Research Pack Index]]
- [[Google Data Integrations]]
- [[QRG Revision Watch]]
- [[AI Search Update Watch]]
- [[Update Impact Review]]
- [[Monthly Source Refresh]]
- [[Monitoring Confidence Labels]]
- [[Spam Update Response Playbook]]
- [[Core Update Response Playbook]]

## Source URLs
- https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
- https://developers.google.com/search/updates/ranking
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
- https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- https://blog.google/products-and-platforms/products/search/search-io-2026/
- https://ziptie.dev/blog/google-ai-overviews-source-selection/

## Maintenance Notes
- Refresh this note from [[Research Pack Index]] when any listed source changes after 2026-07-06.
- Keep backlink health with [[Google Algorithm Update Ledger]], [[index|Index]], and sibling spokes in this folder.
- Keep confidence advisory when source coverage is incomplete, narrow, stale, or practitioner-led.
- Keep confidence verified only for claims directly tied to official, primary, standards, or first-party sources.
- Do not record secrets, tokens, private exports, or private client details in this note.
- Do not publish or mutate CMS, GSC, GA4, Search Console, analytics, schema, sitemap, or platform settings from this note.
