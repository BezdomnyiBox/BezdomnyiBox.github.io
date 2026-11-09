# Служебные скрипты

Папка не публикуется на сайте (исключена в `_config.yml`). Все команды запускаются из корня репозитория, нужен Python 3.10+. Для иконок и обложек — ещё Pillow (`pip install pillow`).

| Скрипт | Что делает |
|---|---|
| `guides/gen.py` | Собирает учебники в `guides/`, `design/` и `ai/` из контента в `guides/*.py`, затем запускает `seo.py` |
| `seo.py` | Добавляет Open Graph-теги на все страницы и пересобирает `sitemap.xml` |
| `og/render.py` | Рисует обложки для превью ссылок `og/cover.jpg`, `og/guides.jpg`, `og/design.jpg`, `og/ai.jpg` |
| `icons.py` | Рисует favicon (`favicon.svg`, `favicon.ico`), иконки для iPhone и Android и `site.webmanifest` |

## Учебники

```bash
python -X utf8 tools/guides/gen.py
```

Контент разложен по файлам:

| Файл | Учебники |
|---|---|
| `guides/dev1.py` | React, TypeScript, Docker, SQL |
| `guides/dev2.py` | ООП, REST API, Git, ML |
| `guides/design1.py` | Шрифты, законы дизайна |
| `guides/design2.py` | Цвет, анимации, доступность, UI-состояния, дизайн-токены |
| `guides/ai1.py` | LLM API, вызов инструментов, безопасность LLM, тестирование, Symfony AI |

Каждый учебник — словарь: заголовок, описание, цвет иконки и список разделов. Раздел состоит из блоков:

- строка — абзац, внутри работают `` `код` `` и `**жирный**`;
- `("ul", [...])` — список;
- `("code", "язык", "файл или None", r"""код""")` — блок кода с подсветкой;
- `("html", "...")` — произвольный HTML для живых примеров;
- `("tiles", [запомнить], [ошибки])` — плитки «Запомнить / Частые ошибки».

Новый учебник: добавьте словарь в один из файлов (или новый файл + импорт в `gen.py`), запустите генератор и добавьте карточку в `guides-data.js`, `design.html` или `ai.html`.

`guides/symfony-patterns.html`, страницы галереи стилей и кейсы в `projects/` написаны вручную — генератор их не трогает.

## Open Graph и sitemap

```bash
python -X utf8 tools/seo.py
```

Запускайте после добавления или переименования любой страницы. Заголовок и описание превью берутся из `<title>` и `<meta name="description">` страницы. Обложка выбирается по разделу: `design*` → `og/design.jpg`, `guide*` → `og/guides.jpg`, `ai*` и кейс AI-ассистента → `og/ai.jpg`, остальное → `og/cover.jpg`.

## Обложки

```bash
python -X utf8 tools/og/render.py
```

Нужен установленный Edge или Chrome. Шаблон — `og/cover.html`, варианты текста — в его скрипте (`VARIANTS`). Если превью в Telegram не обновилось, отправьте ссылку боту [@WebpageBot](https://t.me/WebpageBot) — он сбросит кеш.
