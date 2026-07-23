# Public Backlog Triage: 2026-07-23

> **Private planning record. No public mutations were performed.** No pull
> request was merged, closed, edited, or commented on, and no issue was closed
> or edited during this review.

This note records the evidence-based disposition of every open pull request
and issue in `AgriciDaniel/claude-blog` when the private v2.1.0 update was
prepared.

## Pull Requests

| Item | Disposition | Reason |
|---|---|---|
| [#48](https://github.com/AgriciDaniel/claude-blog/pull/48) | Supersede with a comprehensive public-only normalization change | The broken public raw installer URL is valid, but the patch does not normalize every marketplace, clone, canonical, and private-membership reference. Private raw URLs remain correct in the private repository. |
| [#47](https://github.com/AgriciDaniel/claude-blog/pull/47) | Adapt privately | Update `google-genai` through the requirement range, hash lock, and audio smoke coverage instead of merging the isolated public pin. |
| [#46](https://github.com/AgriciDaniel/claude-blog/pull/46) | Adapt privately | Update Patchright through the requirement, hash lock, and browser/preflight smoke coverage. |
| [#42](https://github.com/AgriciDaniel/claude-blog/pull/42) | Already fixed privately | The setup-python action is already SHA-pinned at the required revision. |
| [#41](https://github.com/AgriciDaniel/claude-blog/pull/41) | Already fixed privately | The checkout action is already SHA-pinned at the required revision. |
| [#40](https://github.com/AgriciDaniel/claude-blog/pull/40) | Reject | It substitutes project ownership, introduces invalid skill metadata, and removes capabilities and safeguards. |
| [#38](https://github.com/AgriciDaniel/claude-blog/pull/38) | Reject wholesale; useful parts already superseded | The private repository already has the delivery contract, renderer, hero ladder, provenance hardening, redirect refusal, and safe hygiene implementation. The remaining content and Hostinger workflow are unrelated to the plugin. |
| [#37](https://github.com/AgriciDaniel/claude-blog/pull/37) | Reject | It adds an unsolicited external-service handoff and obsolete project counts without independent checks. |
| [#26](https://github.com/AgriciDaniel/claude-blog/pull/26) | Already fixed privately | `sentence-transformers` already has a bounded, newer-compatible range. |
| [#25](https://github.com/AgriciDaniel/claude-blog/pull/25) | Already fixed privately | `google-genai` already has a bounded major range and is refreshed in v2.1.0. |
| [#23](https://github.com/AgriciDaniel/claude-blog/pull/23) | Already fixed privately | Google Ads already has a bounded supported range. |
| [#20](https://github.com/AgriciDaniel/claude-blog/pull/20) | Adapt privately; replace publicly later | The correct public marketplace slug is `claude-blog@agricidaniel-blog`; the public patch itself is conflicted. |
| [#19](https://github.com/AgriciDaniel/claude-blog/pull/19) | Already fixed privately | The private requests floor is newer and bounded. |
| [#18](https://github.com/AgriciDaniel/claude-blog/pull/18) | Already fixed privately | The private google-auth range is newer and bounded. |
| [#17](https://github.com/AgriciDaniel/claude-blog/pull/17) | Already fixed privately | `google-auth-oauthlib` is already at or above 1.3.1 with an upper bound. |
| [#15](https://github.com/AgriciDaniel/claude-blog/pull/15) | Already fixed privately | pytest already uses a bounded range below 10. |
| [#13](https://github.com/AgriciDaniel/claude-blog/pull/13) | Already fixed privately | The NotebookLM environment already pins python-dotenv 1.2.2. |
| [#10](https://github.com/AgriciDaniel/claude-blog/pull/10) | Already fixed privately | language-tool-python already uses a bounded range below 4. |

## Issues

| Item | Disposition | Reason |
|---|---|---|
| [#44](https://github.com/AgriciDaniel/claude-blog/issues/44) | Fixed privately; add regression coverage | PageSpeed results initialize `audit_details`; v2.1.0 adds a response-level regression test. |
| [#36](https://github.com/AgriciDaniel/claude-blog/issues/36) | No engineering action | This is a promotional listing request, not a repository defect. |
| [#33](https://github.com/AgriciDaniel/claude-blog/issues/33) | Mitigation completed privately | Documentation now downloads, optionally verifies, and explicitly runs the PowerShell installer without a pipe-to-execution command. |
| [#29](https://github.com/AgriciDaniel/claude-blog/issues/29) | Adapt and harden privately | Missing dotted parents were handled, but `find_spec` can also raise `ValueError` when `__spec__` is unset. v2.1.0 covers both failure modes. |
| [#22](https://github.com/AgriciDaniel/claude-blog/issues/22) | Already fixed privately | Plugin descriptions are below the registry limit and guarded by tests. |

## Future Public Release

Before a future approved public push, prepare a public worktree and run:

```bash
python3 scripts/validate_public_release.py --root /path/to/public-worktree
```

Only a passing public worktree should be considered for release. This note
does not authorize a public push or any backlog mutation.
