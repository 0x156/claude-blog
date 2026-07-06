---
type: spoke
title: "Stale Claim Register"
status: evergreen
created: 2026-07-06
updated: 2026-07-06
tags: [rewriting, freshness, content-decay, evergreen]
domain: "Blog Rewriting"
confidence: advisory
related:
  - "[[Freshness and Content Decay]]"
  - "[[index|Index]]"
  - "[[hot|Hot]]"
  - "[[Content Decay Detection]]"
  - "[[Refresh Versus Rewrite Decision]]"
  - "[[Source Refresh Workflow]]"
  - "[[Intent Drift Audit]]"
  - "[[Historical Performance Review]]"
  - "[[Content Consolidation Rules]]"
  - "[[Pruning Advisory Checklist]]"
  - "[[Update Timestamp Policy]]"
  - "[[Dual Optimization]]"
source_urls:
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/updates/ranking"
  - "https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history"
  - "https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports"
  - "https://developers.google.com/search/docs/appearance/structured-data/faqpage"
---
# Stale Claim Register

## Summary
Stale Claim Register is a rewrite decision note for freshness and decay.
It captures claims that need source refresh before a rewrite can ship.
Use it with [[Freshness and Content Decay]] when the working unit is a published post, cluster, or decayed section.

## Operating Question
- Which claims are too stale, risky, or unsupported to remain live?
- The expected output is a stale-claim register with owner, source URL, and due date.
- The main risk is letting one outdated claim undermine the whole article.
- The reviewer should be able to see the decision, evidence, caveat, and next action without asking for context.
- The note is advisory unless a future approval and publishing workflow changes the V1 boundary.

## Current Evidence Anchors
- Google helpful content guidance retrieved 2026-07-06 remains the quality baseline for rewriting.
- Google ranking update history dated 2026-05-21 and the Search Status Dashboard are the authority path for confirmed update history.
- The substrate records no Google-owned ranking, spam, schema, QRG, or AI search update from 2026-07-01 through 2026-07-06.
- Search Console generative AI reports were announced in June 2026 for AI Overviews and AI Mode reporting on a subset of properties.
- FAQ rich results were retired effective 2026-05-07, so stale FAQ rich result claims must be removed during rewrites.
- Rewrite actions remain advisory in V1 and should not mutate a CMS or publishing system directly.
- Use dated wording such as retrieved 2026-07-06 when freshness affects the recommendation.
- Route new or disputed evidence through [[Research Pack Index]] rather than relying on prose-only notes.

## Operating Standard
- Separate traffic decay, source staleness, intent drift, schema drift, and trust gaps before recommending work.
- Prefer first-party GSC or analytics evidence over generic market behavior when the property has data.
- Date every claim that could age, including Google update, schema, and AI feature guidance.
- Quarantine unconfirmed volatility until a Google-owned source confirms it.
- Choose refresh, rewrite, merge, prune, or no action from evidence rather than preference.
- Preserve old evidence in the source trail even when a recommendation changes.
- Record reversible decisions with the expected effect and rollback cue.
- Keep all V1 rewrite outputs advisory and read-only toward publishing tools.
- Keep the recommendation tied to a reader outcome and a measurable review path.
- Do not present advisory workflow guidance as if it were an official ranking factor.

## Review Sequence
1. Open [[Freshness and Content Decay]] and confirm the parent workflow still applies.
2. Name the page, section, cluster, or program being reviewed.
3. State the reader task in one sentence.
4. Identify the search or answer surface affected by the decision.
5. Pull the current dated source URLs before editing recommendations.
6. Record whether the evidence is official, first-party, market, or practitioner evidence.
7. Identify what would make the recommendation stale.
8. Decide whether the action is draft, refresh, rewrite, measure, escalate, or defer.
9. Add a confidence label that matches the weakest important evidence source.
10. Link the decision to a sibling spoke that handles the next operational detail.
11. Send unresolved quality issues to [[Blog Quality Score]].
12. Keep the final note read-only toward external systems.

## Specific Checks
- Check that stale claim register is applied to the correct content unit.
- Check that the decision matches this purpose: captures claims that need source refresh before a rewrite can ship.
- Check that the output can be inspected as a stale-claim register with owner, source URL, and due date.
- Check that the risk is addressed directly: letting one outdated claim undermine the whole article.
- Compare the current page against the original intent and the current reader need.
- List stale sources before touching prose.
- Separate ranking volatility from confirmed Google updates.
- Check whether AI feature data exists in Search Console before using market context.
- Document whether the action is reversible.
- Preserve evidence that explains why the old version changed.
- Avoid changing visible timestamps without meaningful review.
- Recommend no action when evidence does not justify work.
- Check that links point to existing notes and not future placeholders.
- Check that source URLs are real ledger URLs with retrieval context.

## Acceptance Criteria
- The article or program owner can understand the recommendation without a meeting.
- The current claim dates are visible enough for a later refresh pass.
- The source posture does not mix official guidance with practitioner evidence.
- The note names the relevant hub and at least one sibling spoke for deeper work.
- The decision can be reversed, revised, or deferred if new evidence appears.
- The recommendation does not mutate a CMS, GSC, GA4, or publishing platform.
- The wording avoids ranking guarantees, traffic guarantees, rich result guarantees, and AI citation guarantees.
- The next action is concrete enough to enter a brief, audit, or editorial queue.

## Failure Modes
- The rewrite is triggered by a single short-term metric dip.
- A date is refreshed cosmetically without meaningful review.
- Old claims remain after the article structure is changed.
- Unconfirmed volatility is treated as a Google update.
- A page is pruned before consolidation or refresh is evaluated.
- The rewrite removes experience evidence that supported trust.
- The new version breaks internal links or schema assumptions.
- No one can tell what should be rolled back if results worsen.
- The note becomes stale because a Google source changed and no refresh cue was recorded.
- The recommendation sounds polished but cannot be traced to a dated source.

## Handoff
- Attach the decision note to the rewrite ticket or editorial plan.
- Preserve source URLs that justify the change.
- Name the owner who approves live content changes outside V1.
- Record the expected measurement window.
- Send source gaps to [[Research Pack Index]].
- Send algorithm questions to [[Google Algorithm Update Ledger]].
- Send data pulls to [[Google Data Integrations]].
- Send final QA to [[Blog Quality Score]].
- Use [[Content Decay Detection]] when this note needs a sibling follow-up.
- Use [[Refresh Versus Rewrite Decision]] when the next decision belongs beside this note.

## Related
- [[Freshness and Content Decay]]
- [[index|Index]]
- [[hot|Hot]]
- [[Dual Optimization]]
- [[Google Algorithm Update Ledger]]
- [[E-E-A-T for Blog Content]]
- [[Google Data Integrations]]
- [[AI Citation Mechanics]]
- [[Blog Schema Stack]]
- [[Blog Quality Score]]
- [[Content Decay Detection]]
- [[Refresh Versus Rewrite Decision]]
- [[Source Refresh Workflow]]
- [[Intent Drift Audit]]
- [[Historical Performance Review]]
- [[Content Consolidation Rules]]
- [[Pruning Advisory Checklist]]
- [[Update Timestamp Policy]]
- [[Rewrite QA Checklist]]
- [[Rewrite Rollback Notes]]
- [[Decay Segment Prioritization]]
