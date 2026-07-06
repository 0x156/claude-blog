---
type: hub
title: "Blog Schema Stack"
status: active
created: 2026-07-06
updated: 2026-07-06
tags: [schema, blog-schema, active]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Index]]"
  - "[[Hot]]"
  - "[[Dual Optimization]]"
  - "[[AI Citation Mechanics]]"
  - "[[E-E-A-T for Blog Content]]"
  - "[[Images Audio and Charts]]"
  - "[[Google Algorithm Update Ledger]]"
  - "[[Research Pack Index]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---

# Blog Schema Stack

## Summary

Blog Schema Stack defines the baseline structured data set for blog posts after FAQ and HowTo rich result visibility loss.

The target is a coherent entity graph, not isolated snippets.

## Current fact anchors

- Google structured data introduction, retrieved 2026-07-06, recommends JSON-LD and requires markup to describe visible content.
- Google FAQPage documentation records FAQ rich results retired for all sites effective 2026-05-07.
- The substrate frames Article or BlogPosting plus Person, Organization, and BreadcrumbList as the blog priority after FAQ and HowTo deprecations.
- Google Search Gallery, dated 2026-07-01 in the ledger, is the authority route for supported rich result types.
- Schema.org and JSON-LD 1.1 provide standards references for vocabulary and serialization.

## Scope

- Define baseline BlogPosting or Article markup.
- Define Person and Organization identity support.
- Define BreadcrumbList requirements.
- Define ImageObject, VideoObject, and Product add-ons when relevant.
- Define visible Q and A content without selling FAQ rich results.
- Define validation paths for Google support and Schema.org vocabulary.
- Connect author trust to [[E-E-A-T for Blog Content]].
- Connect media schema to [[Images Audio and Charts]].

## Future spoke notes

- [[Article Schema Baseline]]
- [[BlogPosting Versus Article]]
- [[Author Person Markup]]
- [[Organization Entity Graph]]
- [[BreadcrumbList For Blogs]]
- [[Visible Q And A Without FAQ Rich Results]]
- [[VideoObject For Blog Posts]]
- [[Product Mentions In Blog Schema]]
- [[Schema Validation Workflow]]
- [[Structured Data Deprecation Register]]

## Entity graph checklist

- The schema describes content visible on the page.
- The author is represented consistently.
- The publisher or organization is represented consistently.
- Dates match visible published and modified dates.
- Images have stable URLs and useful alt context.
- Breadcrumbs match the visible site hierarchy.
- Product or video markup is used only when the page actually contains that content.
- Rich result eligibility is never promised.

## Source posture

- Use Google Search Central for supported Search features.
- Use Schema.org for vocabulary breadth.
- Use W3C JSON-LD for serialization.
- Track deprecations through [[Google Algorithm Update Ledger]].
- Mark practitioner schema prioritization as advisory when it exceeds Google documentation.

## Related themes

- [[Dual Optimization]]
- [[E-E-A-T for Blog Content]]
- [[AI Citation Mechanics]]
- [[Images Audio and Charts]]
- [[Multilingual Publishing]]
- [[Google Data Integrations]]
- [[Google Algorithm Update Ledger]]
- [[Research Pack Index]]

## Sources

- Google structured data introduction, retrieved 2026-07-06.
- Google FAQPage documentation, effective 2026-05-07 for retirement.
- Google Search Gallery, dated 2026-07-01 in the ledger.
- Schema.org full hierarchy, retrieved 2026-07-06.
- JSON-LD 1.1, retrieved 2026-07-06.

## Next actions

- Fill [[Article Schema Baseline]] before generator details.
- Fill [[Structured Data Deprecation Register]] before schema audits.
- Cross-link media requirements to [[Images Audio and Charts]].
