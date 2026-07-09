---
type: spoke
title: "Internal Link Matrix"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Internal Link Matrix

## Link Assignment Job

This note assigns intentional links among the hub, spokes, and sibling pages in a cluster. The output is an internal link matrix with anchor purpose, destination, evidence, owner, and review date.

### Link Types This Matrix Owns

The matrix owns hub-to-spoke navigation links, spoke-to-hub return links, sibling links for adjacent tasks, and corrective links when canonical ownership is unclear. It does not implement redirects or rel canonical tags, though those signals may be part of a separate technical review. Source ID: `g-canonical`.

### Bad Link Patterns

Avoid repeating the same keyword anchor across every spoke, linking to thin pages, or using market visibility pressure as a reason to add irrelevant links. Helpful content still decides whether a link helps the reader move to the next useful page. Source ID: `g-helpful-content`.

## Link Matrix Table

| Link role | From page | To page | Anchor rule | Evidence | Source IDs |
|---|---|---|---|---|---|
| Hub to spoke | Hub overview | Narrow task page | Descriptive task phrase, not exact-match stuffing | Spoke solves a distinct task | `g-helpful-content` |
| Spoke to hub | Support article | Cluster hub | Broad topic phrase or "topic guide" equivalent | Hub explains context and siblings | `g-helpful-content` |
| Sibling to sibling | Task page | Adjacent task or comparison | Natural next-step language | Reader sequence or funnel path | `g-gsc-api` when data exists |
| Canonical cleanup | Duplicate or near duplicate | Declared owner | Clarify preferred reader path | Content owner and URL signals reviewed | `g-canonical` |
| AI surface context | Any answer-rich page | Source-backed explainer | Link only when it helps verification | Standard crawling and preview posture | `g-ai-features`; `sparktoro-zero-click-2026` |

## Audit Procedure

1. Start from the chosen hub and list every spoke that should be reachable within one click.
2. Record the exact anchor text proposed for each direction.
3. Compare GSC page-query evidence where available before changing high-value links.
4. Send duplicate-owner conflicts to [[Cannibalization Review]].
5. Recheck the matrix after hub selection, page pruning, or major refresh work.

## Measurement Note

Search Console data can show query, page, CTR, and position patterns, but it does not prove why a link changed performance. Use `g-gsc-api` for measurement fields and keep the causal claim conservative.
