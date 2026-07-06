"""Adapter tests for the Claude Blog Brain domain pipeline."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from ingest_blog_input import ValidationError, load_blog_input  # noqa: E402
from render_blog_report import render_markdown  # noqa: E402
from synthesize_blog_plan import synthesize  # noqa: E402


FIXTURE = ROOT / "tests" / "fixtures" / "sample-blog-post.json"


def test_blog_adapter_happy_path() -> None:
    record = load_blog_input(FIXTURE)
    plan = synthesize(record)
    report = render_markdown(plan)

    assert record["schema"] == "claude-blog-brain.ingested-blog-post.v1"
    assert record["input"]["target_keyword"] == "AI citation ready blog"
    assert record["provenance"]["source_count"] == 3
    assert plan["schema"] == "claude-blog-brain.blog-optimization-plan.v1"
    assert set(plan["scores"]) >= {"overall", "content", "seo", "eeat", "technical", "ai_citation"}
    assert plan["geo_ai_citation_readiness"]["checks"][0]["name"] == "Passage extractability"
    assert any(item["schema_type"] == "FAQPage caveat" for item in plan["schema_recommendations"])
    assert "<table>" in report
    assert "## Prioritized Recommendations" in report
    assert "`g-helpful-content`" in report
    assert "`g-faqpage-sd`" in report


def test_blog_adapter_determinism() -> None:
    first_record = load_blog_input(FIXTURE)
    second_record = load_blog_input(FIXTURE)
    assert first_record == second_record

    first_plan = synthesize(first_record)
    second_plan = synthesize(second_record)
    assert first_plan == second_plan

    first_report = render_markdown(first_plan)
    second_report = render_markdown(second_plan)
    assert first_report == second_report
    assert "--" not in first_report
    assert "\u2014" not in first_report
    assert "\u2013" not in first_report


def test_blog_adapter_invalid_input_error(tmp_path: Path) -> None:
    bad_input = tmp_path / "bad-blog-post.json"
    bad_input.write_text(
        json.dumps(
            {
                "url": "not a url",
                "target_keyword": "AI citation ready blog",
                "locale": "english",
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValidationError) as excinfo:
        load_blog_input(bad_input)

    message = str(excinfo.value)
    assert "missing required key: title" in message
    assert "one of body_markdown or body_html is required" in message
    assert "url must be an absolute URI" in message
