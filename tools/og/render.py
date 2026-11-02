"""Рендер обложек для превью ссылок (1200×630) в og/*.png.

Запуск из корня сайта:  python -X utf8 tools/og/render.py
Нужен установленный Microsoft Edge или Google Chrome: страница tools/og/cover.html
открывается в фоновом (headless) режиме и сохраняется как скриншот.
"""
import pathlib
import shutil
import struct
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
TEMPLATE = (ROOT / "tools" / "og" / "cover.html").as_uri()
OUT = ROOT / "og"
VARIANTS = {"main": "cover.png", "guides": "guides.png", "design": "design.png"}

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


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


def main():
    exe = browser()
    OUT.mkdir(exist_ok=True)
    for variant, name in VARIANTS.items():
        target = OUT / name
        subprocess.run([
            exe, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
            "--window-size=1200,630", "--virtual-time-budget=8000",
            f"--screenshot={target}", f"{TEMPLATE}?v={variant}",
        ], check=True, capture_output=True)
        print(f"{name}: {png_size(target)[0]}×{png_size(target)[1]}")


if __name__ == "__main__":
    main()
