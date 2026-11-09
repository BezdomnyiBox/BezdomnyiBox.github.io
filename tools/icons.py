"""Favicon и иконки приложения.

Запуск из корня сайта:  python -X utf8 tools/icons.py   (нужен Pillow: pip install pillow)

Рисует знак «</>» на фиолетовом градиенте и сохраняет:
  favicon.svg           — основная иконка для современных браузеров
  favicon.ico           — 16, 32 и 48 px для старых браузеров и закладок
  apple-touch-icon.png  — 180 px, квадрат без прозрачности (iOS сам скругляет углы)
  icon-192.png, icon-512.png и site.webmanifest — для Android и «Добавить на главный экран»
"""
import json
import pathlib

from PIL import Image, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOP, BOTTOM = (0x8f, 0x7d, 0xff), (0x4b, 0x3e, 0xe0)   # цвета градиента: сверху-слева и снизу-справа
# Знак «</>» в системе координат 64×64: две «стрелки» и косая черта
STROKES = [[(24, 21), (13, 32), (24, 43)], [(40, 21), (51, 32), (40, 43)], [(35, 16), (29, 48)]]
STROKE_WIDTH = 5.5

SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#{''.join(f'{c:02x}' for c in TOP)}"/>
      <stop offset="1" stop-color="#{''.join(f'{c:02x}' for c in BOTTOM)}"/>
    </linearGradient>
  </defs>
  <circle cx="32" cy="32" r="32" fill="url(#g)"/>
  <path d="M24 21 13 32 24 43M40 21 51 32 40 43M35 16 29 48" fill="none" stroke="#fff" stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def gradient(size):
    img = Image.new("RGB", (size, size))
    px = []
    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * (size - 1))
            px.append(tuple(round(a + (b - a) * t) for a, b in zip(TOP, BOTTOM)))
    img.putdata(px)
    return img


def draw_icon(size, round_shape=True):
    """Рисуем в 4 раза крупнее и уменьшаем — так края получаются сглаженными."""
    big = size * 4
    k = big / 64
    icon = gradient(big).convert("RGBA")
    if round_shape:
        mask = Image.new("L", (big, big), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, big - 1, big - 1), fill=255)
        icon.putalpha(mask)
    draw = ImageDraw.Draw(icon)
    w = STROKE_WIDTH * k
    for stroke in STROKES:
        pts = [(x * k, y * k) for x, y in stroke]
        draw.line(pts, fill="white", width=round(w), joint="curve")
        for x, y in pts:  # скруглённые концы линий
            draw.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill="white")
    return icon.resize((size, size), Image.LANCZOS)


def main():
    (ROOT / "favicon.svg").write_text(SVG, encoding="utf-8", newline="\n")
    draw_icon(48).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    draw_icon(180, round_shape=False).convert("RGB").save(ROOT / "apple-touch-icon.png", optimize=True)
    for size in (192, 512):
        draw_icon(size).save(ROOT / f"icon-{size}.png", optimize=True)
    manifest = {
        "name": "Владимир — fullstack-разработчик",
        "short_name": "Владимир",
        "start_url": "/",
        "display": "browser",
        "theme_color": "#5b4cf0",
        "background_color": "#ffffff",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
        ],
    }
    (ROOT / "site.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("icons: favicon.svg, favicon.ico, apple-touch-icon.png, icon-192.png, icon-512.png, site.webmanifest")


if __name__ == "__main__":
    main()
