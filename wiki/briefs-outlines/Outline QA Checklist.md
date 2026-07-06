---
type: spoke
title: "Outline QA Checklist"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [briefs-outlines, serp-briefs, active]
domain: "Blog Briefs"
confidence: advisory
related:
  - "[[SERP-Informed Briefs and Outlines]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[SERP Brief Input Contract]]"
  - "[[Search Intent Classification]]"
  - "[[Reader Job Statement]]"
  - "[[Competitive Pattern Notes]]"
  - "[[Heading Hierarchy Rules]]"
  - "[[Evidence Block Requirements]]"
  - "[[Brief Source Pack]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://blog.google/products-and-platforms/products/search/search-io-2026/"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://ziptie.dev/blog/google-ai-overviews-source-selection/"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/ai-features"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
---

# Outline QA Checklist

## Summary
Outline QA Checklist is the spoke for check an outline before it becomes a draft request.
Use it when [[SERP-Informed Briefs and Outlines]] needs a repeatable decision record before a brief, draft, score, or report moves forward.
The durable output is a outline QA checklist.
The success condition is that the outline is complete, sourced, answer-first, and tied to the parent cluster.
Keep the note advisory in V1 and route implementation to a human owner.

## Parent Hub Fit
- Parent hub: [[SERP-Informed Briefs and Outlines]].
- Primary upstream context: [[Dual Optimization]].
- Primary downstream context: [[6-Pillar Dual Optimization]].
- Evidence route: [[Blog Quality Score]].
- Sibling comparison starts with [[SERP Brief Input Contract]] and [[Search Intent Classification]].
- Quality review should connect to [[Blog Quality Score]] when the note affects delivery.
- Citation review should connect to [[AI Citation Mechanics]] when answer passages are created or changed.
- Source refresh should connect to [[Research Pack Index]] when a dated claim is older than its cadence.
- The note should not create a publishing action by itself.
- The note should create a clear next decision, owner, and evidence state.

## Current Fact Anchors
- Google helpful content guidance, retrieved 2026-07-06, is the baseline for original, people-first usefulness.
- Google AI optimization guidance, updated 2026-06-15, says Google Search does not need special AI files, special AI schema, Markdown conversion, or llms.txt for AI features.
- SparkToro, 2026-06-09, records 68.01 percent US Google zero click searches for January through April 2026, so planning must include visibility beyond clicks.
- Seer, 2026-04-24, records cited AI Overview pages with about 120 percent more clicks per impression than pages not cited in its analysis.
- Google I/O Search update, 2026-05-19, reports AI Mode passed 1B monthly users, while the substrate records about 0.34 percent US query volume.
- The current QRG reference is the 2025-09-11 revision, with no newer substrate revision recorded as of 2026-07-06.
- FAQ rich results were retired for all sites on 2026-05-07, so Article or BlogPosting is the blog schema priority when schema is relevant.
- Passage extractability guidance is practitioner guidance: aim for self-contained answer blocks around 130 to 170 words under clear headings.
- Google AI features documentation, retrieved 2026-07-06, supports standard crawl, index, and preview controls for AI feature visibility.
- Google Search Gallery, retrieved 2026-07-06, is the supported rich result type reference when a brief requests schema.
- Use first-party GSC, GA4, and crawl evidence when available instead of replacing local data with market averages.
- Treat practitioner studies as planning context unless an official source or property data confirms the exact claim.

## Required Inputs
- Target topic, article, cluster, or workflow item that needs Outline QA Checklist.
- Parent hub context from [[SERP-Informed Briefs and Outlines]].
- Reader problem and intended outcome in one sentence.
- Primary query, entity, or channel that triggered the work.
- Known source URLs with retrieval dates for every current claim.
- First-party data availability, including GSC, GA4, crawl data, or none.
- Existing internal links and candidate links that affect the decision.
- YMYL, legal, medical, financial, or reputation sensitivity flags.
- Schema, media, and author requirements if the note affects a published page.
- Approval owner for changes that affect live content.
- Rollback trigger if the recommendation is later implemented.
- Metric set for review: must-answer coverage, link coverage, source coverage, and risk status.

