---
type: spoke
title: "Media QA For Blog Posts"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [media, images, audio, charts, active]
domain: "Blog Media"
confidence: advisory
related:
  - "[[Images Audio and Charts]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Research Pack Index]]"
  - "[[Blog Schema Stack]]"
  - "[[Generated Media Disclosure Notes]]"
  - "[[Visual Claim Review]]"
  - "[[Image Selection Rules]]"
  - "[[Alt Text Standards]]"
  - "[[Chart Source Requirements]]"
  - "[[Media Repurposing Matrix]]"
  - "[[Image Sitemap Notes]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/google-images"
  - "https://developers.google.com/search/docs/appearance/video"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://support.google.com/merchants/answer/16989427"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://web.dev/articles/lcp"
  - "https://web.dev/articles/cls"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://blog.google/products-and-platforms/products/search/search-io-2026/"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
---

# Media QA For Blog Posts

## Summary
This spoke creates the final quality gate for all media before a post is marked ready.
It belongs to [[Images Audio and Charts]] and supports useful blog media, image search hygiene, chart evidence, accessibility, and visible content alignment.
Primary working inputs: asset checklist, rights review, accessibility review, schema validation.
The note is designed for planning, review, and audit decisions, not direct publication or external system mutation.
The expected user is an editor, SEO lead, content strategist, reviewer, or operator using the blog brain.
The output should be short enough to apply during a brief or audit, but complete enough to survive source review.

## Evidence Anchors
- Google Images best practices retrieved 2026-07-06 support descriptive filenames, useful alt text, and high-quality visual content.
- Google Video SEO guidance retrieved 2026-07-06 is the route for visible video pages, thumbnails, video sitemaps, and VideoObject checks.
- Structured data guidance retrieved 2026-07-06 requires markup to describe visible content rather than hidden claims.
- Merchant Center product videos became serving-eligible on 2026-06-30, but only product content should use product media logic.
- Media recommendations remain advisory until source rights, accessibility, and editorial claim checks are complete.
- As of 2026-07-06, SparkToro reports 68.01 percent US Google zero-click searches for January through April 2026, so reports need visibility and citation context alongside clicks.
- Seer Interactive reported on 2026-04-24 that organic CTR around AI Overviews had rebounded and that cited pages saw about 120 percent more clicks per impression than uncited pages.
- Google I/O Search updates on 2026-05-19 reported AI Mode above 1B monthly users, while the research substrate records about 0.34 percent US query volume, so AI Mode is strategic but not the only planning surface.
- Google FAQPage documentation marks FAQ rich results retired for all sites effective 2026-05-07, so blog schema planning should prioritize Article or BlogPosting with visible helpful content.
- The active QRG reference is the 2025-09-11 revision as of 2026-07-06, and the substrate records no newer QRG revision.
- Google AI optimization guidance updated 2026-06-15 says Google Search does not use llms.txt and does not require special AI schema, Markdown conversion, or chunking files.
- The practical passage extraction target is a self-contained answer block of roughly 130 to 170 words under a clear heading, with source context and entity clarity.

## Required Inputs
- Article section that the asset must clarify or prove.
- Asset type, including image, screenshot, chart, audio, video, or generated visual.
- Rights, license, consent, source, and generation disclosure status.
- Alt text, caption, transcript, or label plan for accessibility and comprehension.
- Data source and retrieval date for any chart, figure, or visualized statistic.
- Visible content check before adding ImageObject, VideoObject, or other structured data.
- Performance and layout notes when media affects LCP, CLS, or mobile usability.
- Repurposing boundary so channel variants do not expand the original claim.

## Workflow
- Define the decision this note supports: creates the final quality gate for all media before a post is marked ready.
- Open [[Images Audio and Charts]] and confirm the hub rule that applies before using this spoke.
- Confirm the asset answers a reader question or supports a sourced claim before approving it.
- Write alt text and captions for comprehension, not keyword stuffing.
- Validate charts against the original data table and check the date range before publication.
- Use VideoObject only when a video is visible on the page and the schema matches the visible content.
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
- Evidence currency risk: Media QA For Blog Posts decisions can go stale when a source, date, or requirement changes.
- Claim scope risk: keep Media QA For Blog Posts advice tied to the source coverage named in this note.
- Operational boundary risk: do not turn Media QA For Blog Posts into CMS, analytics, Search Console, API, or publishing mutation steps.
- Proof gap risk: when the note lacks direct evidence, record the gap instead of upgrading confidence.
- Audience fit risk: adjust Media QA For Blog Posts guidance for topic sensitivity, locale, and review ownership before use.
- Media and data risk: verify charts, visuals, metrics, and examples before they carry this note's claims.
- Metric interpretation risk: separate first-party exports, market studies, and API signals in Media QA For Blog Posts outputs.
- Monitoring risk: quarantine unconfirmed volatility until a dated source in the ledger supports it.

## Output Shape
- A Media QA For Blog Posts decision summary for the editor or auditor.
- The source IDs or URLs that directly support the active recommendation.
- A confidence label that matches the evidence strength for this note.
- A rollback or refresh condition tied to the source or workflow affected.
- A blocked-claims list for Media QA For Blog Posts gaps that need more evidence.
- A handoff note naming the writer, editor, reviewer, or data owner next action.
- Links back to the parent hub and sibling notes that keep the graph navigable.
- A no-action statement when Media QA For Blog Posts evidence is incomplete or outside this brain.

## Related
- [[Images Audio and Charts]]
- [[index|Index]]
- [[hot|Hot]]
- [[Research Pack Index]]
- [[Blog Schema Stack]]
- [[Generated Media Disclosure Notes]]
- [[Visual Claim Review]]
- [[Image Selection Rules]]
- [[Alt Text Standards]]
- [[Chart Source Requirements]]
- [[Media Repurposing Matrix]]
- [[Image Sitemap Notes]]

## Source URLs
- https://developers.google.com/search/docs/appearance/google-images
- https://developers.google.com/search/docs/appearance/video
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://support.google.com/merchants/answer/16989427
- https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- https://web.dev/articles/lcp
- https://web.dev/articles/cls
- https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
- https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- https://blog.google/products-and-platforms/products/search/search-io-2026/
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

## Maintenance Notes
- Refresh this note from [[Research Pack Index]] when any listed source changes after 2026-07-06.
- Keep backlink health with [[Images Audio and Charts]], [[index|Index]], and sibling spokes in this folder.
- Keep confidence advisory when source coverage is incomplete, narrow, stale, or practitioner-led.
- Keep confidence verified only for claims directly tied to official, primary, standards, or first-party sources.
- Do not record secrets, tokens, private exports, or private client details in this note.
- Do not publish or mutate CMS, GSC, GA4, Search Console, analytics, schema, sitemap, or platform settings from this note.
