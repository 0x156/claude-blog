---
type: spoke
title: "2025 Google Update Timeline"
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
  - "[[2026 Google Update Timeline]]"
  - "[[Confirmed Update Entry Template]]"
  - "[[Unverified Volatility Quarantine]]"
  - "[[Core Update Response Playbook]]"
  - "[[Spam Update Response Playbook]]"
  - "[[2024 Google Update Timeline]]"
  - "[[Monitoring Confidence Labels]]"
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
  - "https://services.google.com/fh/files/misc/hsw-sqrg.pdf"
  - "https://blog.google/products/search/ai-mode-search/"
  - "https://blog.google/products/search/google-search-ai-mode-update/"
  - "https://developers.google.com/search/blog/2025/06/simplifying-search-results"
---

# 2025 Google Update Timeline

## Summary
This spoke summarizes confirmed 2025 Google updates from the local Google-owned update ledger.
It belongs to [[Google Algorithm Update Ledger]] and supports confirmed Google updates, volatility quarantine, update response, and dated source refresh.
Primary working inputs: 2025 update entries, Google-owned URLs, notes, blog implications.
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
- Define the decision this note supports: summarizes confirmed 2025 Google updates from the local Google-owned update ledger.
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

This timeline is drawn from data/google-updates.json, last verified 2026-07-06, and includes only Google-owned source URLs for 2025.
The 2025 set contains 9 confirmed entries in the local update ledger.
Each entry should be used as a monitoring anchor, not as proof that a specific page won or lost traffic without first-party data.
Third-party volatility can explain what to inspect, but it does not promote an event into this timeline.

## 2025 Entries
- 2025-01-23: QRG update (Jan 2025) [qrg].
  Source: https://services.google.com/fh/files/misc/hsw-sqrg.pdf
  Note: Adds formal definition of generative AI (section 2.1). Defines scaled content abuse, expired-domain abuse, filler content under section 4.6 Spammy Webpages. Lowest rating triggered when all/almost all MC is copied, paraphrased, or AI-generated.
- 2025-03-05: AI Mode experimental launch [product].
  Source: https://blog.google/products/search/ai-mode-search/
  Note: Initially Google One AI Premium / Labs (US). Gemini 2.0 backend. Query fan-out technique.
- 2025-03-13: March 2025 Core Update [core].
  Source: https://developers.google.com/search/updates/ranking
  Note: 14-day rollout.
- 2025-05-20: AI Mode general rollout (US) [product].
  Source: https://blog.google/products/search/google-search-ai-mode-update/
  Note: No Labs sign-up required. Gemini 2.5 in AI Mode and AI Overviews.
- 2025-06-19: Structured data deprecation [schema].
  Source: https://developers.google.com/search/blog/2025/06/simplifying-search-results
  Note: Phased out: Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement (carryover), Vehicle Listing.
- 2025-06-30: June 2025 Core Update [core].
  Source: https://developers.google.com/search/updates/ranking
  Note: 16-day rollout. Some Sep 2023 HCU partial recoveries.
- 2025-08-21: AI Mode expands to 180+ countries [product].
  Source: https://blog.google/products/search/google-search-ai-mode-update/
  Note: English first. Robby Stein: 'active' AI Mode begins with dining reservations.
- 2025-09-11: QRG update (Sept 2025) [qrg].
  Source: https://services.google.com/fh/files/misc/hsw-sqrg.pdf
  Note: Adds AI Overview rating examples. Expands YMYL to include political/social topics. Google: 'no change to rating guidance'.
- 2025-12-11: December 2025 Core Update [core].
  Source: https://developers.google.com/search/updates/ranking
  Note: 18-day rollout. Third core update of 2025. Reported eCommerce skew per Amsive analysis.

## Blog Implications
- QRG changes in January and September 2025 keep generative AI, YMYL, and AI Overview rating examples in the quality review path.
- AI Mode launches and expansion make AI search a monitoring surface, but source-backed content remains the shared foundation.
- Structured data deprecations in June 2025 warn against selling obsolete visual rich result features.
- Core updates in March, June, and December need measured page-set review using GSC and editorial quality checks.
- AI Mode expansion creates a reason to watch citation surfaces without abandoning ordinary organic search data.

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
- Stale source risk: a Search Central, QRG, schema, or AI feature change can invalidate current wording.
- Overclaim risk: market studies can describe averages, not guaranteed results for a specific site.
- Scope risk: a workflow note can drift into implementation if credential, CMS, or API mutation steps are added.
- Evidence risk: single-source or practitioner-only claims need advisory confidence until stronger evidence is captured.
- Locale risk: translated content can lose legal, cultural, or source meaning without qualified review.
- Media risk: visuals can imply facts that the text and sources do not support.
- Metric risk: GSC, GA4, URL Inspection, and AI feature reports answer different questions and should not be merged casually.
- Monitoring risk: unconfirmed volatility should stay quarantined until a Google-owned URL confirms it.

## Output Shape
- A one-paragraph decision summary for the editor or auditor.
- A dated source list using URLs that are present in the source ledger.
- A confidence label that distinguishes verified evidence from advisory interpretation.
- A rollback or refresh condition for time-sensitive guidance.
- A list of blocked claims that need more evidence before publication.
- A handoff note for writers, editors, reviewers, or data owners.
- A graph link to the parent hub and at least several sibling spokes.
- A clear statement when no action is recommended because the evidence is incomplete.

## Related
- [[Google Algorithm Update Ledger]]
- [[index|Index]]
- [[hot|Hot]]
- [[Research Pack Index]]
- [[Google Data Integrations]]
- [[2026 Google Update Timeline]]
- [[Confirmed Update Entry Template]]
- [[Unverified Volatility Quarantine]]
- [[Core Update Response Playbook]]
- [[Spam Update Response Playbook]]
- [[2024 Google Update Timeline]]
- [[Monitoring Confidence Labels]]

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
- https://services.google.com/fh/files/misc/hsw-sqrg.pdf
- https://blog.google/products/search/ai-mode-search/
- https://blog.google/products/search/google-search-ai-mode-update/
- https://developers.google.com/search/blog/2025/06/simplifying-search-results

## Maintenance Notes
- Refresh this note from [[Research Pack Index]] when any listed source changes after 2026-07-06.
- Keep backlink health with [[Google Algorithm Update Ledger]], [[index|Index]], and sibling spokes in this folder.
- Keep confidence advisory when source coverage is incomplete, narrow, stale, or practitioner-led.
- Keep confidence verified only for claims directly tied to official, primary, standards, or first-party sources.
- Do not record secrets, tokens, private exports, or private client details in this note.
- Do not publish or mutate CMS, GSC, GA4, Search Console, analytics, schema, sitemap, or platform settings from this note.
