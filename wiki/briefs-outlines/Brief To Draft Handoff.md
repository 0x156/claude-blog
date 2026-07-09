---
type: spoke
title: "Brief To Draft Handoff"
domain: "Blog Briefs"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [briefs-outlines, serp-briefs, active]
---

# Brief To Draft Handoff

## Brief To Draft Handoff Control Point

This note turns a completed brief into drafting instructions. It is the transfer layer between planning and writing: the drafter receives the reader job, approved outline, mandatory evidence, caveats, voice constraints, internal links, and rejection conditions. The handoff should be specific enough that the first draft does not invent sources or smooth away uncertainty.

Use [[Brief Source Pack]] for approved evidence, [[Brief Risk Notes]] for unresolved warnings, and [[Heading Hierarchy Rules]] for outline shape. Source IDs travel with the claims. `gh-flow-framework` supports disciplined handoff between evidence, instructions, and output. `g-helpful-content` anchors useful original value, `g-ai-opt-guide` keeps AI-facing wording inside Google's Search guidance, and `nng-editorial-heuristics` supports clear reviewer feedback for the drafter.

### What The Drafter Receives

The drafter receives approved claims, answer targets, section roles, examples to avoid, required caveats, and source IDs. They do not receive permission to add new factual claims without routing them back to the evidence gate.

### What Stays With Reviewer

Approval calls, YMYL sensitivity, first-party data gaps, and confidence labels remain with the reviewer until the draft is ready for QA. If a risk is still open, the handoff must say whether writing can proceed with a caveat or must pause.

## Constraint Transfer Table

| Handoff field | Owner | Required source or note | Writer instruction | Stop condition |
| --- | --- | --- | --- | --- |
| Reader job | brief owner | [[Reader Job Statement]] | Open with the reader problem, not an SEO abstraction | Missing success condition |
| Approved evidence | source steward | [[Brief Source Pack]] plus source IDs | Cite only the supplied claim-source pairs | Source ID absent from a factual claim |
| AI feature wording | SEO lead | `g-ai-opt-guide`; dated llms.txt clarification | Say "eligible to be understood and previewed", not "guaranteed to appear" | AI inclusion promise |
| Click context | analyst | Source from [[Brief Source Pack]]; [[Dual Optimization]] | Keep market data caveated and separate from property metrics | Market average used as site forecast |
| Quality bar | editor | `g-helpful-content` | Add original value and satisfy the named reader task | Thin summary of existing SERPs |
| Risk caveats | approver | [[Brief Risk Notes]] | Preserve caveat text until reviewer removes it | Caveat deleted without approval |

## Handoff Procedure

1. Confirm [[Outline QA Checklist]] has no blocker rows open.
2. Paste the reader job, approved H2/H3 outline, required claims, and source IDs into the draft request.
3. Add the caveats that cannot be softened, especially around AI features, zero-click context, and missing property data.
4. Assign a reviewer for any claim marked advisory, contested, or practitioner.
5. Reject the draft request if it asks the writer to infer facts from competitor pages or live SERP appearance.

## Rejection Conditions

Do not send the brief to drafting when the source pack is generic, when a heading asks for unsupported advice, when the reader job is only a keyword phrase, or when the requested angle would overstate AI citation control. Send those issues back to [[Search Intent Classification]], [[Evidence Block Requirements]], or [[Brief Risk Notes]].

## Sources

- `gh-flow-framework`
- `g-helpful-content`
- `g-ai-opt-guide`
- `nng-editorial-heuristics`
