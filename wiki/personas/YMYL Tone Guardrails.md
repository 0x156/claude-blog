---
type: spoke
title: "YMYL Tone Guardrails"
domain: "Blog Voice"
status: active
created: 2026-07-06
updated: 2026-07-09
tags: [personas, voice-style, active]
---

# YMYL Tone Guardrails

## YMYL Tone Guardrails Rule Scope

YMYL Tone Guardrails controls voice when blog content could affect money, health, safety, legal rights, civic decisions, or other high-impact choices. The note does not decide the factual answer. It decides whether tone, certainty, examples, and CTA pressure are appropriate for the source quality and reviewer ownership.

### Allowed Actions And Disallowed Actions

Allowed actions include cautious wording, source-date placement, expert-review notes, narrower examples, and clearer "not advice" boundaries where appropriate. Disallowed actions include promises of outcomes, casualizing risk, hiding uncertainty, replacing expert review with generated prose, or turning a checklist into professional advice. Cite `g-helpful-content`, `g-qrg-full`, `g-update-2025-01-23-qrg-update-jan-2025`, and `g-update-2025-09-11-qrg-update-sept-2025` for the review basis; add `g-update-2026-05-15-spam-policies-update-gen-ai-scaled-content` when a generated batch creates sensitive pages without added value.

### Exceptions That Require Approval

Any stronger claim, urgent CTA, personal recommendation, or region-specific regulated example needs a named human owner. Link locale-sensitive cases to [[Locale Voice Adaptation]] and evidence gaps to [[Research Pack Index]].

## YMYL Tone Guardrails Rule Table

| Rule | Evidence source | Applies to | Enforcement | Approval path |
|---|---|---|---|---|
| Put risk before persuasion | `g-qrg-full` | Health, finance, legal, civic, safety | Block hype-led intros | Expert or senior editor |
| Keep source limits visible | `g-helpful-content` | Advice, comparisons, how-to content | Require date and caveat near claim | Factcheck owner |
| Reject low-value generated depth | `g-update-2025-01-23-qrg-update-jan-2025`, `g-update-2026-05-15-spam-policies-update-gen-ai-scaled-content` | AI-assisted drafts | Block filler sections | SEO lead plus editor |
| Expand YMYL awareness for civic and social topics | `g-update-2025-09-11-qrg-update-sept-2025` | Political and social topics | Require extra reviewer note | Policy-aware reviewer |

### Rule, Evidence Source, Applies To, And Enforcement

The guardrail should produce a pass, revise, or block decision. A cautious tone is not enough when the underlying source is too weak; in that case the claim leaves the draft.

## YMYL Tone Guardrails Review And Rollback

Rollback if a reviewer identifies missing professional context, local legal risk, or overconfident wording. Reopen [[Banned Claims And Phrases]] when the same risky phrase appears in multiple drafts.
