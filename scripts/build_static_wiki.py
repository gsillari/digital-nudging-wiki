from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
DEFAULT_OUT = ROOT / "site"


@dataclass
class Page:
    source: Path
    rel_source: Path
    title: str
    page_type: str
    tags: list[str]
    body: str
    excerpt: str
    out_rel: Path
    url: str
    links: set[str]


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "page"


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[text.find("\n", end + 1) + 1 :]
    try:
        data = yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        data = {}
        current_list: str | None = None
        for line in raw.splitlines():
            if not line.strip():
                continue
            key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
            if key_match:
                key, value = key_match.groups()
                current_list = key if value == "" else None
                if value == "":
                    data[key] = []
                else:
                    data[key] = value.strip().strip('"')
                continue
            item_match = re.match(r"^\s*-\s+(.*)$", line)
            if item_match and current_list:
                data.setdefault(current_list, []).append(item_match.group(1).strip().strip('"'))
    return data, body


def page_title(meta: dict, body: str, fallback: str) -> str:
    if meta.get("title"):
        return str(meta["title"])
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def output_path(rel: Path) -> Path:
    if rel.name == "index.md":
        return Path("index.html")
    parts = [slugify(part) for part in rel.with_suffix("").parts]
    return Path(*parts) / "index.html"


def url_for(out_rel: Path) -> str:
    if out_rel.name == "index.html" and len(out_rel.parts) == 1:
        return "index.html"
    if out_rel.name == "index.html":
        return "/".join(out_rel.parts[:-1]) + "/"
    return "/".join(out_rel.parts)


def collect_wikilinks(text: str) -> set[str]:
    links: set[str] = set()
    for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.add(target)
    return links


def strip_wikilink_alias(value: str) -> str:
    return value.split("|", 1)[-1].split("#", 1)[0].strip()


def read_pages() -> list[Page]:
    pages: list[Page] = []
    for source in sorted(WIKI.rglob("*.md")):
        rel = source.relative_to(WIKI)
        text = source.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        title = page_title(meta, body, source.stem)
        tags = meta.get("tags") or []
        if not isinstance(tags, list):
            tags = [str(tags)]
        excerpt = " ".join(
            line.strip()
            for line in body.splitlines()
            if line.strip() and not line.startswith("#") and not line.startswith("|")
        )[:260]
        out_rel = output_path(rel)
        pages.append(
            Page(
                source=source,
                rel_source=rel,
                title=title,
                page_type=str(meta.get("page_type") or rel.parts[0] if len(rel.parts) > 1 else "page"),
                tags=[str(tag) for tag in tags],
                body=body,
                excerpt=excerpt,
                out_rel=out_rel,
                url=url_for(out_rel),
                links=collect_wikilinks(body),
            )
        )
    return pages


def build_lookup(pages: Iterable[Page]) -> dict[str, Page]:
    lookup: dict[str, Page] = {}
    for page in pages:
        names = {
            page.title,
            page.source.stem,
            page.rel_source.with_suffix("").as_posix(),
            page.rel_source.stem,
        }
        for name in names:
            lookup.setdefault(name, page)
    return lookup


def relative_href(from_page: Page, to_url: str) -> str:
    from_dir = from_page.out_rel.parent
    target = Path(to_url)
    if to_url.endswith("/"):
        target = Path(to_url) / "index.html"
    rel = Path("../" * len(from_dir.parts)) / target
    return rel.as_posix()


def inline_markup(text: str, page: Page, lookup: dict[str, Page]) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"\u0000{len(placeholders) - 1}\u0000"

    def code_repl(match: re.Match[str]) -> str:
        return stash(f"<code>{html.escape(match.group(1))}</code>")

    text = re.sub(r"`([^`]+)`", code_repl, text)
    text = html.escape(text)

    def wiki_repl(match: re.Match[str]) -> str:
        raw = html.unescape(match.group(1))
        target = raw.split("|", 1)[0].split("#", 1)[0].strip()
        label = strip_wikilink_alias(raw)
        target_page = lookup.get(target)
        if not target_page:
            return html.escape(label)
        href = relative_href(page, target_page.url)
        return f'<a href="{href}">{html.escape(label)}</a>'

    text = re.sub(r"\[\[([^\]]+)\]\]", wiki_repl, text)

    def md_link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        href = match.group(2)
        if href.startswith("/Users/"):
            return html.escape(label)
        return f'<a href="{html.escape(href, quote=True)}">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", md_link_repl, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = text.replace(" -- ", " &mdash; ")

    for idx, value in enumerate(placeholders):
        text = text.replace(f"\u0000{idx}\u0000", value)
    return text


