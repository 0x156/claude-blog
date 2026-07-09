---
type: spoke
title: "Outline QA Checklist"
domain: "Blog Briefs"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [briefs-outlines, serp-briefs, active]
---

# Outline QA Checklist

## Outline QA Checklist Review Scope

This is the gate between a planned outline and a draft request. It checks whether the outline has a reader job, coherent heading hierarchy, claim-source mapping, caveats, and handoff-ready constraints. It does not score the finished article and it does not rewrite sections. Failing rows return to the owner of the upstream note.

The review uses `g-helpful-content` to test whether the outline promises useful, original, people-first coverage. `nng-editorial-heuristics` supports checking whether section jobs and reviewer feedback are clear enough to act on. Use `g-update-2026-05-15-new-generative-ai-optimization-guide` to reject AI shortcuts, and use `sparktoro-zero-click-2026` only when success metrics need a low-click caveat.

### Blocking Checks

Block the outline when it lacks a reader job, has unsupported factual headings, treats a SERP observation as a ranking cause, or sends a generic source bundle to the writer.

### Advisory Checks

Flag but do not block when examples are thin, internal links are missing, the market-data caveat needs clearer wording, or the answer blocks are not yet polished.

## Outline QA Pass Fail Table

| Check | Evidence | Severity | Owner | Fix status |
| --- | --- | --- | --- | --- |
| Reader job appears before keyword expansion | [[Reader Job Statement]] | Blocker | brief owner | Return if missing |
| H2s follow distinct section jobs | [[Heading Hierarchy Rules]] | Blocker | outline owner | Revise hierarchy |
| Every factual claim has a source ID or is marked unsourced | [[Evidence Block Requirements]] | Blocker | source steward | Add source or remove claim |
| AI feature language avoids guarantee wording | `g-update-2026-05-15-new-generative-ai-optimization-guide` | Blocker | SEO lead | Narrow wording |
| Quality promise adds original value beyond a SERP summary | `g-helpful-content` | Major | editor | Add experience, comparison, data, or decision support |
| Click and citation goals are not collapsed into one metric | `sparktoro-zero-click-2026`; [[AI Citation Mechanics]] | Major | analyst | Split success criteria |
| Risk register has owner and state | [[Brief Risk Notes]] | Major | approver | Assign caveat or approval |

## Fix Routing Rules

1. Send intent mismatch to [[Search Intent Classification]].
2. Send missing evidence to [[Brief Source Pack]] before asking the drafter to proceed.
3. Send heading drift to [[Heading Hierarchy Rules]] with the exact section that failed.
4. Send risk or caveat disputes to [[Brief Risk Notes]].
5. Send a fully passing outline to [[Brief To Draft Handoff]] with no hidden reviewer-only warnings.

## Sources

- `g-helpful-content`
- `nng-editorial-heuristics`
- `g-update-2026-05-15-new-generative-ai-optimization-guide`
- `sparktoro-zero-click-2026`

## Handoff Rules After QA

The QA result must be one of three states: ready for draft, revise before draft, or blocked for approval. A ready outline includes source IDs, caveats, internal-link targets, and named owners for open advisory items.
