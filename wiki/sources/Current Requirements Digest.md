---
type: spoke
title: "Current Requirements Digest"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [sources, research-pack, active]
domain: "Source Evidence"
confidence: verified
related:
  - "[[Research Pack Index]]"
  - "[[Index]]"
  - "[[Hot]]"
  - "[[Google Algorithm Update Ledger]]"
  - "[[Google Data Integrations]]"
  - "[[Canon Notes Map]]"
  - "[[Google Source Priority Ladder]]"
  - "[[Primary Study Source Rules]]"
  - "[[Practitioner Source Caveats]]"
  - "[[Source Refresh Cadence]]"
  - "[[Source Ledger Reading Guide]]"
  - "[[Research Release Gate Notes]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/fundamentals/third-party-seo"
  - "https://blog.google/products-and-platforms/products/search/search-io-2026/"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://ziptie.dev/blog/google-ai-overviews-source-selection/"
---

# Current Requirements Digest

## Summary
This spoke condenses the live mid-2026 operating requirements into a routing note for writers and auditors.
It belongs to [[Research Pack Index]] and supports source routing, confidence labels, claim mapping, refresh cadence, and evidence gaps.
Primary working inputs: current requirements file, ledger URLs, refresh date, rule list.
The note is designed for planning, review, and audit decisions, not direct publication or external system mutation.
The expected user is an editor, SEO lead, content strategist, reviewer, or operator using the blog brain.
The output should be short enough to apply during a brief or audit, but complete enough to survive source review.

## Evidence Anchors
- The source ledger contains 115 sources generated and last verified on 2026-07-06.
- Current requirements were last verified 2026-07-06 and set a 2026-08-06 refresh due date.
- Official Google, standards, primary, vendor, regulator, government, authority, and API documentation sources carry the highest source priority.
- Practitioner studies are useful for workflow heuristics and market behavior, but they need advisory confidence when not first-party to the property.
- Evidence must be recorded in references/source-ledger.json rather than only summarized in wiki prose.
- As of 2026-07-06, SparkToro reports 68.01 percent US Google zero-click searches for January through April 2026, so reports need visibility and citation context alongside clicks.
- Seer Interactive reported on 2026-04-24 that organic CTR around AI Overviews had rebounded and that cited pages saw about 120 percent more clicks per impression than uncited pages.
- Google I/O Search updates on 2026-05-19 reported AI Mode above 1B monthly users, while the research substrate records about 0.34 percent US query volume, so AI Mode is strategic but not the only planning surface.
- Google FAQPage documentation marks FAQ rich results retired for all sites effective 2026-05-07, so blog schema planning should prioritize Article or BlogPosting with visible helpful content.
- The active QRG reference is the 2025-09-11 revision as of 2026-07-06, and the substrate records no newer QRG revision.
- Google AI optimization guidance updated 2026-06-15 says Google Search does not use llms.txt and does not require special AI schema, Markdown conversion, or chunking files.
- The practical passage extraction target is a self-contained answer block of roughly 130 to 170 words under a clear heading, with source context and entity clarity.

## Required Inputs
- Source ID, title, URL, source type, section, retrieved date, and refresh due date.
- Claim text exactly as it will appear in a recommendation or audit.
- Confidence label based on source authority, recency, and claim specificity.
- Primary source preference when Google, standards, or first-party documentation exists.
- Practitioner or market source caveat when the evidence describes behavior rather than official requirements.
- Gap owner and due date when evidence is missing or stale.
- Release gate note when a missing source blocks market-ready status.
- Rollback note when an external source changes or loses relevance.

## Workflow
- Define the decision this note supports: condenses the live mid-2026 operating requirements into a routing note for writers and auditors.
- Open [[Research Pack Index]] and confirm the hub rule that applies before using this spoke.
- Start with official Google, standards, primary, or first-party sources when they exist for the claim.
- Use practitioner sources for methods and observed behavior only with caveats about scope and recency.
- Route every current requirement through the ledger rather than relying on memory or prose notes.
- Promote gaps to the evidence register before they reach recommendations.
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
- [[Research Pack Index]]
- [[Index]]
- [[Hot]]
- [[Google Algorithm Update Ledger]]
- [[Google Data Integrations]]
- [[Canon Notes Map]]
- [[Google Source Priority Ladder]]
- [[Primary Study Source Rules]]
- [[Practitioner Source Caveats]]
- [[Source Refresh Cadence]]
- [[Source Ledger Reading Guide]]
- [[Research Release Gate Notes]]

## Source URLs
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
- https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf
- https://developers.google.com/search/docs/fundamentals/third-party-seo
- https://blog.google/products-and-platforms/products/search/search-io-2026/
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://ziptie.dev/blog/google-ai-overviews-source-selection/

## Maintenance Notes
- Refresh this note from [[Research Pack Index]] when any listed source changes after 2026-07-06.
- Keep backlink health with [[Research Pack Index]], [[Index]], and sibling spokes in this folder.
- Keep confidence advisory when source coverage is incomplete, narrow, stale, or practitioner-led.
- Keep confidence verified only for claims directly tied to official, primary, standards, or first-party sources.
- Do not record secrets, tokens, private exports, or private client details in this note.
- Do not publish or mutate CMS, GSC, GA4, Search Console, analytics, schema, sitemap, or platform settings from this note.
