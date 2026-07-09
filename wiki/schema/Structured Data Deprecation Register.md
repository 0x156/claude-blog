---
type: spoke
title: "Structured Data Deprecation Register"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Article Schema Baseline]]"
  - "[[BlogPosting Versus Article]]"
  - "[[Author Person Markup]]"
  - "[[Organization Entity Graph]]"
  - "[[BreadcrumbList For Blogs]]"
  - "[[Visible Q And A Without FAQ Rich Results]]"
  - "[[VideoObject For Blog Posts]]"
  - "[[Product Mentions In Blog Schema]]"
  - "[[Dual Optimization]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://developers.google.com/search/updates"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
  - "https://developers.google.com/search/docs/appearance/structured-data/product"
  - "https://developers.google.com/search/blog/2023/08/howto-faq-changes"
  - "https://developers.google.com/search/docs/appearance/structured-data/merchant-listing"
---
# Structured Data Deprecation Register

## Summary
Structured Data Deprecation Register is a schema review note for blog schema stack.
It tracks schema features that are retired, limited, or no longer worth selling.
Use it with [[Blog Schema Stack]] when the working unit is a blog post, entity graph, or structured data block.

## Operating Question
- Which structured data advice is outdated or unsupported now?
- The expected output is a deprecation register entry with source date and replacement action.
- The main risk is keeping old rich result tactics in current briefs.
- The reviewer should be able to see the decision, evidence, caveat, and next action without asking for context.
- The note is advisory unless a future approval and publishing workflow changes the V1 boundary.

## Current Evidence Anchors
- Google structured data introduction retrieved 2026-07-09 recommends JSON-LD and requires markup to describe visible content.
- Google Search documentation updates record FAQ rich results retired for all sites effective 2026-05-07.
- Google Search Gallery dated 2026-07-01 in the ledger defines supported rich result types.
- Schema.org full hierarchy and JSON-LD 1.1 provide standards references for vocabulary and serialization.
- Article or BlogPosting with Person, Organization, and BreadcrumbList is the blog priority after FAQ and HowTo visibility loss.
- Rich result eligibility is never a guarantee, and unsupported markup should not be sold as a current Search feature.
- Use dated wording such as retrieved 2026-07-09 when freshness affects the recommendation.
- Route new or disputed evidence through [[Research Pack Index]] rather than relying on prose-only notes.

## Deprecation Register

| Feature | Status | Effective date | Source ID | Source | Replacement action | Impacted templates |
|---|---|---:|---|---|---|---|
| FAQ rich result | Retired for all sites in Google Search. | 2026-05-07 | `g-update-2026-05-07-faq-rich-results-retired` | https://developers.google.com/search/updates#deprecating-the-faq-rich-result-feature | Keep visible Q and A only when it helps readers; do not score FAQPage as a visual rich result tactic. | [[Visible Q And A Without FAQ Rich Results]], [[Blog Schema Stack]], [[Blog Quality Score]] |
| FAQ rich result documentation | Removed from Google Search docs after retirement. | 2026-06-15 | `g-faqpage-sd` | https://developers.google.com/search/updates | Treat docs removal as a separate documentation event from the 2026-05-07 retirement. | [[research-pack-2026-07-06|Research Pack 2026-07-06]], [[Claim To Source Mapping]] |
| HowTo rich result | Deprecated in Google Search after desktop support ended. | 2023-09-13 | `pending:g-howto-rich-result-deprecated` | https://developers.google.com/search/blog/2023/08/howto-faq-changes | Do not add HowTo markup to ordinary blog posts for rich result eligibility; keep procedural content visible for readers when useful. | Blog post schema checklist, [[Blog Schema Stack]], [[Blog Quality Score]] |
| Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement, Vehicle Listing visual features | Phased out from Google Search result support and Search Console rich-result reporting. | 2025-06-19 | `g-update-2025-06-19-structured-data-deprecation` | https://developers.google.com/search/blog/2025/06/simplifying-search-results | Remove from blog promise language unless a current Google feature page applies. | Legacy rich result templates, [[Quality Score Rubric]] |
| Product intro page date | Not a July 2026 update source. Live Product intro page shows last updated 2025-12-10. | 2025-12-10 | `g-product-sd` | https://developers.google.com/search/docs/appearance/structured-data/product | Use for general Product structured data overview only; do not use it as the July 7 event source until the ledger date mismatch is repaired. | [[Product Mentions In Blog Schema]], [[research-pack-2026-07-06|Research Pack 2026-07-06]] |
| Product merchant listing fields | Current but changed with July 7 category and sale duration guidance. | 2026-07-07 | `g-search-docs-updates-2026-07-07-product-structured-data`; `pending:g-merchant-listing` | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing | Use only when visible product content qualifies; review `Product.category`, `validFrom`, `validThrough`, and `priceValidUntil` for ecommerce pages. | [[Product Mentions In Blog Schema]], [[Schema Deprecation Watch]] |
| data-vocabulary.org markup for Google rich results | No longer eligible for Google rich result features. | 2020-04-06 | `pending:g-data-vocabulary-sunset` | https://developers.google.com/search/blog/2020/01/data-vocabulary | Convert old breadcrumb or legacy markup to Schema.org vocabulary. | Legacy schema migrations, [[BreadcrumbList For Blogs]] |