## Operating Procedure
- Start with the precise decision that Outline QA Checklist must make.
- Restate the scope so it cannot drift beyond [[SERP-Informed Briefs and Outlines]].
- List the page, cluster, brief, asset, or workflow item under review.
- Separate observed facts from recommendations before scoring or prioritizing.
- Attach a source URL and date to every current Search, AI, schema, or market claim.
- Prefer official Google, standards body, primary, or vendor documentation for rule-like claims.
- Use practitioner sources only as supporting evidence or workflow guidance.
- Check whether the recommendation depends on zero click behavior, AI Overview citation, or AI Mode exposure.
- If it depends on AI features, state that inclusion cannot be guaranteed.
- If it mentions FAQ rich results, rewrite the point because that visual tactic is retired for all sites.
- If schema is relevant, route the baseline to Article or BlogPosting plus visible entity support.
- If passages are relevant, make the answer block self-contained and cite source context nearby.
- If the work affects trust, route the check through QRG-informed E-E-A-T review.
- If first-party data exists, make it the measurement baseline.
- If first-party data is missing, label the estimate advisory and name the data gap.
- Reject the failure pattern of moving a thin outline into drafting because deadlines are tight.
- Write the recommendation in a way that a reviewer can accept, revise, or reject.
- Close with owner, next action, confidence, and rollback note.

## Acceptance Criteria
- The outline QA checklist names the exact object under review.
- The recommendation has one primary owner.
- Every current factual claim has a dated source URL.
- The note distinguishes verified facts from advisory choices.
- The note states whether property data is available or missing.
- The note uses current Core Web Vitals language if performance is mentioned.
- The note avoids FID as a current quality metric.
- The note avoids FAQ rich result language as a current blog tactic.
- The note avoids llms.txt as a Google Search, AI Overview, or AI Mode requirement.
- The note does not promise rankings, traffic, Discover reach, AI Overview inclusion, or chatbot citation.
- The note contains an explicit confidence label.
- The note contains a rollback or review trigger when live content could change.
- The note links back to the parent hub and at least six sibling spokes.
- The note can be audited without reading private client systems.

## Failure Modes
- A claim is current but has no dated source.
- A market statistic is applied as a property forecast without local data.
- A recommendation treats an SEO tool as access to Google's internal ranking systems.
- A passage is written for extraction but lacks source context.
- A schema recommendation describes hidden or unsupported page content.
- A cluster, brief, score, or workflow step creates thin content rather than useful content.
- A reviewer cannot tell whether a statement is verified or advisory.
- A high-risk change has no rollback note.
- A channel or platform action is implied even though V1 is advisory and read-only toward external systems.
- The note accepts moving a thin outline into drafting because deadlines are tight.
- The note hides unresolved uncertainty instead of naming it.
- The note duplicates another sibling without a clear boundary.

## Handoff
- Send brief structure questions to [[SERP Brief Input Contract]].
- Send evidence and source issues to [[Search Intent Classification]].
- Send quality scoring issues to [[Blog Quality Score]].
- Send citation passage issues to [[AI Citation Mechanics]].
- Send schema issues to [[Blog Schema Stack]].
- Send first-party measurement issues to [[Google Data Integrations]].
- Send freshness and decay issues to [[Freshness and Content Decay]].
- Send voice changes to [[Voice and Style]] when wording or channel tone changes.
- Send visual or media requirements to [[Images Audio and Charts]] when the output needs assets.
- Keep unresolved approval items out of automated publishing paths.
- Record durable outcomes in [[log]] only when the vault owner asks for log maintenance.
- Keep the final status as ready, revise, blocked, or monitor.

## Related Links
- [[SERP-Informed Briefs and Outlines]]
- [[index|Index]]
- [[hot|Hot]]
- [[SERP Brief Input Contract]]
- [[Search Intent Classification]]
- [[Reader Job Statement]]
- [[Competitive Pattern Notes]]
- [[Heading Hierarchy Rules]]
- [[Evidence Block Requirements]]
- [[Brief Source Pack]]
- [[Dual Optimization]]
- [[6-Pillar Dual Optimization]]
- [[Semantic Topic Clusters]]

## Source Notes
- Google helpful content guidance is the primary source for people-first usefulness and source-backed quality.
- Google AI optimization guidance is the primary source for no special AI files, no special AI schema, and the Google llms.txt caveat.
- SparkToro and Seer are used as dated market context, not property forecasts.
- The QRG is used as a quality evaluation framework, not as a direct ranking factor claim.
- ZipTie passage guidance is practitioner guidance for extraction readiness, not an official Google rule.
- Search Gallery and FAQPage documentation control schema and rich result claims when schema appears in this note.

## Maintenance
- Refresh this note when the source ledger refreshes.
- Refresh this note when Google changes AI feature guidance, schema support, spam policy, or QRG references.
- Refresh this note when first-party data contradicts an advisory assumption.
- Keep source URLs in frontmatter aligned with the ledger.
- Do not mark the brain market-ready from this note alone.
- The next review should verify whether must-answer coverage, link coverage, source coverage, and risk status still captures the decision quality.
