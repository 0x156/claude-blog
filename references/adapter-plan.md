# Claude Blog Brain Adapter Plan

Status: market-ready. Domain code adapters are implemented, CLI-wired, and test-covered.

## Current Adapter Honesty

`references/adapter-manifest.json` sets `generic_only` to false because the blog
domain importer, synthesis module, and report renderer are implemented, CLI-wired,
and covered by tests. The orchestrator has reconciled maturity to market-ready. The adapter evidence now covers the importer, synthesis module,
renderer, fixture, package CLI, malformed-input envelopes, deterministic output,
and output-file assertions for the supported blog JSON input type.

## Raw Input Types

- Blog post audit input using `schemas/blog-post-input.schema.json`.
- Markdown blog post with YAML frontmatter.
- HTML blog post with canonical URL and extracted metadata.
- claude-blog quality report JSON from `scripts/analyze_blog.py`.
- Blog delivery contract output from `scripts/blog_preflight.py`.
- Google algorithm update ledger from `data/google-updates.json`.
- Optional future exports from GSC, PSI, CrUX, GA4, DataForSEO, Ahrefs, and Firecrawl.

## Implemented Input Schema

- Name: `blog-post-input`.
- Path: `schemas/blog-post-input.schema.json`.
- Scope: title, URL, Markdown or HTML body, frontmatter, target keyword, locale, author, dates, source block, and optional audit findings.
- Enforced facts: HTTP(S) URL patterns, ISO date or date-time strings, required
  title, URL, target keyword, locale, and at least one body field.

## Implemented Importer

- `ingest_blog_input`, path `scripts/ingest_blog_input.py`.
- CLI path: `claude-blog-brain blog-ingest`.
- Output schema: `claude-blog-brain.ingested-blog-post.v1`.
- Output facts: normalized headings, sections, links, source counts,
  provenance hashes, date metadata, author signals, and schema hints.

## Implemented Synthesis Module

- `synthesize_blog_plan`, path `scripts/synthesize_blog_plan.py`.
- CLI path: `claude-blog-brain blog-synthesize`.
- Output schema: `claude-blog-brain.blog-optimization-plan.v1`.
- Output facts: five-category blog scorecard, intent and entity coverage,
  GEO and AI citation readiness checks, schema recommendations, prioritized
  recommendations, delivery contract, and source citations.

## Implemented Renderer

- `render_blog_report`, path `scripts/render_blog_report.py`.
- CLI path: `claude-blog-brain blog-report`.
- Output format: Markdown report with scorecard, delivery verdict, prioritized
  recommendations, GEO and AI citation readiness, schema recommendations, and
  source citations.

## Implemented Fixture

- `sample-blog-post`, path `tests/fixtures/sample-blog-post.json`.
- Later fixtures may cover blog audits, Google update ledgers, and claude-blog
  reference packs after the first input type is release-verified.

## Implemented Tests

- `valid_input`, path `tests/test_blog_adapters.py`.
- `malformed_input_json_error_envelope`, path `tests/test_blog_adapters.py`.
- `output_file_assertions`, path `tests/test_blog_adapters.py`.
- `deterministic_output`, path `tests/test_blog_adapters.py`.
- `domain_specific_end_to_end_output`, path `tests/test_blog_adapters.py`.
- `citation_coverage`, path `tests/test_blog_adapters.py`.
- `operator_supplied_uncited_audit_finding`, path `tests/test_blog_adapters.py`.
- `invalid_date_and_url_rejection`, path `tests/test_blog_adapters.py`.
- `package_cli_blog_subcommands`, path `tests/test_blog_adapters.py`.
- `package_cli_blog_pipeline`, path `tests/test_blog_adapters.py`.

## Safety Requirements

- Reject credentials and private client data in fixtures.
- Preserve raw inputs before transformation.
- Cite every recommendation to `references/source-ledger.json`.
- Keep advice read-only unless a future release defines approval, mutation, and rollback.
- Treat missing source dates, deprecated schema advice, fabricated statistics, and unsupported GEO promises as blocking defects.
- Reject non-HTTP(S) URLs, localhost, private IP ranges, link-local IPs,
  credential-bearing URLs, and redirect chains that resolve into blocked ranges.
- Normalize local paths as vault-relative paths, reject absolute paths and `..`,
  and never follow symlinks outside the allowed raw-source lane.
- Sanitize HTML before extraction or report rendering by removing scripts, event
  handlers, unsafe URL schemes, remote executable embeds, and style injection.
- Scrub rendered outputs for local absolute paths, secrets, cookies, private draft
  URLs, and raw private client content.

## Completion Gate

Domain-adapted maturity requires one implemented importer, one implemented
synthesis module, one implemented report renderer, one fixture per supported
input type, and tests for valid input, malformed input, rendering, credentials
boundary, deterministic output, and citation coverage.