def heading_id(text: str, used: set[str]) -> str:
    base = slugify(re.sub(r"<[^>]+>", "", text))
    candidate = base
    counter = 2
    while candidate in used:
        candidate = f"{base}-{counter}"
        counter += 1
    used.add(candidate)
    return candidate


def render_table(lines: list[str], page: Page, lookup: dict[str, Page]) -> str:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) < 2:
        return ""
    headers = rows[0]
    body_rows = rows[2:] if re.match(r"^\s*\|?\s*:?-{3,}", lines[1]) else rows[1:]
    out = ["<table>", "<thead><tr>"]
    out.extend(f"<th>{inline_markup(cell, page, lookup)}</th>" for cell in headers)
    out.append("</tr></thead>")
    out.append("<tbody>")
    for row in body_rows:
        out.append("<tr>")
        out.extend(f"<td>{inline_markup(cell, page, lookup)}</td>" for cell in row)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def render_markdown(body: str, page: Page, lookup: dict[str, Page]) -> tuple[str, list[tuple[int, str, str]]]:
    lines = body.splitlines()
    out: list[str] = []
    toc: list[tuple[int, str, str]] = []
    used_ids: set[str] = set()
    i = 0
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(line.strip() for line in paragraph)
            out.append(f"<p>{inline_markup(text, page, lookup)}</p>")
            paragraph.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            language = stripped[3:].strip()
            code: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            klass = f' class="language-{html.escape(language)}"' if language else ""
            out.append(f"<pre><code{klass}>{html.escape(chr(10).join(code))}</code></pre>")
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            flush_paragraph()
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            out.append(render_table(table_lines, page, lookup))
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            content = inline_markup(heading.group(2), page, lookup)
            hid = heading_id(content, used_ids)
            if level <= 3:
                toc.append((level, re.sub(r"<[^>]+>", "", content), hid))
            out.append(f'<h{level} id="{hid}">{content}</h{level}>')
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            flush_paragraph()
            out.append("<ul>")
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                item = re.sub(r"^[-*]\s+", "", lines[i].strip())
                out.append(f"<li>{inline_markup(item, page, lookup)}</li>")
                i += 1
            out.append("</ul>")
            continue

        if re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                out.append(f"<li>{inline_markup(item, page, lookup)}</li>")
                i += 1
            out.append("</ol>")
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            quote = stripped.lstrip("> ")
            out.append(f"<blockquote>{inline_markup(quote, page, lookup)}</blockquote>")
            i += 1
            continue

        paragraph.append(line)
        i += 1

    flush_paragraph()
    return "\n".join(out), toc


def group_pages(pages: list[Page]) -> dict[str, list[Page]]:
    groups: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        group = page.rel_source.parts[0] if len(page.rel_source.parts) > 1 else "home"
        groups[group].append(page)
    return dict(sorted(groups.items()))


def nav_html(pages: list[Page], current: Page) -> str:
    groups = group_pages(pages)
    parts = ['<nav class="sidebar">', '<a class="brand" href="/digital-nudging-wiki/">Digital Nudging Wiki</a>']
    parts.append('<form class="search-form" role="search"><input id="search" type="search" placeholder="Search the wiki" autocomplete="off"><div id="search-results"></div></form>')
    for group, items in groups.items():
        label = "Home" if group == "home" else group.replace("-", " ").title()
        parts.append(f"<details open><summary>{html.escape(label)}</summary>")
        for item in sorted(items, key=lambda p: p.title.lower()):
            active = " active" if item.source == current.source else ""
            href = relative_href(current, item.url)
            parts.append(f'<a class="nav-link{active}" href="{href}">{html.escape(item.title)}</a>')
        parts.append("</details>")
    parts.append("</nav>")
    return "\n".join(parts)


def render_backlinks(page: Page, backlinks: dict[str, list[Page]]) -> str:
    incoming = backlinks.get(page.title, []) + backlinks.get(page.source.stem, [])
    dedup: dict[Path, Page] = {p.source: p for p in incoming if p.source != page.source}
    if not dedup:
        return ""
    links = []
    for other in sorted(dedup.values(), key=lambda p: p.title.lower()):
        href = relative_href(page, other.url)
        links.append(f'<li><a href="{href}">{html.escape(other.title)}</a></li>')
    return '<section class="backlinks"><h2>Backlinks</h2><ul>' + "".join(links) + "</ul></section>"


