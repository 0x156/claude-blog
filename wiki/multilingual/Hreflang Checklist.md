---
type: spoke
title: "Hreflang Checklist"
domain: "Multilingual Blog Publishing"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [multilingual, hreflang, technical-seo, active]
source_urls:
  - "https://developers.google.com/search/docs/specialty/international/localized-versions"
  - "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"
  - "https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls"
  - "https://www.sitemaps.org/protocol.html"
---

# Hreflang Checklist

## Review Gate

This checklist turns hreflang from a vague international SEO task into a prepublish and audit gate. It belongs after URL structure and canonical decisions are stable, but before [[Locale Launch QA]] signs off. The checklist does not decide whether content deserves a locale page. That decision belongs to [[Translation Versus Localization]] and [[Locale Intent Research]].

Use `g-localized` for annotation rules, `g-multiregional` for site targeting context, `g-canonical` for duplicate URL consolidation, and `sitemaps-org` when the alternate set is delivered through XML sitemaps.

### Inputs Required Before Review

The reviewer needs the canonical URL, every alternate URL, language or language-region codes, the self-referencing alternate, the return-link proof, sitemap location if used, and the owner who can fix templates or publishing data.

### Checks Unique To This Gate

Do not mix review of translated quality into this gate. Hreflang review asks whether Google can understand language and regional alternates, whether every alternate returns the relationship, and whether canonical signals conflict with that relationship.

## Hreflang Pass Fail Table

| Check | Evidence to inspect | Pass state | Severity if failed | Fix owner |
|---|---|---|---|---|
| Self-reference | HTML head or sitemap entry | Current page names itself in the alternate set | Major | SEO lead |
| Return links | Each alternate URL | Every alternate points back to this URL | Blocker | Template owner |
| Code precision | Locale map | Language-only or language-region code matches targeting | Major | Locale SEO |
| Canonical alignment | Canonical tag and redirects | Canonical points to the same localized page, not a different language | Blocker | Technical SEO |
| Sitemap syntax | XML sitemap if used | Alternate entries are attached to the correct URL node | Major | Platform owner |
| x-default | Fallback page decision | Selector or neutral fallback appears only when justified | Minor or Major | International SEO |

## Handoff Rules

1. Block launch when canonicalization contradicts hreflang.
2. Return language-quality concerns to [[Locale Review Workflow]] instead of hiding them in this technical checklist.
3. Send fallback decisions to [[x-default Handling]] when the page is a selector, global default, or language-neutral landing page.
4. Record unresolved alternates as an evidence gap, not as a soft pass.

## Evidence Notes

The strongest claim this note can make is operational: the alternate set is internally consistent against the cited rules. It cannot claim ranking lift, traffic recovery, or automatic correct-country serving.
