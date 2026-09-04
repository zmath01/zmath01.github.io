#!/usr/bin/env python3
"""Normalize Etherpad-style markdown so Python-Markdown renders it correctly.

Fixes applied (idempotent, content-preserving):
1. Blank line before a list block that directly follows a paragraph line.
2. Blank line after a list block when a col-0 paragraph follows (prevents
   lazy continuation into the last list item).
3. Display-math $$...$$ blocks de-indented out of list items and wrapped
   with blank lines, so arithmatex protects them (keeps \\ intact).
"""
import re
import sys
from pathlib import Path

LIST_RE = re.compile(r"^\s*(?:[*+-]|\d+\.)\s")


def is_list(line: str) -> bool:
    return bool(LIST_RE.match(line))


def normalize(text: str) -> str:
    lines = text.split("\n")
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        stripped = line.lstrip()

        # -- display math block: dedent + blank-line wrap ----------------
        if stripped.startswith("$$"):
            if out and out[-1].strip():
                out.append("")
            out.append(stripped)
            if stripped.count("$$") < 2:  # multi-line block
                i += 1
                while i < n:
                    cont = lines[i].lstrip()
                    out.append(cont)
                    if "$$" in cont:
                        break
                    i += 1
            if i + 1 < n and lines[i + 1].strip():
                out.append("")
            i += 1
            continue

        # -- blank line before list following a paragraph ----------------
        if is_list(line) and out and out[-1].strip() and not is_list(out[-1]):
            out.append("")

        out.append(line)

        # -- blank line after list when a col-0 paragraph follows --------
        if is_list(line):
            nxt = lines[i + 1] if i + 1 < n else ""
            if nxt.strip() and not is_list(nxt) and not nxt.startswith((" ", "\t")):
                out.append("")
        i += 1
    return "\n".join(out)


def main() -> None:
    root = Path(sys.argv[1])
    changed = 0
    for p in sorted(root.glob("*.md")):
        orig = p.read_text(encoding="utf-8")
        fixed = normalize(orig)
        if fixed != orig:
            p.write_text(fixed, encoding="utf-8")
            changed += 1
            print(f"  fixed: {p.name}")
    print(f"total changed: {changed}")


if __name__ == "__main__":
    main()
