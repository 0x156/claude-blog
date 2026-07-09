---
type: spoke
title: "FLOW Draft Stage"
domain: "Blog Workflow"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [flow, active]
confidence: advisory
related:
  - "[[FLOW Framework]]"
  - "[[FLOW Brief Stage]]"
  - "[[FLOW Review Stage]]"
  - "[[Voice and Style]]"
  - "[[AI Citation Mechanics]]"
---

# FLOW Draft Stage

## Drafting Boundary

FLOW Draft Stage creates the article, section, or rewrite text from an approved brief. It does not broaden claims, add new statistics, or turn advisory assumptions into facts. The stage protects the brief's reader job, source limits, voice constraints, internal links, and confidence tags while moving from outline to prose.

## Section Build Table

| Draft component | Required input | Evidence held constant | Draft action | Owner | Handoff |
|---|---|---|---|---|---|
| Lead answer | Brief promise and reader task | `g-helpful-content` | State the useful answer before supporting detail | Writer | [[FLOW Review Stage]] |
| AI search caveat | Brief note on AI visibility | `g-ai-features` | Avoid adding unsupported AI visibility claims | Writer | [[FLOW Factcheck Stage]] |
| Extractable answer block | Existing draft or source warning | `ziptie-aio-source-selection` as practitioner evidence | Keep the answer self-contained under a clear heading | SEO reviewer | [[AI Citation Mechanics]] |
| Market context paragraph | Approved planning note | Brief source packet only | Describe the planning environment with method caveat | Strategy editor | [[AI Citation Mechanics]] |
| Source-bound examples | Source packet, customer-neutral examples | Accepted source IDs only | Explain without inventing proof | Writer | [[FLOW Factcheck Stage]] |

## Claim Preservation Rules

Every factual sentence that depends on current Search behavior, AI visibility, source methodology, or quality guidance must remain traceable to the brief. If the draft needs a new factual claim, the writer pauses and sends that claim to [[FLOW Source Intake]] instead of adding a plausible line from memory. This is especially important for AI citation language, where the draft may optimize clarity but cannot promise inclusion.

## Voice And Structure Controls

Use [[Voice and Style]] for phrasing, but do not let voice edits soften limitations. If a statistic or policy caveat feels too heavy in the paragraph, move it into a short source note rather than deleting it. The useful-content lens from `g-helpful-content` favors original, reader-serving explanation. AI feature wording stays inside `g-ai-features`, while extraction tactics from `ziptie-aio-source-selection` stay labeled as practitioner guidance.

## Handoff To Review

The draft exits with a claim map, source IDs used, open questions, and any lines the writer intentionally left advisory. [[FLOW Review Stage]] checks usefulness and structure; [[FLOW Factcheck Stage]] checks current claims and citations.
