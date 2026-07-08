#!/usr/bin/env python3
"""
Setup script for nanobanana-mcp in claude-blog.

Configures @ycse/nanobanana-mcp in Claude Code's global settings.json
(default) or the project's .mcp.json (with --project flag).

Usage:
    python3 setup_image_mcp.py                    # Interactive (writes global)
    python3 setup_image_mcp.py --key-file key.txt # Non-interactive
    python3 setup_image_mcp.py --check            # Verify existing setup
    python3 setup_image_mcp.py --remove           # Remove MCP config
    python3 setup_image_mcp.py --project          # Write to project .mcp.json (env-expansion only)
    python3 setup_image_mcp.py --json             # Output structured JSON
    python3 setup_image_mcp.py --help             # Show usage
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

MCP_NAME = "nanobanana-mcp"
MCP_PACKAGE = "@ycse/nanobanana-mcp"
DEFAULT_MODEL = "flash"
PINNED_PACKAGE = "@ycse/nanobanana-mcp@1.1.1"
ENV_PLACEHOLDER = "${GOOGLE_AI_API_KEY}"
PLUGIN_NAME = "claude-blog"
GLOBAL_SETTINGS_PATH = Path.home() / ".claude" / "settings.json"
PLACEHOLDER_RE = re.compile(r"^\$\{([A-Za-z_][A-Za-z0-9_]*)\}$")


def find_project_mcp_json() -> Path:
    """Find the project-level .mcp.json by locating .claude-plugin/plugin.json with name=='claude-blog'."""
    def matches(plugin_path: Path) -> bool:
        try:
            import json as _json
            with open(plugin_path) as f:
                return _json.load(f).get("name") == PLUGIN_NAME
        except (OSError, _json.JSONDecodeError):
            return False
    for start in (Path(__file__).resolve().parent, Path.cwd()):
        current = start
        for _ in range(5):
            candidate = current / ".claude-plugin" / "plugin.json"
            if candidate.exists() and matches(candidate):
                return current / ".mcp.json"
            parent = current.parent
            if parent == current:
                break
            current = parent
    return None


def get_config_path(use_global: bool) -> Path:
    """Get the appropriate config file path."""
    if use_global:
        return GLOBAL_SETTINGS_PATH
    project_path = find_project_mcp_json()
    if project_path:
        return project_path
    print("Warning: Could not find project root (.claude-plugin/plugin.json).")
    print("Falling back to global settings.")
    return GLOBAL_SETTINGS_PATH


def load_config(path: Path) -> dict:
    """Load config file."""
    if not path.exists():
        return {}
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in {path}: line {exc.lineno}, column {exc.colno}. "
            "Repair the file or move it aside before rerunning setup."
        ) from exc


def save_config(path: Path, config: dict, quiet: bool = False) -> None:
    """Save config file. Sets restrictive permissions if the file may contain secrets."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(config, f, indent=2)
        f.write("\n")
    os.chmod(path, 0o600)  # belt-and-braces if file pre-existed
    if not quiet:
        print(f"Config saved to {path}")


def _mask_api_key(key: str) -> str:
    """Mask an API key for safe display (VULN-S01).

    Shows the first 4 and last 4 chars with stars between. For short keys
    (<10 chars), returns a length-only placeholder so we never reveal more
    than half the key. Terminal scrollback, tmux logs, and screen recordings
    all preserve stdout; this helper keeps the literal key out of the echo.
    """
    if not key:
        return "(not set)"
    if len(key) < 10:
        return f"<{len(key)} chars>"
    return f"{key[:4]}****{key[-4:]}"


def _is_git_tracked(path: Path) -> bool:
    """Return True if path is tracked by git in its containing repo."""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "ls-files", "--error-unmatch", path.name],
            cwd=path.parent,
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except (OSError, FileNotFoundError):
        return False


def _placeholder_env_var(value: str) -> str:
    """Return placeholder env var name, or an empty string."""
    match = PLACEHOLDER_RE.match(value or "")
    return match.group(1) if match else ""