def page_html(page: Page, pages: list[Page], lookup: dict[str, Page], backlinks: dict[str, list[Page]]) -> str:
    body_html, toc = render_markdown(page.body, page, lookup)
    toc_html = ""
    if toc:
        toc_items = []
        for level, label, hid in toc:
            toc_items.append(f'<a class="toc-level-{level}" href="#{hid}">{html.escape(label)}</a>')
        toc_html = '<aside class="toc"><div class="toc-title">On This Page</div>' + "".join(toc_items) + "</aside>"
    tags = "".join(f"<span>{html.escape(tag)}</span>" for tag in page.tags)
    backlinks_html = render_backlinks(page, backlinks)
    nav = nav_html(pages, page)
    rel_root = "../" * len(page.out_rel.parent.parts)
    css = f"{rel_root}assets/site.css"
    js = f"{rel_root}assets/site.js"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page.title)} · Digital Nudging Wiki</title>
  <link rel="stylesheet" href="{css}">
</head>
<body>
  {nav}
  <main class="page">
    <header class="page-header">
      <div class="eyebrow">{html.escape(page.page_type)}</div>
      <h1>{html.escape(page.title)}</h1>
      <div class="tags">{tags}</div>
    </header>
    <div class="content-grid">
      <article class="content">
        {body_html}
        {backlinks_html}
      </article>
      {toc_html}
    </div>
  </main>
  <script src="{js}"></script>
