---
type: spoke
title: "Tone By Funnel Stage"
domain: "Blog Voice"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [personas, voice-style, active]
---

# Tone By Funnel Stage

## Tone By Funnel Stage Stage Purpose

Tone By Funnel Stage maps voice to awareness, evaluation, decision, retention, and advocacy contexts. The goal is to match the reader's decision pressure without manufacturing urgency. This note is useful when [[Audience Persona Template]] names the reader stage but the writer still needs tone, CTA, proof, and caveat guidance.

### Trigger And Entry Criteria

Enter this workflow when a brief has a reader job, target stage, primary claim, and source packet. Use `g-helpful-content` for usefulness, `g-qrg-full` for trust and YMYL sensitivity, `nng-editorial-heuristics` for predictable interaction cues, and `g-ai-opt-guide` if the stage includes AI answer review. `g-ai-features` can support Google AI feature context, but it cannot justify a stronger CTA.

### Output Artifact And Exit Criteria

The output is a tone row for the brief: stage, reader question, acceptable confidence, CTA type, proof type, and banned pressure. Exit only when [[Banned Claims And Phrases]] and [[YMYL Tone Guardrails]] do not block the stage framing.

## Tone By Funnel Stage Step Table

| Stage | Input | Evidence | Action | Owner | Handoff |
|---|---|---|---|---|---|
| Awareness | Problem language and low prior knowledge | `g-helpful-content` | Explain terms before advice | Strategist | [[Readability Review]] |
| Evaluation | Alternatives, criteria, objections | `nng-editorial-heuristics` | Compare tradeoffs without hype | Editor | [[Example Selection Rules]] |
| Decision | Proof, implementation risk, reviewer limits | `g-qrg-full` | State conditions and caveats early | Reviewer | [[YMYL Tone Guardrails]] |
| Retention | Existing-user task and support signal | first-party evidence | Use precise, helpful next steps | Customer owner | [[Persona Evidence Packet]] |

### Input, Evidence, Action, Owner, And Handoff

The stage row should say what tone is allowed and what tone is banned. "Confident about the process" is different from "certain about the outcome"; the latter needs evidence the blog usually does not have.

## Tone By Funnel Stage Control Points

Reject stage changes that add scarcity, authority, or fear without a source. Recheck the tone when a draft moves from blog post to distribution asset.