def check_setup(use_global: bool, as_json: bool = False) -> bool:
    """Check if MCP is already configured."""
    # Check project-level first, then global
    paths_to_check = []
    if not use_global:
        project_path = find_project_mcp_json()
        if project_path:
            paths_to_check.append(("Project .mcp.json", project_path))
    paths_to_check.append(("Global settings.json", GLOBAL_SETTINGS_PATH))

    for label, path in paths_to_check:
        config = load_config(path)
        servers = config.get("mcpServers", {})
        if MCP_NAME in servers:
            env = servers[MCP_NAME].get("env", {})
            key = env.get("GOOGLE_AI_API_KEY", "")
            placeholder_var = _placeholder_env_var(key)
            key_ok = bool(key)
            key_detail = f"<{len(key)} chars, set>" if key else "(not set)"
            if placeholder_var:
                key_ok = bool(os.environ.get(placeholder_var))
                key_detail = (
                    f"{key} resolves from environment"
                    if key_ok
                    else f"{key} is configured but {placeholder_var} is not exported"
                )
            result = {
                "status": "success" if key_ok else "error",
                "configured": True,
                "path": str(path),
                "scope": label,
                "package": PINNED_PACKAGE,
                "api_key_ok": key_ok,
                "api_key": key_detail,
                "model": env.get("NANOBANANA_MODEL", DEFAULT_MODEL),
            }
            if as_json:
                print(json.dumps(result, indent=2))
            else:
                print(f"MCP server '{MCP_NAME}' found in {label}.")
                print(f"  Path:    {path}")
                print(f"  Package: {MCP_PACKAGE}")
                print(f"  API Key: {key_detail}")
                print(f"  Model:   {result['model']}")
            return key_ok

    if as_json:
        print(json.dumps({"status": "missing", "configured": False}, indent=2))
    else:
        print(f"MCP server '{MCP_NAME}' is NOT configured.")
    return False


def remove_mcp(use_global: bool, as_json: bool = False) -> None:
    """Remove MCP configuration."""
    path = get_config_path(use_global)
    config = load_config(path)
    servers = config.get("mcpServers", {})
    if MCP_NAME in servers:
        del servers[MCP_NAME]
        config["mcpServers"] = servers
        save_config(path, config, quiet=as_json)
        if as_json:
            print(json.dumps({"status": "success", "removed": True, "path": str(path)}, indent=2))
        else:
            print(f"Removed '{MCP_NAME}' from {path}.")
    else:
        if as_json:
            print(json.dumps({"status": "missing", "removed": False, "path": str(path)}, indent=2))
        else:
            print(f"'{MCP_NAME}' not found in {path}.")


