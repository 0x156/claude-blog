---
type: deliverable
title: "Platform Output Formatting Matrix"
domain: "Blog Content Brain"
status: active
created: 2026-07-09
updated: 2026-07-09
tags: [deliverables, platforms, formatting]
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/google-images"
  - "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide"
---

# Platform Output Formatting Matrix

## Formatting Comparison Job

This matrix helps [[Blog Quality Score]] and [[Images Audio and Charts]] hand a finished article to WordPress, MDX, Hugo, Ghost, Astro, Jekyll, 11ty, Gatsby, or static HTML without losing metadata, image context, internal links, or structured-data intent. The source IDs are `g-helpful-content`, `g-intro-sd`, `g-google-images`, and `g-ai-opt-guide`.

## Platform Rows To Include

The matrix records platform-specific output packaging only. It does not claim that any CMS has a ranking advantage. It also avoids special AI-only formatting claims because `g-ai-opt-guide` does not support a separate file or markup requirement for Google AI features.

## Platform Output Formatting Matrix

| Platform | Output wrapper | Metadata handling | Media and schema concern | Handoff check |
|---|---|---|---|---|
| WordPress | HTML body plus CMS fields | Title, slug, excerpt, category, tags | Alt text, captions, JSON-LD placement | Preview before publish |
| MDX | Markdown plus components | Frontmatter fields | Component props must preserve text alternatives | Build preview |
| Hugo | Markdown content file | TOML, YAML, or JSON frontmatter | Shortcodes must not hide primary content | Local render |
| Ghost | HTML or editor import | Slug, excerpt, tags | Cards need accessible media context | Editor preview |
| Astro | MDX or Markdown route | Frontmatter and layout props | Schema may live in layout | Static build |
| Jekyll | Markdown post | YAML frontmatter | Image paths and canonical fields checked | Local build |
| 11ty | Markdown, Nunjucks, or data file | Data cascade fields | Template controls structured data | Local build |
| Gatsby | MDX or CMS source node | GraphQL fields | Image plugin output keeps alt text | Build preview |
| Static HTML | Complete HTML document | Inline head fields | Structured data and image attributes visible | Browser check |

## Interpretation Rules For Platform Exports

Helpful content and source fidelity survive the export only if the platform wrapper preserves headings, citations, media context, and visible text. `g-intro-sd` supports structured-data caution, while `g-google-images` supports image-context checks. If a platform cannot render a required element, the deliverable records a blocker rather than replacing it with decorative formatting.
