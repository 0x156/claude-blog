---
type: spoke
title: "BreadcrumbList For Blogs"
status: evergreen
created: 2026-07-06
updated: 2026-07-06
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
  - "[[Visible Q And A Without FAQ Rich Results]]"
  - "[[VideoObject For Blog Posts]]"
  - "[[Product Mentions In Blog Schema]]"
  - "[[Schema Validation Workflow]]"
  - "[[Dual Optimization]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
  - "https://developers.google.com/search/docs/appearance/structured-data/product"
---
# BreadcrumbList For Blogs

## Summary
BreadcrumbList For Blogs is a schema review note for blog schema stack.
It aligns BreadcrumbList markup with visible site hierarchy and internal navigation.
Use it with [[Blog Schema Stack]] when the working unit is a blog post, entity graph, or structured data block.

## Operating Question
- Do breadcrumbs match what the reader sees and how the site is organized?
- The expected output is a breadcrumb checklist with hierarchy and URL checks.
- The main risk is using breadcrumbs to invent a hierarchy not visible on the page.
- The reviewer should be able to see the decision, evidence, caveat, and next action without asking for context.
- The note is advisory unless a future approval and publishing workflow changes the V1 boundary.

## Current Evidence Anchors
- Google structured data introduction retrieved 2026-07-06 recommends JSON-LD and requires markup to describe visible content.
- Google FAQPage documentation records FAQ rich results retired for all sites effective 2026-05-07.
- Google Search Gallery dated 2026-07-01 in the ledger defines supported rich result types.
- Schema.org full hierarchy and JSON-LD 1.1 provide standards references for vocabulary and serialization.
- Article or BlogPosting with Person, Organization, and BreadcrumbList is the blog priority after FAQ and HowTo visibility loss.
- Rich result eligibility is never a guarantee, and unsupported markup should not be sold as a current Search feature.
- Use dated wording such as retrieved 2026-07-06 when freshness affects the recommendation.
- Route new or disputed evidence through [[Research Pack Index]] rather than relying on prose-only notes.

## Operating Standard
- Describe only visible page content in structured data.
- Prefer JSON-LD unless a local platform requires another supported format.
- Use Google Search Central for supported Search features and Schema.org for vocabulary breadth.
- Keep Article or BlogPosting, author identity, publisher identity, and breadcrumbs coherent.
- Avoid presenting FAQPage or HowTo as current blog rich result tactics.
- Use Product or VideoObject only when the page visibly contains qualifying content.
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
- Check that breadcrumblist for blogs is applied to the correct content unit.
- Check that the decision matches this purpose: aligns BreadcrumbList markup with visible site hierarchy and internal navigation.
- Check that the output can be inspected as a breadcrumb checklist with hierarchy and URL checks.
- Check that the risk is addressed directly: using breadcrumbs to invent a hierarchy not visible on the page.
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
- [[Visible Q And A Without FAQ Rich Results]]
- [[VideoObject For Blog Posts]]
- [[Product Mentions In Blog Schema]]
- [[Schema Validation Workflow]]
- [[Structured Data Deprecation Register]]
- [[JSON-LD Publishing Checklist]]
- [[Schema And E-E-A-T Alignment]]