def setup_mcp(api_key: str, use_global: bool, as_json: bool = False) -> None:
    """Configure MCP server. Project mode uses env-expansion only (never literal key)."""
    if not api_key or not api_key.strip():
        print("Error: API key cannot be empty.")
        sys.exit(1)
    api_key = api_key.strip()
    path = get_config_path(use_global)

    # Safety: project mode must never write a literal key into a tracked file.
    if not use_global and _is_git_tracked(path):
        gitignore = path.parent / ".gitignore"
        ignored = ".mcp.json" in gitignore.read_text() if gitignore.exists() else False
        if not ignored:
            print(f"REFUSING: {path} is tracked by git and .gitignore does not exclude .mcp.json.")
            print("Either:")
            print(f"  1. Add '.mcp.json' to {gitignore} and run: git rm --cached .mcp.json")
            print(f"  2. Use --global to write to ~/.claude/settings.json instead (recommended).")
            sys.exit(2)

    config = load_config(path)
    config.setdefault("mcpServers", {})

    # Project mode: env-expansion only. Global mode: literal value (file is user-private + chmod 600).
    key_value = ENV_PLACEHOLDER if not use_global else api_key

    config["mcpServers"][MCP_NAME] = {
        "command": "npx",
        "args": ["-y", PINNED_PACKAGE],
        "env": {
            "GOOGLE_AI_API_KEY": key_value,
            "NANOBANANA_MODEL": DEFAULT_MODEL,
        },
    }
    save_config(path, config, quiet=as_json)

    result = {
        "status": "success",
        "server": MCP_NAME,
        "package": PINNED_PACKAGE,
        "model": DEFAULT_MODEL,
        "config": str(path),
        "uses_env_placeholder": not use_global,
    }
    if as_json:
        print(json.dumps(result, indent=2))
        return

    print(f"\nMCP server '{MCP_NAME}' configured successfully!")
    print(f"  Package: {PINNED_PACKAGE}")
    print(f"  Model:   {DEFAULT_MODEL}")
    print(f"  Config:  {path}")
    if not use_global:
        print()
        print("Project mode uses env-expansion (never writes literal key).")
        print("Add this line to your shell rc (~/.bashrc or ~/.zshrc),")
        print("substituting the API key you just entered for <YOUR_KEY>:")
        # VULN-S01 (v1.9.1): do NOT echo the literal key. Terminal scrollback,
        # tmux logs, and recording sessions all preserve stdout. Mask the
        # value; the user already entered it, so a placeholder + first/last
        # 4-char hint is enough to confirm the intended export.
        masked = _mask_api_key(api_key)
        print(f"  export GOOGLE_AI_API_KEY=<YOUR_KEY>   # hint: {masked}")
        print("Then restart your shell + Claude Code.")
    else:
        print()
        print(f"File mode set to 0600 (user-private).")
        print("Restart Claude Code for changes to take effect.")
    print(f"Generated images saved to: ~/Documents/nanobanana_generated/")


def build_parser() -> argparse.ArgumentParser:
    """Build the command line parser."""
    parser = argparse.ArgumentParser(description="Configure nanobanana-mcp for claude-blog")
    parser.add_argument("--key", help="API key. Prefer --key-file, env var, or interactive prompt.")
    parser.add_argument("--key-file", help="Read API key from a local file")
    parser.add_argument("--check", action="store_true", help="Verify existing setup")
    parser.add_argument("--remove", action="store_true", help="Remove MCP configuration")
    parser.add_argument("--project", action="store_true", help="Write project .mcp.json")
    parser.add_argument("--global", dest="global_scope", action="store_true", help="Write global settings")
    parser.add_argument("--json", action="store_true", help="Output structured JSON")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    # Safer default: --global (writes user-private ~/.claude/settings.json).
    # --project opts in to project-local config (with safety guards).
    if args.project and args.global_scope:
        parser.error("Use either --project or --global, not both")
    use_global = not args.project

    try:
        if args.check:
            ok = check_setup(use_global, args.json)
            sys.exit(0 if ok else 1)
            return

        if args.remove:
            remove_mcp(use_global, args.json)
            return

        api_key = None
        if args.key_file:
            api_key = Path(args.key_file).read_text(encoding="utf-8").strip()
        elif args.key:
            api_key = args.key
            if not args.json:
                print("Warning: --key can expose secrets in shell history. Prefer --key-file or GOOGLE_AI_API_KEY.")
        else:
            api_key = os.environ.get("GOOGLE_AI_API_KEY")

        if not api_key:
            if args.json:
                print(json.dumps({
                    "status": "error",
                    "error": "GOOGLE_AI_API_KEY is not set and no key was provided",
                }, indent=2))
                sys.exit(1)
            print("claude-blog - Image Generation MCP Setup")
            print("=" * 45)
            print("\nCreate an API key at: https://aistudio.google.com/apikey")
            print("Image models may require a paid tier or billing-enabled project.")
            print()
            try:
                api_key = input("Enter your Google AI API key: ")
            except (EOFError, KeyboardInterrupt):
                print("\nError: No input received. Provide --key-file or set GOOGLE_AI_API_KEY.")
                sys.exit(1)

        setup_mcp(api_key, use_global, args.json)
    except (OSError, ValueError) as exc:
        if args.json:
            print(json.dumps({"status": "error", "error": str(exc)}, indent=2))
        else:
            print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
