---
type: spoke
title: "2026 Google Update Timeline"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [monitoring, google-updates, active]
domain: "Google Update Monitoring"
confidence: verified
related:
  - "[[Google Algorithm Update Ledger]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Research Pack Index]]"
  - "[[Google Data Integrations]]"
  - "[[Confirmed Update Entry Template]]"
  - "[[Unverified Volatility Quarantine]]"
  - "[[Core Update Response Playbook]]"
  - "[[Spam Update Response Playbook]]"
  - "[[Schema Deprecation Watch]]"
  - "[[2025 Google Update Timeline]]"
  - "[[2024 Google Update Timeline]]"
source_urls:
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
  - "https://developers.google.com/search/updates/ranking"
  - "https://developers.google.com/search/updates"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://developers.google.com/search/docs/appearance/preferred-sources"
  - "https://developers.google.com/search/docs/crawling-indexing/amp"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/essentials/spam-policies"
  - "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://blog.google/products-and-platforms/products/search/search-io-2026/"
  - "https://ziptie.dev/blog/google-ai-overviews-source-selection/"
  - "https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing"
  - "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing"
  - "https://developers.google.com/search/docs/fundamentals/third-party-seo"
  - "https://developers.google.com/search/blog/2026/04/back-button-hijacking"
  - "https://support.google.com/merchants/answer/16989427"
---

# 2026 Google Update Timeline

## Summary
This spoke summarizes confirmed 2026 Google-owned ranking incidents and Search documentation updates checked through 2026-07-09.
It belongs to [[Google Algorithm Update Ledger]] and supports confirmed Google updates, volatility quarantine, update response, and dated source refresh.
Primary working inputs: 2026 update entries, Google-owned URLs, notes, blog implications.
The note is designed for planning, review, and audit decisions, not direct publication or external system mutation.
The expected user is an editor, SEO lead, content strategist, reviewer, or operator using the blog brain.
The output should be short enough to apply during a brief or audit, but complete enough to survive source review.

## Evidence Anchors
- The local update ledger contains 34 Google-owned update entries through the 2026-06-30 Merchant Center product videos entry, but it is stale for July 2026 documentation updates.
- The Search Status Dashboard records no confirmed Google-owned ranking incident after the 2026-06-24 spam update as of 2026-07-09.
- Google Search documentation updates add 2026-07-01 AMP guidance changes and 2026-07-07 merchant listing structured-data changes.
- FAQ rich results retired for all sites effective 2026-05-07, which makes Article or BlogPosting the blog schema priority.
- Google AI optimization guide page date is 2026-06-29; the 2026-06-15 Search documentation update added the llms.txt clarification.
- Preferred Sources availability for AI Mode and AI Overviews is confirmed by Google Search documentation dated 2026-05-27.
- QRG status remains tied to the 2025-09-11 version as of 2026-07-09.
- As of 2026-07-06, SparkToro reports 68.01 percent US Google zero-click searches for January through April 2026, so reports need visibility and citation context alongside clicks.
- Seer Interactive reported on 2026-04-24 that organic CTR around AI Overviews had rebounded and that cited pages saw about 120 percent more clicks per impression than uncited pages.
- Google I/O Search updates on 2026-05-19 reported AI Mode above 1B monthly users, while the research substrate records about 0.34 percent US query volume, so AI Mode is strategic but not the only planning surface.
- Google FAQPage documentation marks FAQ rich results retired for all sites effective 2026-05-07, so blog schema planning should prioritize Article or BlogPosting with visible helpful content.
- The active QRG reference is the 2025-09-11 revision as of 2026-07-06, and the substrate records no newer QRG revision.
- Google AI optimization guidance has current page date 2026-06-29; the 2026-06-15 documentation change specifically clarified that Google Search does not use llms.txt and the current guide says special AI files, special AI schema, Markdown conversion, and chunking are not Google requirements.
- Passage extraction heuristics belong in [[Passage Citability Checklist]] and remain practitioner-derived, not Google update requirements.

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
- Define the decision this note supports: summarizes confirmed 2026 Google updates checked through 2026-07-09.
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

This timeline uses data/google-updates.json, last verified 2026-07-06, plus a 2026-07-09 manual check of Google-owned Search documentation and the Search Status Dashboard.
The local data file contains 16 confirmed 2026 entries; this wiki timeline adds three Google-owned documentation entries that are not yet in the data file.
Each entry should be used as a monitoring anchor, not as proof that a specific page won or lost traffic without first-party data.
Third-party volatility can explain what to inspect, but it does not promote an event into this timeline.

## 2026 Entries
- 2026-02-05: February 2026 Discover Update [discover].
  Source: https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
  Note: Started Feb 5, 21-day rollout. Discover-surface ranking update per the Google status dashboard (verified 2026-07-02).
