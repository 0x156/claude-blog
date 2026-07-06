#!/usr/bin/env python3
"""
Validate that nanobanana-mcp is properly configured for claude-blog.

Checks project .mcp.json first, then falls back to global ~/.claude/settings.json.

Checks:
1. Config file has the MCP entry
2. API key is present
3. Node.js/npx is available
4. Output directory exists or can be created

Usage:
    python3 validate_image_setup.py
"""

import json
import shutil
import sys
from pathlib import Path

MCP_NAME = "nanobanana-mcp"
OUTPUT_DIR = Path.home() / "Documents" / "nanobanana_generated"
GLOBAL_SETTINGS_PATH = Path.home() / ".claude" / "settings.json"
DEFAULT_NANOBANANA_MODEL = "gemini-3.1-flash-image"
SUPPORTED_GA_MODELS = {
    "gemini-3.1-flash-image": "Nano Banana 2 default",
    "gemini-3-pro-image": "Nano Banana Pro high quality",
    "gemini-3.1-flash-lite-image": "Nano Banana Lite low latency",
    "gemini-2.5-flash-image": "Nano Banana Original stable fallback",
}
DEPRECATED_MODEL_REPLACEMENTS = {
    "gemini-3.1-flash-image-preview": (
        "deprecated on 2026-05-28 and shut down on 2026-06-25; "
        "use gemini-3.1-flash-image"
    ),
    "gemini-3-pro-image-preview": (
        "deprecated on 2026-05-28 and shut down on 2026-06-25; "
        "use gemini-3-pro-image"
    ),
    "gemini-2.5-flash-image-preview": (
        "shut down on 2026-01-15; use gemini-2.5-flash-image"
    ),
    "gemini-2.0-flash-exp": (
        "shut down on 2026-06-01; use gemini-3.1-flash-image"
    ),
    "imagen-4.0-fast-generate-001": (
        "deprecated on 2026-06-15 and shuts down on 2026-08-17; "
        "use gemini-3.1-flash-image"
    ),
    "imagen-4.0-generate-001": (
        "deprecated on 2026-06-15 and shuts down on 2026-08-17; "
        "use gemini-3.1-flash-image"
    ),
    "imagen-4.0-ultra-generate-001": (
        "deprecated on 2026-06-15 and shuts down on 2026-08-17; "
        "use gemini-3.1-flash-image"
    ),
}


def find_project_mcp_json() -> Path:
    """Find the project-level .mcp.json by looking for .claude-plugin/plugin.json."""
    current = Path(__file__).resolve().parent
    for _ in range(10):
        candidate = current / ".claude-plugin" / "plugin.json"
        if candidate.exists():
            return current / ".mcp.json"
        parent = current.parent
        if parent == current:
            break
        current = parent
    current = Path.cwd()
    for _ in range(10):
        candidate = current / ".claude-plugin" / "plugin.json"
        if candidate.exists():
            return current / ".mcp.json"
        parent = current.parent
        if parent == current:
            break
        current = parent
    return None


def check(label: str, passed: bool, detail: str = "") -> bool:
    status = "PASS" if passed else "FAIL"
    msg = f"  [{status}] {label}"
    if detail:
        msg += f" - {detail}"
    print(msg)
    return passed


def _supported_model_list() -> str:
    return ", ".join(sorted(SUPPORTED_GA_MODELS))


def validate_nanobanana_model(model: str) -> tuple:
    """Validate the configured image model against supported GA model IDs."""
    model = (model or "").strip()
    if not model:
        return True, f"(not set - package will use default {DEFAULT_NANOBANANA_MODEL})"
    if model in SUPPORTED_GA_MODELS:
        return True, f"{model} ({SUPPORTED_GA_MODELS[model]})"
    if model in DEPRECATED_MODEL_REPLACEMENTS:
        return False, f"{model} (WARNING: {DEPRECATED_MODEL_REPLACEMENTS[model]})"
    if "-preview" in model:
        return False, (
            f"{model} (WARNING: preview image models are deprecated or shut down; "
            f"use one of: {_supported_model_list()})"
        )
    return False, f"{model} (unsupported; use one of: {_supported_model_list()})"


