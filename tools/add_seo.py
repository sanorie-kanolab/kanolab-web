"""全ページに canonical / hreflang / OGP / JSON-LD を挿入し、sitemap.xml・robots.txt・llms.txt を生成する。

何度実行しても同じ結果になる（<!-- seo:start --> ～ <!-- seo:end --> を置き換える）。
公開 URL が変わったら BASE を書き換えて再実行する。
使い方: python3 -I tools/add_seo.py
"""
import html
import json
import re
from pathlib import Path

BASE = "https://sanorie-kanolab.github.io/kanolab-web/"  # 末尾はスラッシュ
ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- seo:start -->", "<!-- seo:end -->"
SITE_NAME = {"ja": "加納研究室", "en": "Kano Lab"}
LOCALE = {"ja": "ja_JP", "en": "en_US"}


def url_path(page: Path) -> str:
    """index.html の相対パスを公開 URL のパス部分に変換する。"""
    rel = page.relative_to(ROOT).parent.as_posix()
    return "" if rel == "." else rel + "/"


def counterpart(path: str) -> str:
    """日本語版 <-> 英語版の対応パスを返す。"""
    if path == "en/":
        return ""
    if path.startswith("en/"):
        return path[3:]
    return "en/" + path


def meta(text: str, pattern: str) -> str:
    m = re.search(pattern, text)
    return html.unescape(m.group(1)) if m else ""


def build_block(text: str, path: str, lang: str) -> str:
    title = meta(text, r"<title>(.*?)</title>")
    desc = meta(text, r'<meta name="description" content="(.*?)">')
    modified = meta(text, r'<time datetime="([\d-]+)"')
    other_lang = "en" if lang == "ja" else "ja"
    url = BASE + path
    other = BASE + counterpart(path)
    ja_url, en_url = (url, other) if lang == "ja" else (other, url)
    esc = lambda v: html.escape(v, quote=True)
    lines = [
        START,
        f'<link rel="canonical" href="{url}">',
        f'<link rel="alternate" hreflang="ja" href="{ja_url}">',
        f'<link rel="alternate" hreflang="en" href="{en_url}">',
        f'<link rel="alternate" hreflang="x-default" href="{ja_url}">',
        f'<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{esc(SITE_NAME[lang])}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:locale" content="{LOCALE[lang]}">',
        f'<meta property="og:locale:alternate" content="{LOCALE[other_lang]}">',
        f'<meta property="og:image" content="{BASE}assets/img/mascot.png">',
        '<meta name="twitter:card" content="summary">',
    ]
    # ホームには手書きの組織情報（ResearchOrganization）があるため、WebPage は下層ページのみ
    if path not in ("", "en/"):
        data = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": title,
            "description": desc,
            "url": url,
            "inLanguage": lang,
            "isPartOf": {"@type": "WebSite", "name": SITE_NAME[lang], "url": BASE + ("en/" if lang == "en" else "")},
            "publisher": {"@type": "ResearchOrganization", "name": "加納研究室", "alternateName": "Kano Lab"},
        }
        if modified:
            data["dateModified"] = modified
        lines.append('<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>")
    lines.append(END)
    return "\n  ".join(lines)


def main() -> None:
    pages = sorted(ROOT.rglob("index.html"))
    pages = [p for p in pages if ".git" not in p.parts]
    entries = []
    for page in pages:
        text = page.read_text(encoding="utf-8")
        text = re.sub(r"\n  " + re.escape(START) + r".*?" + re.escape(END), "", text, flags=re.S)
        path = url_path(page)
        lang = "en" if path.startswith("en/") or path == "en/" else "ja"
        block = build_block(text, path, lang)
        marker = re.search(r'(<meta name="description"[^>]*>)', text)
        assert marker, page
        text = text.replace(marker.group(1), marker.group(1) + "\n  " + block, 1)
        page.write_text(text, encoding="utf-8")
        entries.append((path, meta(text, r'<time datetime="([\d-]+)"')))

    ja = {p for p, _ in entries if not p.startswith("en/") and p != "en/"}
    rows = []
    for path, modified in entries:
        other = counterpart(path)
        alt = ""
        if other in {p for p, _ in entries}:
            ja_p, en_p = (path, other) if path in ja else (other, path)
            alt = (
                f'\n    <xhtml:link rel="alternate" hreflang="ja" href="{BASE}{ja_p}"/>'
                f'\n    <xhtml:link rel="alternate" hreflang="en" href="{BASE}{en_p}"/>'
            )
        last = f"\n    <lastmod>{modified}</lastmod>" if modified else ""
        rows.append(f"  <url>\n    <loc>{BASE}{path}</loc>{last}{alt}\n  </url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows) + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
    print(f"{len(entries)} pages")


if __name__ == "__main__":
    main()
