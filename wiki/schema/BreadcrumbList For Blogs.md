---
type: spoke
title: "BreadcrumbList For Blogs"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[Article Schema Baseline]]"
  - "[[Internal Link Matrix]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# BreadcrumbList For Blogs

## Breadcrumb Review Job

Breadcrumb schema should mirror the path readers see or the canonical hierarchy the site uses for blog navigation. It is not an internal-linking strategy by itself. [[Blog Schema Stack]] owns the schema relationship, while [[Internal Link Matrix]] owns broader link placement.

The evidence split matters. Google's general guidance, source ID `g-intro-sd`, requires the markup to reflect the page. Search Gallery, source ID `g-search-gallery`, is the supported-feature checkpoint for breadcrumb appearances. Schema.org, source ID `schema-full`, defines `BreadcrumbList` and `ListItem`; JSON-LD serialization follows source ID `w3c-jsonld`.

## BreadcrumbList For Blogs Schema Table

| Breadcrumb element | Required property | Validation target | Warning to log | Source id |
|---|---|---|---|---|
| `BreadcrumbList` | `itemListElement` containing ordered list items | One list represents one visible path | Multiple competing paths can confuse ownership of the article | `schema-full` |
| `ListItem.position` | Integer sequence starting at the first path item | Positions match rendered order | Missing or duplicate positions make the trail unreliable | `schema-full` |
| `ListItem.name` | Visible label or canonical category label | Labels match navigation or taxonomy | Do not use keyword-stuffed labels hidden from readers | `g-intro-sd` |
| `ListItem.item` | Absolute canonical URL for each linked step when applicable | URLs resolve and match canonical hierarchy | Staging URLs and redirect chains should block handoff | `w3c-jsonld` |
| Search support check | Feature appears in current Google gallery | Current Search Gallery review date is recorded | Gallery support is not a guarantee of display | `g-search-gallery` |

## Taxonomy Cases That Need Judgment

A blog often has category pages, topic hubs, and tag archives that could all look like breadcrumb parents. Choose the path that matches the visible template and the editorial hierarchy. If a post belongs to several tags, do not generate several breadcrumb trails unless the page visibly offers several paths and the implementation can support them cleanly.

## Change Triggers

Review this note when categories are renamed, a hub becomes canonical, the CMS changes URL paths, or old posts are migrated. A breadcrumb can stay syntactically valid while pointing to an outdated taxonomy, so validation must include a navigation check and not only a JSON parser.

## Breadcrumb Publishing Boundary

The handoff should list the accepted trail, rejected alternate trails, and any redirect or canonical issue. It does not approve taxonomy restructuring. Escalate large hierarchy changes to cluster planning before updating schema templates.
