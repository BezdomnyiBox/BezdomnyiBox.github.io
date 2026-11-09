"""Open Graph-теги для всех страниц и sitemap.xml.

Запуск из корня сайта:  python -X utf8 tools/seo.py

Заголовок и описание берутся из <title> и <meta name="description"> каждой страницы.
Блок между <!-- og: … --> и <!-- /og --> пересоздаётся при каждом запуске, поэтому
скрипт можно запускать сколько угодно раз. Обложки лежат в og/ (рисует tools/og/render.py).
"""
import datetime
import html
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = "https://bezdomnyibox.github.io"
SITE_NAME = "Владимир — fullstack-разработчик"
SKIP = {"404.html"}  # служебная страница: без OG-тегов и не в sitemap

OG_BLOCK = re.compile(r"\n[ \t]*<!-- og: .*?<!-- /og -->", re.S)


def pages():
    yield from sorted(ROOT.glob("*.html"))
    for folder in ("projects", "guides", "design", "ai"):
        yield from sorted((ROOT / folder).glob("*.html"))


def rel_path(p):
    return p.relative_to(ROOT).as_posix()


def url_of(rel):
    return SITE + "/" + ("" if rel == "index.html" else rel)


def image_of(rel):
    if rel.startswith("design"):
        return "og/design.jpg"
    if rel.startswith("guide"):
        return "og/guides.jpg"
    if rel.startswith("ai") or rel == "projects/ai-assistant.html":
        return "og/ai.jpg"
    return "og/cover.jpg"


def attr(s):
    return html.escape(html.unescape(s.strip()), quote=True)


def og_block(rel, text):
    title = re.search(r"<title>(.*?)</title>", text, re.S).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', text, re.S)
    desc = desc.group(1) if desc else ""
    url = url_of(rel)
    image = f"{SITE}/{image_of(rel)}"
    tags = [
        "<!-- og: создаётся tools/seo.py, не редактируйте вручную -->",
        f'<link rel="canonical" href="{url}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{attr(SITE_NAME)}">',
        '<meta property="og:locale" content="ru_RU">',
        f'<meta property="og:title" content="{attr(title)}">',
        f'<meta property="og:description" content="{attr(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{image}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{attr(title)}">',
        '<meta name="twitter:card" content="summary_large_image">',
        "<!-- /og -->",
    ]
    return "\n" + "\n".join("  " + t for t in tags)


def add_og(p):
    rel = rel_path(p)
    text = p.read_text(encoding="utf-8")
    text = OG_BLOCK.sub("", text)
    anchor = re.search(r'<meta name="description" content=".*?">', text, re.S) or re.search(r"<title>.*?</title>", text, re.S)
    text = text[:anchor.end()] + og_block(rel, text) + text[anchor.end():]
    p.write_text(text, encoding="utf-8", newline="\n")


def lastmod(p):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(p)],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        out = ""
    return out or datetime.date.today().isoformat()


def write_sitemap(all_pages):
    urls = "\n".join(
        f"  <url><loc>{url_of(rel_path(p))}</loc><lastmod>{lastmod(p)}</lastmod></url>" for p in all_pages)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n"
        "</urlset>\n", encoding="utf-8", newline="\n")


def main():
    site_pages = [p for p in pages() if rel_path(p) not in SKIP]
    for p in site_pages:
        add_og(p)
    write_sitemap(site_pages)
    print(f"seo: OG-теги на {len(site_pages)} страницах, sitemap.xml обновлён")


if __name__ == "__main__":
    main()
