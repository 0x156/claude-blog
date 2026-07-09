---
type: spoke
title: "FLOW Brief Stage"
domain: "Blog Workflow"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [flow, active]
confidence: advisory
related:
  - "[[FLOW Framework]]"
  - "[[FLOW Source Intake]]"
  - "[[FLOW Draft Stage]]"
  - "[[SERP-Informed Briefs and Outlines]]"
  - "[[AI Citation Mechanics]]"
---

# FLOW Brief Stage

## Brief Stage Job

FLOW Brief Stage turns a source packet and reader problem into a draftable brief. It sits between [[FLOW Source Intake]] and [[FLOW Draft Stage]], so its job is not to write the article. It decides what the draft must answer, which evidence is allowed, which claims need caution, and which handoffs are blocked until a human owner resolves the gap.

### Trigger And Entry Criteria

Enter this stage when the topic, target reader, source IDs, and intended artifact are known. The brief may cite Google helpful-content guidance for reader value and usefulness checks (source_id: `g-helpful-content`). AI visibility instructions use Google's AI feature documentation for surface boundaries (source_id: `g-ai-features`). Passage-level answer blocks remain practitioner guidance and need that label when used (source_id: `ziptie-aio-source-selection`). Zero-click research can shape distribution framing, but it should point to [[AI Citation Mechanics]] and not become a traffic forecast (source_id: `sparktoro-zero-click-2026`).

### Output Artifact And Exit Criteria

The exit artifact is a brief with a reader job, answer promise, claim inventory, source list, excluded claims, internal link targets, and owner notes. It exits only when a draft owner can write without guessing source authority or Search policy.

## FLOW Brief Stage Step Table

| Step | Input | Evidence required | Produced artifact | Downstream handoff |
|---|---|---|---|---|
| 1. Frame the reader job | Topic, audience, search intent | `g-helpful-content` plus local persona notes | One-sentence reader task | [[FLOW Draft Stage]] |
| 2. Bind source claims | Source intake packet | Source IDs, dates, verdicts, limitations | Claim inventory with allowed use | [[FLOW Confidence Tags]] |
| 3. Separate AI Search guidance | AI or GEO requirement in the request | `g-ai-features`, `ziptie-aio-source-selection` if passage tactics appear | AI caveat block for the brief | [[AI Citation Mechanics]] |
| 4. Decide market-context use | Zero-click or distribution assumption | `sparktoro-zero-click-2026` with AS-REPORTED scope | Advisory planning note | [[FLOW Report Stage]] |
| 5. Name draft constraints | Voice, structure, internal links, exclusions | Accepted source and link list | Draft-ready brief packet | [[FLOW Draft Stage]] |

## Input, Evidence, Action, Owner, And Handoff

The brief owner records who supplied the source packet, who accepts the framing, and who will draft. If first-party GSC, analytics, or crawl evidence exists, the brief names it separately from market studies. If it does not exist, the brief says that property evidence is missing rather than filling the gap with a public benchmark.

## FLOW Brief Stage Control Points

Reject the brief if it asks the writer to prove a result the evidence does not support, if it treats panel research as client data, or if it describes a Google AI file as required. Send those items back to [[FLOW Source Intake]] or forward them to [[FLOW Approval Queue]] when a stakeholder must decide whether to keep an advisory assumption.
