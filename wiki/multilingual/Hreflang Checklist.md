---
type: spoke
title: "Hreflang Checklist"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [multilingual, localization, active]
domain: "Multilingual Blog Publishing"
confidence: advisory
related:
  - "[[Multilingual Publishing]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Research Pack Index]]"
  - "[[Voice and Style]]"
  - "[[x-default Handling]]"
  - "[[Locale Intent Research]]"
  - "[[Localized Source Requirements]]"
  - "[[Multilingual Schema Rules]]"
  - "[[Locale Review Workflow]]"
  - "[[Translation Versus Localization]]"
  - "[[Cross Locale Internal Linking]]"
source_urls:
  - "https://developers.google.com/search/docs/specialty/international/localized-versions"
  - "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/essentials/spam-policies"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/"
  - "https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update"
  - "https://blog.google/products-and-platforms/products/search/search-io-2026/"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
  - "https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf"
  - "https://ziptie.dev/blog/google-ai-overviews-source-selection/"
---

# Hreflang Checklist

## Summary
This spoke turns hreflang implementation into a prepublish and audit checklist.
It belongs to [[Multilingual Publishing]] and supports locale-aware translation, hreflang, source fidelity, and regional content quality.
Primary working inputs: URL pairs, language codes, return links, x-default decision.
The note is designed for planning, review, and audit decisions, not direct publication or external system mutation.
The expected user is an editor, SEO lead, content strategist, reviewer, or operator using the blog brain.
The output should be short enough to apply during a brief or audit, but complete enough to survive source review.

## Evidence Anchors
- Google localized versions documentation, retrieved 2026-07-06, is the route for hreflang return links and x-default handling.
- Google multi-regional guidance, retrieved 2026-07-06, is the route for URL structure choices across languages and regions.
- Google spam policies updated 2026-05-15 flag automated transformations, including low-value translations, as a scaled content risk.
- Helpful content guidance retrieved 2026-07-06 applies the same people-first quality bar to translated and localized pages.
- Locale recommendations are advisory until native-language review, legal review where needed, and local source checks are complete.
- As of 2026-07-06, SparkToro reports 68.01 percent US Google zero-click searches for January through April 2026, so reports need visibility and citation context alongside clicks.
- Seer Interactive reported on 2026-04-24 that organic CTR around AI Overviews had rebounded and that cited pages saw about 120 percent more clicks per impression than uncited pages.
- Google I/O Search updates on 2026-05-19 reported AI Mode above 1B monthly users, while the research substrate records about 0.34 percent US query volume, so AI Mode is strategic but not the only planning surface.
- Google FAQPage documentation marks FAQ rich results retired for all sites effective 2026-05-07, so blog schema planning should prioritize Article or BlogPosting with visible helpful content.
- The active QRG reference is the 2025-09-11 revision as of 2026-07-06, and the substrate records no newer QRG revision.
- Google AI optimization guidance updated 2026-06-15 says Google Search does not use llms.txt and does not require special AI schema, Markdown conversion, or chunking files.
- The practical passage extraction target is a self-contained answer block of roughly 130 to 170 words under a clear heading, with source context and entity clarity.

## Required Inputs
- Target language and country or region, written as a precise locale rather than a vague market.
- Canonical source article and the intended localized URL.
- Alternate URL set, including self-reference, return links, and any fallback page.
- Local source list for laws, pricing, product availability, units, dates, and examples.
- Reviewer identity or reviewer role for language quality and source fidelity.
- Schema fields that need localized names, descriptions, URLs, and author details.
- Known YMYL or legal sensitivity that requires escalation before publication.
- Refresh trigger for facts that vary by market or language.

## Workflow
- Define the decision this note supports: turns hreflang implementation into a prepublish and audit checklist.
- Open [[Multilingual Publishing]] and confirm the hub rule that applies before using this spoke.
- Map every localized claim to a source that is valid for the target locale or mark it as an evidence gap.
- Check hreflang only after canonical URLs and locale URL structure are stable.
- Treat translation memory, machine translation, and glossary matches as starting evidence, not final quality.
- Require native or qualified review for idiom, cultural examples, YMYL risk, and legal references.
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
- [[Multilingual Publishing]]
- [[index|Index]]
- [[hot|Hot]]
- [[Research Pack Index]]
- [[Voice and Style]]
- [[x-default Handling]]
- [[Locale Intent Research]]
- [[Localized Source Requirements]]
- [[Multilingual Schema Rules]]
- [[Locale Review Workflow]]
- [[Translation Versus Localization]]
- [[Cross Locale Internal Linking]]

## Source URLs
- https://developers.google.com/search/docs/specialty/international/localized-versions
- https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
- https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- https://blog.google/products-and-platforms/products/search/search-io-2026/
- https://developers.google.com/search/docs/appearance/structured-data/faqpage
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf
- https://ziptie.dev/blog/google-ai-overviews-source-selection/

## Maintenance Notes
- Refresh this note from [[Research Pack Index]] when any listed source changes after 2026-07-06.
- Keep backlink health with [[Multilingual Publishing]], [[index|Index]], and sibling spokes in this folder.
- Keep confidence advisory when source coverage is incomplete, narrow, stale, or practitioner-led.
- Keep confidence verified only for claims directly tied to official, primary, standards, or first-party sources.
- Do not record secrets, tokens, private exports, or private client details in this note.
- Do not publish or mutate CMS, GSC, GA4, Search Console, analytics, schema, sitemap, or platform settings from this note.
