"""Auto-generate the nav from docs/blog/ on every build.

Adding or removing a post file updates the nav automatically:
- new post  -> appears under its year, in date-descending position
- deleted post -> its entry disappears (no more 'None' in the nav)

Run by mkdocs via the `hooks` setting; works for `mkdocs build` and
`mkdocs serve` alike. The hook runs at on_config, before the i18n
plugin resolves per-language navs.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
BLOG = DOCS / "blog"


def _title(path: Path) -> str:
    """First '# ' heading of the file, falling back to its slug."""
    try:
        for line in path.read_text(encoding="utf-8").splitlines()[:10]:
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return path.stem


def on_config(config, **kwargs):
    posts = []
    if BLOG.is_dir():
        for p in BLOG.glob("2*.md"):
            m = re.match(r"^(\d{4}-\d{2}-\d{2})-", p.stem)
            if m:
                posts.append((m.group(1), p.stem, _title(p)))

    # date prefix sorts chronologically; reverse = newest first
    posts.sort(key=lambda t: (t[0], t[1]), reverse=True)

    years = {}
    for date, slug, title in posts:
        years.setdefault(date[:4], []).append({title: f"blog/{slug}.md"})

    blog = ["blog/index.md"]  # section index (navigation.indexes)
    for y in sorted(years, reverse=True):
        blog.append({y: years[y]})

    config.nav = [
        {"首页": "index.md"},
        {"博客": blog},
        {"项目": "projects/index.md"},
        {"玩具": "gadgets/index.md"},
    ]
    return config


def _index_markdown(zh: bool) -> str:
    """Full content of the blog listing page, generated from docs/blog/."""
    posts = []
    if BLOG.is_dir():
        for p in BLOG.glob("2*.md"):
            m = re.match(r"^(\d{4}-\d{2}-\d{2})-", p.stem)
            if m:
                posts.append((m.group(1), p.stem, _title(p)))
    posts.sort(key=lambda t: (t[0], t[1]), reverse=True)

    lines = ["# 博客", "", "学习笔记与技术文章，按时间倒序。"] if zh else \
            ["# Blog", "", "Study notes and technical posts, newest first."]
    years = {}
    for date, slug, title in posts:
        years.setdefault(date[:4], []).append(f"- [{title}]({slug}.md)")
    for y in sorted(years, reverse=True):
        lines += ["", f"## {y}"] + years[y]
    return "\n".join(lines) + "\n"


def on_page_markdown(markdown, page, config, files):
    """Auto-generate the blog listing pages (zh + en) at build time."""
    src = page.file.src_path.replace("\\", "/")
    if src == "blog/index.md":
        return _index_markdown(zh=True)
    if src == "blog/index.en.md":
        return _index_markdown(zh=False)
    return markdown
