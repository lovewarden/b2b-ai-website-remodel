#!/usr/bin/env python3
"""Extract simple page signals from an HTML file using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.meta_description = ""
        self.headings: dict[str, list[str]] = {f"h{i}": [] for i in range(1, 7)}
        self.links: list[dict[str, str]] = []
        self.schema_blocks: list[str] = []
        self._tag_stack: list[str] = []
        self._capture_script = False
        self._script_buf: list[str] = []
        self._current_link: dict[str, str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k.lower(): v or "" for k, v in attrs}
        self._tag_stack.append(tag.lower())
        if tag.lower() == "meta" and attrs_dict.get("name", "").lower() == "description":
            self.meta_description = attrs_dict.get("content", "")
        if tag.lower() == "a":
            self._current_link = {"href": attrs_dict.get("href", ""), "text": ""}
        if tag.lower() == "script" and attrs_dict.get("type", "").lower() == "application/ld+json":
            self._capture_script = True
            self._script_buf = []

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "a" and self._current_link:
            if self._current_link["href"] or self._current_link["text"].strip():
                self._current_link["text"] = clean(self._current_link["text"])
                self.links.append(self._current_link)
            self._current_link = None
        if tag == "script" and self._capture_script:
            self.schema_blocks.append("".join(self._script_buf).strip())
            self._capture_script = False
        if self._tag_stack:
            self._tag_stack.pop()

    def handle_data(self, data: str) -> None:
        tag = self._tag_stack[-1] if self._tag_stack else ""
        if tag == "title":
            self.title += data
        if tag in self.headings:
            self.headings[tag].append(clean(data))
        if self._current_link is not None:
            self._current_link["text"] += data
        if self._capture_script:
            self._script_buf.append(data)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract(path: Path) -> dict:
    parser = PageParser()
    html = path.read_text(encoding="utf-8", errors="ignore")
    parser.feed(html)
    return {
        "file": str(path),
        "title": clean(parser.title),
        "meta_description": clean(parser.meta_description),
        "headings": {k: [h for h in v if h] for k, v in parser.headings.items()},
        "links_count": len(parser.links),
        "links_sample": parser.links[:25],
        "schema_count": len(parser.schema_blocks),
        "schema_blocks": parser.schema_blocks,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract page signals from HTML.")
    parser.add_argument("html_file")
    args = parser.parse_args()
    print(json.dumps(extract(Path(args.html_file)), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

