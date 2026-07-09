---
type: spoke
title: "VideoObject For Blog Posts"
status: evergreen
created: 2026-07-06
updated: 2026-07-09
tags: [schema, blog-schema, evergreen]
domain: "Blog Structured Data"
confidence: verified
related:
  - "[[Blog Schema Stack]]"
  - "[[Images Audio and Charts]]"
  - "[[Article Schema Baseline]]"
source_urls:
  - "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
  - "https://developers.google.com/search/docs/appearance/structured-data/search-gallery"
  - "https://schema.org/docs/full.html"
  - "https://www.w3.org/TR/json-ld11/"
---
# VideoObject For Blog Posts

## VideoObject Decision Job

VideoObject is an add-on for blog posts that visibly contain a meaningful video. It should not be added to every article template, to decorative embeds, or to a page that only links to a video elsewhere. [[Images Audio and Charts]] owns media quality and accessibility; this note owns the structured-data decision.

Use `g-intro-sd` to keep markup aligned with visible media, `schema-full` for VideoObject vocabulary, `w3c-jsonld` for graph syntax, and `g-search-gallery` before discussing a Google Search video appearance.

## VideoObject For Blog Posts Schema Table

| Video situation | Required property or proof | Validation target | Warning to record | Source id |
|---|---|---|---|---|
| Original embedded explainer | Video is visible, playable, and central to the article | Article body and player render in final HTML | Do not mark a hidden or lazy-failed player as a video | `g-intro-sd` |
| Hosted video with thumbnail | Name, description, thumbnail URL, upload date when available | VideoObject fields match visible media and asset metadata | Thumbnail and upload date should not be invented | `schema-full` |
| Third-party embed | Embed URL, visible player, and rights or platform context | JSON-LD links the article and video consistently | Platform embed changes can stale the graph | `w3c-jsonld` |
| Short decorative clip | Usually no VideoObject | Editorial value is incidental | Decorative motion should stay outside schema | `g-intro-sd` |
| Search feature claim | Current gallery confirms relevant support | Search Gallery reviewed on current source date | Eligibility language is not a guarantee of display | `g-search-gallery` |

## Qualification Procedure

1. Watch or inspect the video enough to confirm it supports the article's reader task.
2. Verify the player, thumbnail, transcript or caption availability, and publication metadata.
3. Connect the VideoObject to the article graph only after the media facts pass review.
4. Escalate rights, accessibility, and production gaps to [[Images Audio and Charts]].

## Cases To Reject

Reject VideoObject when the page has only a text link, a broken embed, a background animation, an unrelated product demo, or a video whose title and thumbnail do not match the article. Also reject it when the CMS would emit the same video node on every post.

## VideoObject Publishing Boundary

The handoff should say VideoObject accepted, rejected, or deferred. Accepted handoffs list the visible video, fields used, validation result, and owner for future media changes.
