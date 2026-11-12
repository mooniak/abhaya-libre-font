"""mnik.mdrender — dependency-free markdown → HTML fragment renderer.

Shared by ``mnik.qa`` (fontspector ghmarkdown reports) and ``mnik.proofpdf``
(frontmattered Sinhala test-string sections). Handles headings, paragraphs,
fenced code, inline code/links/bold/italic, GFM tables, lists, raw HTML
passthrough and horizontal rules — enough for both sources without pulling in
a markdown dependency.
"""
from __future__ import annotations

import html as _html
import re

_INLINE_CODE = re.compile(r"`([^`]+)`")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC = re.compile(r"(?<![\*\w])\*([^*]+)\*(?![\*\w])")
_HTML_LINE = re.compile(r"^</?[a-zA-Z][^>]*>?")
_TABLE_SEP = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")
_LI = re.compile(r"^([-*+]|\d+\.)\s+")


def _inline(s: str) -> str:
    s = _INLINE_CODE.sub(lambda m: "<code>" + _html.escape(m.group(1)) + "</code>", s)
    s = _LINK.sub(lambda m: f'<a href="{m.group(2)}" target="_blank" '
                            f'rel="noopener">{m.group(1)}</a>', s)
    s = _BOLD.sub(r"<strong>\1</strong>", s)
    s = _ITALIC.sub(r"<em>\1</em>", s)
    return s


def _split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _render_table(header: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{_inline(c)}</th>" for c in header)
    body = []
    for r in rows:
        cells = (r + [""] * len(header))[:len(header)]
        body.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in cells) + "</tr>")
    return (f"<table class='qa-table'><thead><tr>{th}</tr></thead>"
            f"<tbody>{''.join(body)}</tbody></table>")


def md_to_html(md: str) -> str:
    """Render a markdown body to an HTML fragment (no <html> wrapper)."""
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    para: list[str] = []
    i, n = 0, len(lines)

    def flush():
        if para:
            out.append("<p>" + _inline(" ".join(para)) + "</p>")
            para.clear()

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):                       # fenced code
            flush()
            code, i = [], i + 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            out.append("<pre><code>" + _html.escape("\n".join(code)) + "</code></pre>")
            continue
        if not stripped:                                     # blank line
            flush(); i += 1; continue
        if _HTML_LINE.match(stripped):                       # raw HTML (details/summary/…)
            flush(); out.append(line); i += 1; continue
        m = re.match(r"(#{1,6})\s+(.*)", stripped)           # heading
        if m:
            flush()
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{_inline(m.group(2).strip())}</h{lvl}>"); i += 1; continue
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):  # horizontal rule
            flush(); out.append("<hr>"); i += 1; continue
        if "|" in stripped and i + 1 < n and "|" in lines[i + 1] \
                and _TABLE_SEP.match(lines[i + 1]):          # GFM table
            flush()
            header = _split_row(stripped); i += 2
            rows = []
            while i < n and lines[i].strip() and "|" in lines[i]:
                rows.append(_split_row(lines[i])); i += 1
            out.append(_render_table(header, rows)); continue
        if _LI.match(stripped):                              # list
            flush()
            ordered = bool(re.match(r"^\d+\.\s+", stripped))
            items = []
            while i < n and lines[i].strip() and _LI.match(lines[i].strip()):
                items.append("<li>" + _inline(_LI.sub("", lines[i].strip())) + "</li>")
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>{''.join(items)}</{tag}>"); continue
        para.append(stripped); i += 1                        # paragraph text

    flush()
    return "\n".join(out)