- 2026-03-24: March 2026 Spam Update [spam].
  Source: https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
  Note: Started Mar 24, completed in under a day (19.5-hour rollout). Per the Google status dashboard (verified 2026-07-02).
- 2026-03-27: March 2026 Core Update [core].
  Source: https://developers.google.com/search/updates/ranking
  Note: Started Mar 27, completed Apr 8 (12-day rollout). First core update of 2026. Promoted from unverified[] after Google status-dashboard confirmation.
- 2026-05-07: FAQ rich results retired [schema].
  Source: https://developers.google.com/search/docs/appearance/structured-data/faqpage
  Note: FAQ rich results no longer shown for any site (supersedes the Aug 2023 gov/health restriction). Rich Results Test + report support drops Jun 2026; Search Console API support removed Aug 2026. Use QAPage for genuine single-question pages; FAQPage still aids AI/LLM citation as an entity signal.
- 2026-05-15: Spam policies update (gen-AI scaled content) [policy].
  Source: https://developers.google.com/search/docs/essentials/spam-policies
  Note: Scaled content abuse now explicitly names 'using generative AI tools to generate many pages without adding value' (and automated transformations like translating). Expired-domain and site-reputation abuse remain.
- 2026-05-15: New Generative AI optimization guide [product].
  Source: https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing
  Note: New 'Generative AI fundamentals / ai-optimization-guide' doc. The page is currently dated 2026-06-29, and the 2026-06-15 docs update clarified that Google Search ignores llms.txt.
- 2026-05-19: Google I/O 2026: Gemini 3.5 Flash powers AI Mode [product].
  Source: https://blog.google/products-and-platforms/products/search/search-io-2026/
  Note: Gemini 3.5 Flash becomes the default model in AI Mode globally. AI Mode surpassed 1B+ monthly users. New intelligent Search box; Information Agents, generative UI, and agentic checkout rolling out summer 2026.
- 2026-05-20: hasAdultConsideration property added [schema].
  Source: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
  Note: Product variant / Merchant listing; required for adult-oriented products; only supported value https://schema.org/SexualContentConsideration.
- 2026-05-21: May 2026 Core Update [core].
  Source: https://developers.google.com/search/updates/ranking
  Note: Up to 2-week rollout. Second core update of 2026. Global, all languages. Google: 'a regular update designed to better surface relevant, satisfying content from all types of sites.'
- 2026-05-27: Preferred Sources available in AI Mode and AI Overviews [search-feature].
  Source: https://developers.google.com/search/docs/appearance/preferred-sources
  Source ID: pending:g-preferred-sources
  Note: Google updated Preferred Sources feature availability to include AI Overviews and AI Mode, and states domain-level and subdomain-level sites are eligible. Route publisher distribution and citation planning through [[AI Citation Mechanics]] and [[Distribution and Repurposing]]; do not treat this as a citation guarantee.
- 2026-06-02: May 2026 Core Update complete [core].
  Source: https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
  Note: May 2026 core update (started 2026-05-21) completed 2026-06-02.
- 2026-06-03: Search Console Search Generative AI performance reports [tooling].
  Source: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
  Note: New Search Console reporting of impressions in AI Overviews and AI Mode (and Discover). Rolling out to a subset; day-of-month lightly sourced, month confirmed.
- 2026-06-05: Guidance on third-party SEO tools, services, and advice [product].
  Source: https://developers.google.com/search/docs/fundamentals/third-party-seo
  Note: No tool guarantees rankings; third-party tools lack access to Google's internal ranking data; Google doesn't endorse vendors; evaluate AEO/GEO claims vs official guidance; GSC is the first-party source.
- 2026-06-15: Back button hijacking spam policy in effect [policy].
  Source: https://developers.google.com/search/blog/2026/04/back-button-hijacking
  Note: Malicious-practices spam policy published 2026-04, enforcement began 2026-06-15.
- 2026-06-15: llms.txt clarified as unused by Google Search [guidance].
  Source: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
  Note: Google Search does not use llms.txt; it neither helps nor harms Search, AI Overviews, or AI Mode visibility.
- 2026-06-24: June 2026 Spam Update [spam].
  Source: https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
  Note: Normal spam update, all languages/locations. Rolled out 2026-06-24, complete 2026-06-26. Not link-specific; enforces existing spam policies (scaled content, cloaking, sneaky redirects).
- 2026-06-30: Merchant Center product videos serving-eligible [ecommerce].
  Source: https://support.google.com/merchants/answer/16989427
  Note: video_link attribute becomes eligible to serve on 2026-06-30.
