---
type: spoke
title: "Cluster Canonical Page Rules"
domain: "Blog Topic Architecture"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [clusters, semantic-clusters, active]
confidence: advisory
---

# Cluster Canonical Page Rules

## Rule Scope For Editorial Owners

This note chooses the page that owns an intent inside a cluster. It does not by itself add redirects, rel canonical tags, CMS edits, or sitemap changes. When implementation is proposed, the reviewer must preserve the read-only boundary and hand the change to a human owner.

### Allowed Actions

Allowed decisions are: nominate a hub as the primary broad-topic owner, assign a spoke to a narrower intent, keep an older article as the canonical editorial owner after refresh, or send conflicting pages into [[Cannibalization Review]]. Helpful-content evidence matters because the owner must add original value for readers rather than merely absorb more keywords. Source ID: `g-helpful-content`.

### Actions Requiring Separate Approval

Technical canonical tags, redirects, noindex decisions, and URL removals are outside this page. If those become necessary, cite the canonicalization source directly and document rollback. Source ID: `g-canonical`.

## Canonical Rule Table

| Rule | Source basis | Applies to | Exception path |
|---|---|---|---|
| One primary page owns one primary intent | `g-helpful-content` | Hub, spoke, or refreshed legacy article | Split when two reader tasks are meaningfully different |
| Canonical owner must be useful without sibling context | `g-helpful-content` | Broad hubs and high-traffic articles | Escalate weak pages to [[Cluster Gap Analysis]] |
| Do not create AI-only cluster requirements | `g-ai-opt-guide`; `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` | Any rule that mentions AI Overview or AI Mode | Route the caveat to [[2026 Google Update Timeline]] |
| Treat click scarcity as planning context | `sparktoro-zero-click-2026` | Forecast notes and prioritization memos | Keep the benchmark in [[AI Citation Mechanics]] rather than repeating the stat here |
| Use technical canonical signals only after content ownership is settled | `g-canonical` | Duplicate URLs, redirect candidates, syndicated variants | Require SEO lead approval and a rollback plan |

## Review And Rollback Path

1. Name the candidate owner and the intent it would own.
2. Confirm the candidate page can answer the broad reader promise better than its siblings.
3. Check that assigning ownership will not erase a useful narrower page.
4. Add source IDs and state whether the decision is content-only or implementation-ready.
5. Define the rollback trigger: ranking loss, GSC query split, reviewer rejection, or new Google guidance.

## Boundary Notes

Do not use llms.txt, Markdown conversion, or special AI schema as a reason to choose a canonical cluster owner. The current Google Search clarification is source-ledger evidence, not an invitation to add new files. The owner choice should make navigation and source-backed usefulness clearer for readers before it helps any search system.