## Operating Standard
- Describe only visible page content in structured data.
- Prefer JSON-LD unless a local platform requires another supported format.
- Use Google Search Central for supported Search features and Schema.org for vocabulary breadth.
- Keep Article or BlogPosting, author identity, publisher identity, and breadcrumbs coherent.
- Avoid presenting FAQPage or HowTo as current blog rich result tactics.
- Use Product or VideoObject only when the page visibly contains qualifying content.
- Keep documentation updates separate from ranking updates in monitoring notes.
- Validate syntax, vocabulary, Google support, and page-content alignment before handoff.
- Treat schema as entity clarity and eligibility support, not a traffic guarantee.
- Keep the recommendation tied to a reader outcome and a measurable review path.
- Do not present advisory workflow guidance as if it were an official ranking factor.

## Review Sequence
1. Open [[Blog Schema Stack]] and confirm the parent workflow still applies.
2. Name the page, section, cluster, or program being reviewed.
3. State the reader task in one sentence.
4. Identify the search or answer surface affected by the decision.
5. Pull the current dated source URLs before editing recommendations.
6. Record whether the evidence is official, first-party, market, or practitioner evidence.
7. Identify what would make the recommendation stale.
8. Decide whether the action is draft, refresh, rewrite, measure, escalate, or defer.
9. Add a confidence label that matches the weakest important evidence source.
10. Link the decision to a sibling spoke that handles the next operational detail.
11. Send unresolved quality issues to [[Blog Quality Score]].
12. Keep the final note read-only toward external systems.

## Specific Checks
- Check that structured data deprecation register is applied to the correct content unit.
- Check that the decision matches this purpose: tracks schema features that are retired, limited, or no longer worth selling.
- Check that the output can be inspected as a deprecation register entry with source date and replacement action.
- Check that the risk is addressed directly: keeping old rich result tactics in current briefs.
- Verify that each marked-up fact is visible to readers.
- Validate JSON-LD syntax before interpreting eligibility.
- Check Google Search Gallery support before promising a feature.
- Use Schema.org vocabulary for entity clarity even when Google has no rich result.
- Keep author, publisher, dates, images, and breadcrumbs consistent with the page.
- Avoid obsolete FAQ and HowTo rich result advice.
- Use Product or VideoObject only for visible qualifying content.
- Record validation evidence and unresolved platform constraints.
- Check that links point to existing notes and not future placeholders.
- Check that source URLs are real ledger URLs with retrieval context.

## Acceptance Criteria
- The article or program owner can understand the recommendation without a meeting.
- The current claim dates are visible enough for a later refresh pass.
- The source posture does not mix official guidance with practitioner evidence.
- The note names the relevant hub and at least one sibling spoke for deeper work.
- The decision can be reversed, revised, or deferred if new evidence appears.
- The recommendation does not mutate a CMS, GSC, GA4, or publishing platform.
- The wording avoids ranking guarantees, traffic guarantees, rich result guarantees, and AI citation guarantees.
- The next action is concrete enough to enter a brief, audit, or editorial queue.

## Failure Modes
- The markup describes content that is not visible on the page.
- A rich result is promised even though Google support has changed.
- FAQPage is retained as a visual SERP tactic after retirement.
- Author or publisher nodes conflict with visible page identity.
- Product markup is added to casual product mentions.
- VideoObject appears without a qualifying visible video.
- The schema validates syntactically but fails editorial alignment.
- The structured data creates a disconnected entity graph.
- The note becomes stale because a Google source changed and no refresh cue was recorded.
- The recommendation sounds polished but cannot be traced to a dated source.

## Handoff
- Attach the schema note to the article template, CMS ticket, or audit report.
- List visible-content dependencies before implementation advice.
- Record validation tools and unresolved warnings.
- Send author and trust issues to [[E-E-A-T for Blog Content]].
- Send media markup questions to [[Images Audio and Charts]].
- Send deprecation questions to [[Google Algorithm Update Ledger]].
- Send citation entity questions to [[AI Citation Mechanics]].
- Score technical readiness through [[Blog Quality Score]].
- Use [[Article Schema Baseline]] when this note needs a sibling follow-up.
- Use [[BlogPosting Versus Article]] when the next decision belongs beside this note.

## Related
- [[Blog Schema Stack]]
- [[index|Index]]
- [[hot|Hot]]
- [[Dual Optimization]]
- [[AI Citation Mechanics]]
- [[E-E-A-T for Blog Content]]
- [[Images Audio and Charts]]
- [[Multilingual Publishing]]
- [[Google Data Integrations]]
- [[Google Algorithm Update Ledger]]
- [[Article Schema Baseline]]
- [[BlogPosting Versus Article]]
- [[Author Person Markup]]
- [[Organization Entity Graph]]
- [[BreadcrumbList For Blogs]]
- [[Visible Q And A Without FAQ Rich Results]]
- [[VideoObject For Blog Posts]]
- [[Product Mentions In Blog Schema]]
- [[Schema Validation Workflow]]
- [[JSON-LD Publishing Checklist]]
- [[Schema And E-E-A-T Alignment]]