- 2026-07-01: AMP documentation update [documentation].
  Source: https://developers.google.com/search/updates#july-2026
  Source ID: pending:g-search-docs-updates-2026-07-01-amp
  Note: Google simplified AMP documentation by removing outdated AMP viewer, AMP Cache, and signed exchange references. AMP content continues to rank like other web pages. This is a documentation and maintenance-language update, not a confirmed ranking rollout.
- 2026-07-07: Merchant listing structured data category and sale duration guidance [schema].
  Source: https://developers.google.com/search/updates#july-2026
  Source ID: g-search-docs-updates-2026-07-07-product-structured-data
  Note: Google added `Product.category` guidance for Text and CategoryCode values and added sale-price effective-date guidance using `validFrom`, `validThrough`, and `priceValidUntil`. The operational merchant listing page is https://developers.google.com/search/docs/appearance/structured-data/merchant-listing and needs a dedicated ledger source ID.

## Blog Implications
- February Discover, March spam, March core, May core, and June spam updates create separate review tracks by surface and policy.
- FAQ rich results retired on 2026-05-07, so blog schema should prioritize Article or BlogPosting with visible reader value.
- The 2026-06-15 AI optimization guidance says Google Search does not use llms.txt, so do not add it as a Google visibility requirement.
- Generative AI performance reports announced 2026-06-03 make first-party AI feature impressions available for some properties.
- No confirmed Google-owned ranking incident appears after 2026-06-24 in the Search Status Dashboard as of 2026-07-09.
- July 2026 documentation changes affect AMP maintenance language and ecommerce schema guidance; they do not create a new confirmed ranking rollout by themselves.

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
- Evidence currency risk: 2026 Google Update Timeline decisions can go stale when a source, date, or requirement changes.
- Claim scope risk: keep 2026 Google Update Timeline advice tied to the source coverage named in this note.
- Operational boundary risk: do not turn 2026 Google Update Timeline into CMS, analytics, Search Console, API, or publishing mutation steps.
- Proof gap risk: when the note lacks direct evidence, record the gap instead of upgrading confidence.
- Audience fit risk: adjust 2026 Google Update Timeline guidance for topic sensitivity, locale, and review ownership before use.
- Media and data risk: verify charts, visuals, metrics, and examples before they carry this note's claims.
- Metric interpretation risk: separate first-party exports, market studies, and API signals in 2026 Google Update Timeline outputs.
- Monitoring risk: quarantine unconfirmed volatility until a dated source in the ledger supports it.

## Output Shape
- A 2026 Google Update Timeline decision summary for the editor or auditor.
- The source IDs or URLs that directly support the active recommendation.
- A confidence label that matches the evidence strength for this note.
- A rollback or refresh condition tied to the source or workflow affected.
- A blocked-claims list for 2026 Google Update Timeline gaps that need more evidence.
- A handoff note naming the writer, editor, reviewer, or data owner next action.
- Links back to the parent hub and sibling notes that keep the graph navigable.
- A no-action statement when 2026 Google Update Timeline evidence is incomplete or outside this brain.

## Related
- [[Google Algorithm Update Ledger]]
- [[index|Index]]
- [[hot|Hot]]
- [[Research Pack Index]]
- [[Google Data Integrations]]
- [[Confirmed Update Entry Template]]
- [[Unverified Volatility Quarantine]]
- [[Core Update Response Playbook]]
- [[Spam Update Response Playbook]]
- [[Schema Deprecation Watch]]
- [[2025 Google Update Timeline]]
- [[2024 Google Update Timeline]]

## Source URLs
- https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history
- https://developers.google.com/search/updates/ranking
- https://developers.google.com/search/updates
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/appearance/preferred-sources
- https://developers.google.com/search/docs/crawling-indexing/amp
- https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
- https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- https://blog.google/products-and-platforms/products/search/search-io-2026/
- https://ziptie.dev/blog/google-ai-overviews-source-selection/
- https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing
- https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- https://developers.google.com/search/docs/fundamentals/third-party-seo
- https://developers.google.com/search/blog/2026/04/back-button-hijacking
- https://support.google.com/merchants/answer/16989427

## Maintenance Notes
- Refresh this note from [[Research Pack Index]] when any listed source changes after 2026-07-09.
- Keep backlink health with [[Google Algorithm Update Ledger]], [[index|Index]], and sibling spokes in this folder.
- Keep confidence advisory when source coverage is incomplete, narrow, stale, or practitioner-led.
- Keep confidence verified only for claims directly tied to official, primary, standards, or first-party sources.
- Do not record secrets, tokens, private exports, or private client details in this note.
- Do not publish or mutate CMS, GSC, GA4, Search Console, analytics, schema, sitemap, or platform settings from this note.
