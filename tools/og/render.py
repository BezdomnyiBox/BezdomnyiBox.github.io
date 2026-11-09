"""Рендер обложек для превью ссылок (1200×630) в og/*.jpg.

Запуск из корня сайта:  python -X utf8 tools/og/render.py
Нужен установленный Microsoft Edge или Google Chrome (страница tools/og/cover.html
открывается в фоновом режиме и сохраняется как скриншот) и Pillow для сжатия в JPEG.
JPEG весит примерно в 6 раз меньше PNG — превью в мессенджерах появляется быстрее.
"""
import pathlib
import shutil
import subprocess
import time

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[2]
TEMPLATE = (ROOT / "tools" / "og" / "cover.html").as_uri()
OUT = ROOT / "og"
VARIANTS = {"main": "cover.jpg", "guides": "guides.jpg", "design": "design.jpg", "ai": "ai.jpg"}
QUALITY = 85

CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "msedge", "google-chrome", "chromium", "chrome",
]


def browser():
    for c in CANDIDATES:
        path = c if pathlib.Path(c).exists() else shutil.which(c)
        if path:
            return path
    raise SystemExit("Не найден Edge или Chrome — установите один из них")


def wait_for_file(path, timeout=30):
    """Edge на Windows возвращает управление раньше, чем дописывает скриншот, — ждём готовый файл."""
    last = -1
    for _ in range(timeout * 4):
        size = path.stat().st_size if path.exists() else -1
        if size > 0 and size == last:
            return
        last = size
        time.sleep(.25)
    raise SystemExit(f"Браузер не сохранил скриншот: {path}")


def main():
    exe = browser()
    OUT.mkdir(exist_ok=True)
    for variant, name in VARIANTS.items():
        # Скриншот кладём рядом с результатом: в системную временную папку браузер писать не может
        shot = OUT / f".{variant}.tmp.png"
        subprocess.run([
            exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
            "--window-size=1200,630", "--virtual-time-budget=8000",
            f"--screenshot={shot}", f"{TEMPLATE}?v={variant}",
        ], check=True, capture_output=True)
        wait_for_file(shot)
        target = OUT / name
        with Image.open(shot) as img:
            img.convert("RGB").save(target, "JPEG", quality=QUALITY, optimize=True, progressive=True)
            size = img.size
        shot.unlink()
        print(f"{name}: {size[0]}×{size[1]}, {target.stat().st_size // 1024} КБ")


if __name__ == "__main__":
    main()
