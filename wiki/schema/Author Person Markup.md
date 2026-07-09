---
type: spoke
title: "Author Person Markup"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[Article Schema Baseline]]"
  - "[[Schema And E-E-A-T Alignment]]"
  - "[[E-E-A-T for Blog Content]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# Author Person Markup

## Author Identity Job

Author markup answers one narrow question: which visible person is responsible for this blog post, and how does that person connect to the site's article graph? It supports entity clarity inside [[Blog Schema Stack]], but it is not an E-E-A-T badge and it cannot compensate for a weak byline, absent bio, or unsupported reviewer claim.

Google's general structured-data guidance, source ID `g-intro-sd`, keeps the markup tied to page content. Schema.org, source ID `schema-full`, supplies the Person vocabulary. JSON-LD graph syntax comes from `w3c-jsonld`. Search feature claims still need a current Google feature route through `g-search-gallery`; most author work is about clarity rather than a special visual result.

## Person Property Evidence Map

| Person field | Visible evidence needed | Schema use | Reviewer warning | Source id |
|---|---|---|---|---|
| `name` | Byline or author card uses the same name | Primary Person label linked from Article author | Do not invent full names from initials or staff aliases | `g-intro-sd` |
| `url` | Crawlable author page, team page, or profile URL | Stable author `@id` target when available | A broken or thin author page weakens the graph | `schema-full` |
| `sameAs` | Public profile controlled by the author or brand | Disambiguation only when confidence is high | Avoid random social handles, syndication pages, or scraper bios | `schema-full` |
| `jobTitle` or `affiliation` | Visible bio or site policy states the role | Optional context for expertise and organization relation | Role claims need editorial proof, especially in YMYL-adjacent topics | `g-intro-sd` |
| JSON-LD `@id` | Stable canonical URL or fragment strategy | Connects author across article nodes | Template-generated IDs must not vary per build | `w3c-jsonld` |

## Profile And Byline Consistency Review

1. Compare the rendered byline, author card, and author profile before looking at JSON-LD.
2. Confirm the article node uses the same Person `@id` that the author profile uses.
3. Record any mismatch between displayed role, editorial review claim, and schema field.
4. Send unresolved trust evidence to [[E-E-A-T for Blog Content]] rather than hiding it in markup.

## Unsupported Author Shortcuts

Do not use Person markup to claim medical, legal, financial, or professional authority that the page does not show. Do not attach `sameAs` links because an SEO template has a field to fill. Do not treat an author schema warning as proof of ranking loss or recovery. The Search Gallery is the guardrail for supported Search appearances, while this note remains focused on accurate identity.

## Author Handoff

The handoff should list the accepted Person fields, rejected fields, and any needed author-page edits. If the author is a company, freelancer, syndicated partner, or committee, document that choice before changing the graph. The final recommendation stays advisory until a separate publishing workflow approves template changes.