</body>
</html>
"""


CSS = """
:root {
  color-scheme: light;
  --bg: #f7f5ef;
  --panel: #ffffff;
  --ink: #232323;
  --muted: #6f6a60;
  --line: #dfd8cb;
  --accent: #0f766e;
  --accent-soft: #d8eee9;
  --link: #1261a6;
  --code-bg: #f0ede5;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
}
a { color: var(--link); text-decoration-thickness: 0.08em; text-underline-offset: 0.16em; }
.sidebar {
  position: fixed;
  inset: 0 auto 0 0;
  width: 292px;
  overflow: auto;
  padding: 20px 16px 28px;
  border-right: 1px solid var(--line);
  background: #fbfaf6;
}
.brand {
  display: block;
  color: var(--ink);
  font-size: 20px;
  font-weight: 750;
  line-height: 1.15;
  text-decoration: none;
  margin-bottom: 18px;
}
.search-form { position: relative; margin-bottom: 16px; }
#search {
  width: 100%;
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 10px 11px;
  background: white;
  color: var(--ink);
  font: inherit;
}
#search-results {
  display: none;
  position: absolute;
  z-index: 5;
  inset: calc(100% + 6px) 0 auto 0;
  max-height: 420px;
  overflow: auto;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: white;
  box-shadow: 0 14px 28px rgba(0,0,0,0.12);
}
#search-results a {
  display: block;
  padding: 10px 12px;
  color: var(--ink);
  text-decoration: none;
  border-bottom: 1px solid var(--line);
}
#search-results a:last-child { border-bottom: 0; }
#search-results small { display: block; color: var(--muted); margin-top: 3px; }
details { margin: 12px 0; }
summary {
  color: var(--muted);
  cursor: pointer;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 7px;
}
.nav-link {
  display: block;
  padding: 6px 8px;
  border-radius: 5px;
  color: var(--ink);
  font-size: 14px;
  line-height: 1.25;
  text-decoration: none;
}
.nav-link:hover, .nav-link.active { background: var(--accent-soft); color: #063f3a; }
.page {
  margin-left: 292px;
  min-height: 100vh;
}
.page-header {
  padding: 44px clamp(24px, 5vw, 72px) 20px;
  border-bottom: 1px solid var(--line);
  background: rgba(255,255,255,0.44);
}
.eyebrow {
  color: var(--accent);
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}
h1 {
  margin: 8px 0 12px;
  font-size: clamp(32px, 4.4vw, 56px);
  line-height: 1.02;
}
.tags { display: flex; flex-wrap: wrap; gap: 7px; }
.tags span {
  padding: 4px 8px;
  border: 1px solid var(--line);
  border-radius: 999px;
  color: var(--muted);
  background: white;
  font-size: 12px;
}
.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 780px) minmax(180px, 260px);
  gap: 44px;
  padding: 28px clamp(24px, 5vw, 72px) 72px;
}
.content {
  font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  font-size: 18px;
  line-height: 1.68;
}
.content h1 { display: none; }
.content h2, .content h3, .content h4 {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.18;
}
.content h2 { margin-top: 2.1em; font-size: 30px; }
.content h3 { margin-top: 1.8em; font-size: 23px; }
.content p, .content ul, .content ol { margin: 1em 0; }
.content li { margin: 0.32em 0; }
.content code {
  background: var(--code-bg);
  padding: 0.13em 0.28em;
  border-radius: 4px;
  font-size: 0.9em;
}
pre {
  overflow: auto;
  padding: 16px;
  background: #242321;
  color: #fff8ea;
  border-radius: 6px;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.2em 0;
  font-size: 15px;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
th, td { border: 1px solid var(--line); padding: 9px 10px; text-align: left; vertical-align: top; }
th { background: #ece7dc; }
blockquote {
  margin: 1.2em 0;
  padding-left: 18px;
  border-left: 4px solid var(--accent);
  color: #3d3932;
}
.toc {
  position: sticky;
  top: 24px;
  align-self: start;
  padding: 16px;
  border-left: 1px solid var(--line);
  color: var(--muted);
  font-size: 14px;
}
.toc-title {
  margin-bottom: 8px;
  color: var(--ink);
  font-weight: 750;
}
.toc a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  margin: 8px 0;
}
.toc-level-3 { padding-left: 14px; }
.backlinks {
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--line);
}
@media (max-width: 920px) {
  .sidebar {
    position: static;
    width: auto;
    max-height: 45vh;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }
  .page { margin-left: 0; }
  .content-grid { grid-template-columns: 1fr; }
  .toc { display: none; }
}
"""


JS = """
(() => {
  const input = document.getElementById("search");
  const results = document.getElementById("search-results");
  if (!input || !results) return;
  const root = document.querySelector("script[src$='site.js']").getAttribute("src").replace(/assets\\/site\\.js$/, "");
  let index = [];
  fetch(root + "assets/search.json").then(r => r.json()).then(data => { index = data; });
  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    if (!q) {
      results.style.display = "none";
      results.innerHTML = "";
      return;
    }
    const hits = index
      .map(page => {
        const haystack = `${page.title} ${page.type} ${page.tags.join(" ")} ${page.excerpt}`.toLowerCase();
        return { page, score: haystack.includes(q) ? (page.title.toLowerCase().includes(q) ? 2 : 1) : 0 };
      })
      .filter(hit => hit.score)
      .sort((a, b) => b.score - a.score || a.page.title.localeCompare(b.page.title))
      .slice(0, 12);
    results.innerHTML = hits.map(({ page }) => `<a href="${root}${page.url}">${page.title}<small>${page.type}</small></a>`).join("");
    results.style.display = hits.length ? "block" : "none";
  });
  document.addEventListener("click", event => {
    if (!results.contains(event.target) && event.target !== input) results.style.display = "none";
  });
})();
"""


def build(out_dir: Path) -> None:
    pages = read_pages()
    lookup = build_lookup(pages)
    backlinks: dict[str, list[Page]] = defaultdict(list)
    for page in pages:
        for link in page.links:
            backlinks[link].append(page)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "assets").mkdir(parents=True)
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    (out_dir / "assets" / "site.css").write_text(CSS, encoding="utf-8")
    (out_dir / "assets" / "site.js").write_text(JS, encoding="utf-8")

    search = [
        {
            "title": page.title,
            "url": page.url,
            "type": page.page_type,
            "tags": page.tags,
            "excerpt": page.excerpt,
        }
        for page in sorted(pages, key=lambda p: p.title.lower())
    ]
    (out_dir / "assets" / "search.json").write_text(json.dumps(search, indent=2), encoding="utf-8")

    for page in pages:
        destination = out_dir / page.out_rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(page_html(page, pages, lookup, backlinks), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a static public HTML site from wiki/")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output directory")
    args = parser.parse_args()
    build(args.out.resolve())
    print(f"Built static wiki at {args.out.resolve()}")


if __name__ == "__main__":
    main()
