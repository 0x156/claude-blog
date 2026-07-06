"""Tests for the blog post quality gate."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import analyze_blog
import quality_gate

FIXTURES = Path(__file__).parent / "fixtures"


def _copy_fixture(name: str, tmp_path: Path) -> Path:
    target = tmp_path / name
    target.write_text((FIXTURES / name).read_text(encoding="utf-8"), encoding="utf-8")
    return target


def test_passing_post_exits_zero(tmp_path, capsys):
    post = _copy_fixture("blog_pass.md", tmp_path)
    score = analyze_blog.analyze_file(str(post))["score"]["total"]

    assert score >= quality_gate.DEFAULT_THRESHOLD
    assert quality_gate.main([str(post)]) == 0
    assert "1 post(s) checked" in capsys.readouterr().out


def test_failing_post_exits_one(tmp_path, capsys):
    post = _copy_fixture("blog_fail.md", tmp_path)

    assert quality_gate.main([str(post)]) == 1
    output = capsys.readouterr().out
    assert "Blog quality gate failed" in output
    assert "blog_fail.md" in output
    assert "[high]" in output


def test_selection_skips_non_blog_paths(tmp_path):
    skill_file = tmp_path / "skills" / "blog" / "SKILL.md"
    skill_file.parent.mkdir(parents=True)
    skill_file.write_text(
        "---\n"
        "title: Looks Like a Post\n"
        "description: This should still be skipped because it is a skill file.\n"
        "---\n\n"
        "# Looks Like a Post\n",
        encoding="utf-8",
    )

    reference_file = tmp_path / "references" / "source.md"
    reference_file.parent.mkdir(parents=True)
    reference_file.write_text(
        "---\n"
        "title: Reference Entry\n"
        "description: This should be skipped because it is reference material.\n"
        "---\n\n"
        "# Reference Entry\n",
        encoding="utf-8",
    )

    notes_file = tmp_path / "notes.md"
    notes_file.write_text(
        "---\n"
        "source: Editorial memo\n"
        "---\n\n"
        "# Notes\n",
        encoding="utf-8",
    )

    post_file = tmp_path / "posts" / "post.md"
    post_file.parent.mkdir()
    post_file.write_text(
        "---\n"
        "title: A Real Blog Post\n"
        "description: This one has the required blog post frontmatter fields.\n"
        "---\n\n"
        "# A Real Blog Post\n",
        encoding="utf-8",
    )

    assert not quality_gate.is_blog_post(skill_file, root=tmp_path)
    assert not quality_gate.is_blog_post(reference_file, root=tmp_path)
    assert not quality_gate.is_blog_post(notes_file, root=tmp_path)
    assert quality_gate.is_blog_post(post_file, root=tmp_path)


def test_json_format_shape(tmp_path, capsys):
    post = _copy_fixture("blog_fail.md", tmp_path)

    assert quality_gate.main([str(post), "--format", "json"]) == 1
    payload = json.loads(capsys.readouterr().out)

    assert payload["threshold"] == quality_gate.DEFAULT_THRESHOLD
    assert len(payload["checked"]) == 1
    assert len(payload["failures"]) == 1
    assert payload["failures"][0]["file"].endswith("blog_fail.md")
    assert payload["failures"][0]["score"] < quality_gate.DEFAULT_THRESHOLD
    assert payload["failures"][0]["issues"]
    assert payload["failures"][0]["issues"][0]["severity"] == "high"
