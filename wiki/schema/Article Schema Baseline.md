---
type: spoke
title: "Article Schema Baseline"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[BlogPosting Versus Article]]"
  - "[[Author Person Markup]]"
  - "[[Organization Entity Graph]]"
  - "[[BreadcrumbList For Blogs]]"
  - "[[Schema Validation Workflow]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# Article Schema Baseline

## Baseline Job For Blog Articles

This note defines the smallest useful article node for a normal blog post. The job is not to make every possible Schema.org assertion. It is to make the article, author, publisher, dates, image, and breadcrumb trail legible to machines while matching what a reader can inspect on the page. [[Blog Schema Stack]] owns the overall stack; this note owns the article-level minimum.

Use JSON-LD as the default serialization unless a platform has a documented reason to use another supported format. That preference is grounded in Google's structured-data guidance, source ID `g-intro-sd`, and the JSON-LD syntax baseline is the W3C recommendation, source ID `w3c-jsonld`. Treat Schema.org as the vocabulary reference, source ID `schema-full`, and Google Search Gallery as the Search feature support check, source ID `g-search-gallery`.

## Article Schema Baseline Schema Table

| Schema item | Required or baseline property | Validation target | Warning to record | Source id |
|---|---|---|---|---|
| `Article` or `BlogPosting` | `headline`, `datePublished`, `dateModified` when visible, author, publisher, image when available | Google Rich Results Test plus rendered page comparison | Do not mark dates or titles that differ from the visible article | `g-intro-sd` |
| `Person` author reference | Stable author name and author URL when the site has one | Same `@id` used by the article and author profile | Pseudonyms, ghostwriting, and reviewed-by claims need editorial evidence | `schema-full` |
| `Organization` publisher reference | Brand name, URL, and logo when part of the site identity | Consistent publisher node across templates | Do not swap publisher with sponsor, advertiser, or product brand | `schema-full` |
| `BreadcrumbList` link | Ordered article location in the site hierarchy | Breadcrumb markup matches visible navigation | Category changes can stale the schema before the body changes | `g-search-gallery` |
| JSON-LD graph container | Valid `@context`, `@type`, and stable `@id` values | JSON parser and Rich Results Test syntax pass | A syntactic pass does not prove Search feature eligibility | `w3c-jsonld` |

## Fields That Must Match Visible Content

Check the rendered page before approving the node. The headline should match the article title, not a campaign headline from metadata. The author must be the displayed author or credited organization. Dates should reflect the public published and modified dates, not build time. Image references should point to stable crawlable assets that represent the article. If a field is true internally but absent to readers, leave it out or route it to editorial review.

## Exclusions From The Baseline

Do not add Product, VideoObject, FAQPage, HowTo, Review, Course, or dataset markup just because the article mentions those concepts. Extra types belong in their own review notes and need visible qualifying content. A Schema.org type can be valid vocabulary while still lacking a current Google Search appearance, so Search feature promises must go through `g-search-gallery` and not through vocabulary breadth alone.

## Article Baseline Publishing Boundary

The output is an advisory checklist or JSON-LD review comment. It may identify missing fields, stale IDs, or invalid references, but it does not publish to a CMS. Escalate author identity to [[Author Person Markup]], publisher graph conflicts to [[Organization Entity Graph]], type choice to [[BlogPosting Versus Article]], and validation evidence to [[Schema Validation Workflow]].
