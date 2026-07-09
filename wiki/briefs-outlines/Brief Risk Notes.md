---
type: spoke
title: "Brief Risk Notes"
domain: "Blog Briefs"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [briefs-outlines, serp-briefs, active]
---

# Brief Risk Notes

## Brief Risk Notes Planning Job

This note owns the risk register that travels with a SERP-informed brief. It is not the place to fix the outline or rewrite the article. Its job is to make uncertainty visible before drafting starts, especially when the brief touches YMYL-adjacent advice, stale statistics, non-Google AI tactics, or market data that could be mistaken for property performance.

Risk notes should point reviewers to the canonical hub rather than restating broad evidence. Use [[AI Citation Mechanics]] for Google AI feature constraints, [[Dual Optimization]] for zero-click and click-planning context, and [[2026 Google Update Timeline]] when the concern is tied to a dated Google Search change. Cite `sparktoro-zero-click-2026` only as market context, and use `g-qrg-full` when the brief enters trust or YMYL sensitivity.

### Risk Register Boundary

Record only risks that can change the brief, block drafting, or force a named caveat. Minor wording preferences belong in [[Brief To Draft Handoff]], and missing sources belong in [[Brief Source Pack]] unless the absence creates approval risk.

### Approval Triggers

Require owner review when a claim depends on practitioner data, when a recommendation implies Google AI feature eligibility, or when the source is older than its refresh cadence. `g-spam-policies` covers scaled-content and abuse risk, while `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` blocks unsupported AI-file requirements for Google Search.

## Reader Intent Signals And Exposure Caveats

Risk scoring starts with the reader decision the brief will influence. A high-volume query is not enough. The reviewer should know whether the reader is choosing a tool, handling a compliance concern, comparing options, or solving a time-sensitive problem. If the likely search journey may end without a site visit, the brief still needs a useful answer path and a measurement caveat tied to [[Dual Optimization]].

## Brief Risk Notes Planning Table

| Risk field | Owner | Source requirement | Acceptance check | Draft handoff state |
| --- | --- | --- | --- | --- |
| YMYL or reputation sensitivity | editor | `g-qrg-full` plus an expert or policy source for the topic | Risk note names who must approve the claim before drafting | Blocked until owner signs off |
| AI feature tactic | SEO lead | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` when the tactic mentions special files | No claim says a file, schema, or formatting trick guarantees AI visibility | Ready with caveat |
| Market behavior statistic | analyst | `sparktoro-zero-click-2026` with method limits | The note says market panel, geography, and that first-party data wins | Advisory only |
| Outdated Search guidance | source steward | `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search` or newer ledger entry | Refresh due date is named and routed to [[Research Pack Index]] | Monitor |
| Unapproved factual claim | brief owner | Source ID from [[Brief Source Pack]] | Claim has a verdict label from the claim-ledger discipline | Revise before draft |

## Brief Risk Notes Acceptance Procedure

1. Name the exact brief, page, cluster, or outline section affected by the risk.
2. Classify the risk as blocker, caveat, monitor, or no action.
3. Attach at least one source ID and state whether the evidence is official, primary, or practitioner.
4. Decide who can approve the risk and what wording the drafter must preserve.
5. Send unresolved source gaps to [[Brief Source Pack]] and unresolved structure gaps to [[Outline QA Checklist]].

## Sources

- `g-qrg-full`
- `g-spam-policies`
- `g-update-2026-06-15-llms-txt-clarified-as-unused-by-google-search`
- `sparktoro-zero-click-2026`

## Related Routes

[[SERP-Informed Briefs and Outlines]] owns the parent workflow. [[Evidence Block Requirements]] decides source strength for individual claims. [[SERP Observation Ledger]] holds dated SERP observations without turning them into ranking facts.
