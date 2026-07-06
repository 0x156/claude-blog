"""Tests for the AI citation probability scorer."""

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import ai_citation_score


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "ai_citation_score.py"
FRONTMATTER_BOUNDARY = "-" * 3


HIGH_QUALITY_POST = f"""{FRONTMATTER_BOUNDARY}
title: AI Citation Optimization Benchmarks for 2026
description: Evidence-backed benchmarks for increasing AI citation probability across Google, Perplexity, and ChatGPT.
author: Jane Doe
date: 2026-01-15
lastUpdated: 2026-06-20
{FRONTMATTER_BOUNDARY}

# AI Citation Optimization Benchmarks for 2026

TL;DR: AI citation optimization works best when a post gives a direct answer, cites authoritative sources, defines entities, and keeps data fresh.

## What raises AI citation probability?

AI citation probability rises when a page gives a complete answer in one extractable passage. **AI citation probability** is the estimated chance that an answer engine will quote or reference a page for a matching query. In our testing, answer-first sections worked best when the first paragraph named the entity, gave the direct answer, added a current statistic, and linked to the source. A 2026 review found that 68% of cited passages included a direct definition and a source link [NIH research](https://nih.gov/example-ai-citations). A second benchmark found 54% better retrieval when headings used questions [Stanford study](https://stanford.edu/example-study). The strongest posts also used short paragraphs, one idea per section, and a summary list that a model can lift without extra context. This paragraph is intentionally self-contained so an answer engine can cite it without reading the rest of the article.

## How should sources be added?

Every statistic should sit beside its source. A 2026 newsroom sample found 41% more citations when articles linked to primary data [Reuters analysis](https://reuters.com/example-ai-study). A public health review found 33% fewer hallucinated summaries when sources were named near the claim [CDC guidance](https://cdc.gov/example-guidance).

- Define the core entity.
- Put the direct answer first.
- Refresh the date when facts change.

## FAQ

### What is a citable passage?

A citable passage is a short, self-contained answer that names the topic, explains the claim, and includes enough context for reuse.

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "AI Citation Optimization Benchmarks for 2026",
  "author": {{"@type": "Person", "name": "Jane Doe"}},
  "dateModified": "2026-06-20"
}}
</script>
"""


THIN_POST = """# Short Update

This post says AI citations matter. It has no source links, no schema, and no clear answer structure.
"""


def _write_post(tmp_path: Path, name: str, content: str) -> Path:
    path = tmp_path / name
    path.write_text(content, encoding="utf-8")
    return path


def test_scores_have_expected_shape(tmp_path):
    post = _write_post(tmp_path, "high.md", HIGH_QUALITY_POST)
    result = ai_citation_score.score_file(post)

    assert isinstance(result["overall"], int)
    assert 0 <= result["overall"] <= 100
    assert set(result["engines"]) == {"ai_overview", "perplexity", "chatgpt"}
    assert isinstance(result["factors"], dict)
    assert isinstance(result["recommendations"], list)

    for engine_result in result["engines"].values():
        assert isinstance(engine_result["score"], int)
        assert 0 <= engine_result["score"] <= 100


def test_scoring_is_deterministic(tmp_path):
    post = _write_post(tmp_path, "high.md", HIGH_QUALITY_POST)

    first = ai_citation_score.score_file(post)
    second = ai_citation_score.score_file(post)

    assert first == second


def test_high_quality_fixture_scores_higher_than_thin_fixture(tmp_path):
    high_post = _write_post(tmp_path, "high.md", HIGH_QUALITY_POST)
    thin_post = _write_post(tmp_path, "thin.md", THIN_POST)

    high_score = ai_citation_score.score_file(high_post)["overall"]
    thin_score = ai_citation_score.score_file(thin_post)["overall"]

    assert high_score > thin_score


def test_invalid_utf8_file_returns_structured_error(tmp_path):
    bad_post = tmp_path / "bad.md"
    bad_post.write_bytes(b"# Bad\n\xff\n")

    result = ai_citation_score.score_file(bad_post)

    assert "error" in result
    assert "Could not analyze" in result["error"]


def test_invalid_utf8_cli_exits_cleanly_with_json_error(tmp_path):
    bad_post = tmp_path / "bad.md"
    bad_post.write_bytes(b"# Bad\n\xff\n")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(bad_post)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert "error" in payload
    assert "Could not analyze" in payload["error"]
    assert "Traceback" not in result.stderr
