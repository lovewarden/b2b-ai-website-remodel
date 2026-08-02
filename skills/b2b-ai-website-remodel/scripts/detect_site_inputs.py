#!/usr/bin/env python3
"""Detect basic website project signals using only the Python standard library."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SIGNALS = {
    "nextjs": ["next.config.js", "next.config.mjs", "app", "pages"],
    "astro": ["astro.config.mjs", "astro.config.ts"],
    "vite": ["vite.config.js", "vite.config.ts", "vite.config.mjs"],
    "vue": ["vue.config.js", "nuxt.config.js", "nuxt.config.ts"],
    "wordpress": ["wp-content", "functions.php", "style.css"],
    "static_html": ["index.html"],
}


def exists(root: Path, name: str) -> bool:
    return (root / name).exists() or any(root.glob(f"**/{name}"))


def detect(root: Path) -> dict:
    root = root.resolve()
    matches: dict[str, list[str]] = {}
    for kind, names in SIGNALS.items():
        found = [name for name in names if exists(root, name)]
        if found:
            matches[kind] = found
    package_json = root / "package.json"
    pyproject = root / "pyproject.toml"
    return {
        "root": str(root),
        "exists": root.exists(),
        "signals": matches,
        "has_package_json": package_json.exists(),
        "has_pyproject": pyproject.exists(),
        "suggested_site_type": next(iter(matches), "unknown") if matches else "unknown",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect website project signals.")
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()
    print(json.dumps(detect(Path(args.path)), indent=2))


if __name__ == "__main__":
    main()

