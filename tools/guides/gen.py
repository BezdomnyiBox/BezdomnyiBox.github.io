"""Генератор страниц учебников.

Запуск из корня сайта:  python -X utf8 tools/guides/gen.py

Контент учебников лежит рядом, в dev1.py, dev2.py (гайды по технологиям, папка guides/),
design1.py, design2.py (раздел «Дизайн», папка design/) и ai1.py (раздел «AI и LLM», папка ai/). После генерации
скрипт обновляет Open Graph-теги и sitemap.xml (tools/seo.py).
guides/symfony-patterns.html написан вручную и генератором не затрагивается.
"""
import html
import pathlib
import re
import sys
import textwrap

import ai1
import design1
import design2
import dev1
import dev2

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import seo  # noqa: E402

BACK = {"design": "Весь раздел «Дизайн»", "ai": "Весь раздел «AI и LLM»"}


def inline(s):
    parts = s.split("`")
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append("<code>" + html.escape(p, quote=False) + "</code>")
        else:
            t = html.escape(p, quote=False)
            t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
            out.append(t)
    return "".join(out)


def link(text, url, cls):
    ext = url.startswith("http")
    attrs = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="{cls}" href="{html.escape(url)}"{attrs}>{html.escape(text)}{" ↗" if ext else ""}</a>'


def block(b):
    if isinstance(b, str):
        return f"<p>{inline(b)}</p>"
    kind = b[0]
    if kind == "ul":
        return "<ul>" + "".join(f"<li>{inline(i)}</li>" for i in b[1]) + "</ul>"
    if kind == "code":
        _, lang, file, code = b
        code = textwrap.dedent(code).strip("\n")
        attr = f' data-file="{html.escape(file)}"' if file else ""
        return f'<pre{attr}><code class="language-{lang}">{html.escape(code, quote=False)}</code></pre>'
    if kind == "html":
        return b[1]
    if kind == "tiles":
        _, good, bad = b
        li = lambda items: "".join(f"<li>{inline(i)}</li>" for i in items)
        return ('<div class="tiles">'
                f'<div class="good"><h3>Запомнить</h3><ul>{li(good)}</ul></div>'
                f'<div class="bad"><h3>Частые ошибки</h3><ul>{li(bad)}</ul></div>'
                "</div>")
    raise ValueError(kind)


def page(g):
    plain, bold = g["h1"]
    title = f"{plain} {bold}"
    toc = "".join(f'<li><a href="#{sid}">{html.escape(t)}</a></li>' for sid, t, _ in g["sections"])
    sections = "\n".join(
        f'        <section class="lesson" id="{sid}">\n'
        f'          <h2><span>{n:02d}</span>{html.escape(t)}</h2>\n'
        + "\n".join("          " + block(b) for b in blocks) +
        "\n        </section>"
        for n, (sid, t, blocks) in enumerate(g["sections"], 1)
    )
    facts = "".join(f"<span>{html.escape(f)}</span>" for f in g["facts"])
    icon = g.get("icon_html") or html.escape(g["icon"])
    links = "".join(link(t, u, "pill ghost") for t, u in g["links"])
    parent_title, parent_url = g.get("parent", ("Гайды", "../guides.html"))
    page_key = g.get("page", "guides")
    head_extra = g.get("head_extra", "")
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} — Владимир</title>
  <meta name="description" content="{html.escape(g['lead'])}">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#5b4cf0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"></noscript>
  <link rel="stylesheet" href="../styles.css">
  <link rel="stylesheet" href="../docs.css">
  <script src="../theme.js"></script>
  <script src="../layout.js" data-base="../" data-page="{page_key}" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js" defer></script>{head_extra}
</head>
<body>
  <header class="site-header" data-layout="header"></header>

  <main class="wrap">
    <div class="doc-hero" style="--hero-bg: {g['bg']}">
      <div>
        <div class="crumbs"><a href="{parent_url}">{parent_title}</a> / {html.escape(g['category'])}</div>
        <h1>{html.escape(plain)} <b>{html.escape(bold)}</b></h1>
        <p>{inline(g['lead'])}</p>
        <div class="hero-facts">{facts}</div>
      </div>
      <div class="icon i-{g['color']}">{icon}</div>
    </div>

    <div class="guide">
      <aside class="toc">
        <p class="toc-title">Содержание</p>
        <ol>{toc}</ol>
      </aside>

      <div>
{sections}
        <section class="lesson" id="next">
          <h2>Что дальше</h2>
          <p>{inline(g['next'])}</p>
          <div class="next-steps"><a class="pill" href="{parent_url}">{BACK.get(page_key, "Все гайды")}</a>{links}</div>
        </section>
      </div>
    </div>
  </main>

  <footer class="site-footer" data-layout="footer"></footer>
</body>
</html>
"""


if __name__ == "__main__":
    for g in dev1.GUIDES + dev2.GUIDES + design1.GUIDES + design2.GUIDES + ai1.GUIDES:
        out = ROOT / g.get("folder", "guides")
        out.mkdir(exist_ok=True)
        (out / f"{g['slug']}.html").write_text(page(g), encoding="utf-8", newline="\n")
        print("written", g["slug"], len(g["sections"]), "sections")
    seo.main()
