---
type: spoke
title: "BlogPosting Versus Article"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[Article Schema Baseline]]"
  - "[[JSON-LD Publishing Checklist]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# BlogPosting Versus Article

## Type Choice Question

The review decides whether a blog page should use `BlogPosting`, `Article`, or a more specific article subtype already used by the site. The choice should describe the content model, not chase a surface-level advantage. In Schema.org's vocabulary, source ID `schema-full`, `BlogPosting` is a narrower article-like type for blog posts, while `Article` remains the broader fallback when the site does not distinguish formats.

Google's structured-data guidance, source ID `g-intro-sd`, keeps the choice anchored to what the page actually contains. Google Search Gallery, source ID `g-search-gallery`, is the check before anyone says the selected type has a current Search appearance. JSON-LD syntax and graph linking use source ID `w3c-jsonld`.

## Decision Table For Article Types

| Page situation | Preferred type | Required properties to inspect | Validation target | Warning | Source id |
|---|---|---|---|---|---|
| Standard editorial blog post | `BlogPosting` | Headline, dates, author, publisher, image when visible | Template graph and rendered article | Use only if the site treats the page as a blog post | `schema-full` |
| Newsroom, magazine, or evergreen article outside the blog | `Article` | Same baseline fields plus section or series context if visible | Article node connected to publisher | Do not force BlogPosting onto non-blog content | `schema-full` |
| How-to style article with steps | `Article` unless a current supported feature applies | Visible steps, author, dates, page purpose | Search Gallery support check | Procedural content does not automatically justify legacy rich-result language | `g-search-gallery` |
| Syndicated or partner article | `Article` with careful author and publisher links | Original source, visible byline, canonical policy | Rendered page and canonical note | Do not blur author, publisher, and host site identity | `g-intro-sd` |
| CMS template cannot vary by format | One consistent site-level article type | Stable `@id`, fields, and visible-content match | JSON-LD parse plus sample pages | Consistency beats per-page guessing when evidence is thin | `w3c-jsonld` |

## Local Convention Check

Before changing type, inspect three existing posts that already validate. If they all use `BlogPosting`, keep the pattern unless the reviewed page is clearly not a blog post. If the site uses `Article` everywhere, document the convention and focus on field accuracy. Type churn can create noisy diffs without improving the graph.

## Unsupported Type Arguments

Reject arguments that claim one type will rank better without a dated source. Also reject "Schema.org allows it" as proof that Google Search displays it. Vocabulary fit and Search support are separate checks, so the final note should cite the vocabulary source and the Search Gallery source separately.

## Handoff For Type Selection

The deliverable is a one-line type decision, the reason, the checked sample pages, and any template constraints. Send field completeness to [[Article Schema Baseline]] and syntax evidence to [[JSON-LD Publishing Checklist]].