def find_mcp_config() -> tuple:
    """Find MCP config in project or global settings. Returns (config_dict, path_label)."""
    # Try project .mcp.json first
    project_path = find_project_mcp_json()
    if project_path and project_path.exists():
        try:
            with open(project_path) as f:
                config = json.load(f)
            if MCP_NAME in config.get("mcpServers", {}):
                return config, f"project .mcp.json ({project_path})"
        except (json.JSONDecodeError, OSError):
            pass

    # Fallback to global settings
    if GLOBAL_SETTINGS_PATH.exists():
        try:
            with open(GLOBAL_SETTINGS_PATH) as f:
                config = json.load(f)
            if MCP_NAME in config.get("mcpServers", {}):
                return config, f"global settings ({GLOBAL_SETTINGS_PATH})"
        except (json.JSONDecodeError, OSError):
            pass

    return None, None


def main() -> int:
    print("claude-blog - Image Generation Setup Validation")
    print("=" * 48)
    results = []

    # 1-2. Find and load config
    config, config_label = find_mcp_config()

    if config is None:
        results.append(check(
            "MCP config found",
            False,
            "Not found in project .mcp.json or global settings.json",
        ))
        print(f"\nRun: python3 scripts/setup_image_mcp.py --key YOUR_KEY")
        return 1

    results.append(check("MCP config found", True, config_label))

    # 3. MCP entry exists
    servers = config.get("mcpServers", {})
    has_mcp = MCP_NAME in servers
    results.append(check(f"MCP server '{MCP_NAME}' configured", has_mcp))

    if has_mcp:
        mcp = servers[MCP_NAME]

        # 4. Command is npx
        results.append(check(
            "Command is 'npx'",
            mcp.get("command") == "npx",
            mcp.get("command", "(missing)"),
        ))

        # 5. Package is correct (accepts pinned versions like @ycse/nanobanana-mcp@1.1.1)
        args = mcp.get("args", [])
        has_pkg = any(
            isinstance(a, str) and a.startswith("@ycse/nanobanana-mcp")
            for a in args
        )
        is_pinned = any(
            isinstance(a, str) and a.startswith("@ycse/nanobanana-mcp@")
            for a in args
        )
        pkg_detail = str(args)
        if has_pkg and not is_pinned:
            pkg_detail += " (WARNING: not version-pinned - supply chain risk)"
        results.append(check(
            "Package is @ycse/nanobanana-mcp",
            has_pkg,
            pkg_detail,
        ))

        # 6. API key present
        env = mcp.get("env", {})
        key = env.get("GOOGLE_AI_API_KEY", "")
        # Accept env var placeholders as configured, but warn about ${} syntax
        key_set = bool(key) and key != ""
        is_placeholder = key.startswith("${") and key.endswith("}")
        if is_placeholder:
            results.append(check(
                "GOOGLE_AI_API_KEY is set",
                True,
                f"{key} (env var placeholder - ensure this variable is exported in your shell)",
            ))
        else:
            # Closes audit VULN-032: length-only display, no prefix/suffix leak.
            display = f"<{len(key)} chars, set>" if key_set else "(empty)"
            results.append(check(
                "GOOGLE_AI_API_KEY is set",
                key_set,
                display,
            ))

        # 7. Model configured (optional - package has a supported GA default)
        model = env.get("NANOBANANA_MODEL", "")
        model_ok, model_detail = validate_nanobanana_model(model)
        results.append(check(
            "NANOBANANA_MODEL is supported",
            model_ok,
            model_detail,
        ))

    # 8. Node.js/npx available
    has_npx = shutil.which("npx") is not None
    results.append(check(
        "npx is available in PATH",
        has_npx,
        shutil.which("npx") or "not found - install Node.js 18+",
    ))

    # 9. Output directory
    if OUTPUT_DIR.exists():
        results.append(check("Output directory exists", True, str(OUTPUT_DIR)))
    else:
        try:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            results.append(check("Output directory created", True, str(OUTPUT_DIR)))
        except OSError as e:
            results.append(check("Output directory writable", False, str(e)))

    # Summary
    passed = sum(1 for r in results if r)
    total = len(results)
    print(f"\n{'=' * 48}")
    print(f"Results: {passed}/{total} checks passed")

    if passed == total:
        print("Status: Ready to generate blog images!")
        return 0
    else:
        print("Status: Some checks failed. Fix the issues above.")
        print("Setup: python3 scripts/setup_image_mcp.py --key YOUR_KEY")
        return 1


if __name__ == "__main__":
    sys.exit(main())
