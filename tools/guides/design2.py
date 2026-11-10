PARENT = ("Дизайн", "../design.html")

# ---------------------------------------------------------------- Цвет
COLORS_HEAD = """
  <style>
    .ramp { display: flex; border-radius: 16px; overflow: hidden; margin-top: 16px; }
    .ramp div { flex: 1; height: 72px; display: flex; align-items: flex-end; padding: 6px; font: 500 11px "JetBrains Mono", monospace; }
    .harm { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; margin-top: 16px; }
    .harm figure { margin: 0; background: var(--tile); border-radius: 16px; padding: 18px; display: flex; flex-direction: column; align-items: center; gap: 12px; }
    .harm .dots { display: flex; gap: 6px; }
    .harm .dots i { width: 34px; height: 34px; border-radius: 50%; display: block; }
    .harm figcaption { font-size: 13px; color: var(--muted); text-align: center; }
    .sem { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; margin-top: 16px; }
    .sem div { border-radius: 14px; padding: 14px 16px; font-size: 14px; font-weight: 500; }
    .themes { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-top: 16px; }
    .themes > div { border-radius: 18px; padding: 18px; font-size: 14px; }
    .themes .mock { border-radius: 14px; padding: 16px; margin-top: 10px; }
    .themes .mock b { display: block; font-size: 18px; margin-bottom: 4px; }
    .themes .mock span { display: inline-block; margin-top: 12px; padding: 8px 14px; border-radius: 999px; font-weight: 500; }
    .themes small { display: block; font-size: 12px; text-transform: uppercase; letter-spacing: .08em; opacity: .7; }
  </style>"""

RAMP = [(97, .02), (92, .05), (85, .09), (76, .14), (66, .18), (57, .2), (49, .19), (41, .16), (33, .12), (26, .08)]
ramp_html = '<div class="ramp">' + "".join(
    f'<div style="background: oklch({l}% {c} 280); color: {"#fff" if i >= 5 else "#1a1a1f"}">{(i * 100) or 50}</div>'
    for i, (l, c) in enumerate(RAMP)) + "</div>"


def dots(hues, l=(65,)):
    if len(l) == 1:
        l = l * len(hues)
    return '<div class="dots">' + "".join(f'<i style="background: oklch({li}% .17 {h})"></i>' for h, li in zip(hues, l)) + "</div>"


COLORS = {
    "slug": "colors", "folder": "design", "parent": PARENT, "page": "design",
    "h1": ("Цвет", "и палитры"),
    "category": "Цвет",
    "lead": "Как построить палитру из одного цвета, подобрать гармонию, выбрать нейтральные и смысловые цвета и правильно сделать тёмную тему.",
    "facts": ["7 уроков", "~15 минут", "OKLCH и CSS"],
    "icon": "Co", "color": "ml",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(255, 211, 25, .45) 0%, transparent 60%), radial-gradient(45% 80% at 10% 90%, rgba(111, 227, 192, .45) 0%, transparent 60%), linear-gradient(135deg, #4a0d2c, #8c1c48 50%, #d0563a)",
    "head_extra": COLORS_HEAD,
    "sections": [
        ("models", "Цветовые модели", [
            ("ul", [
                "**HEX и RGB** (`#5b4cf0`, `rgb(91 76 240)`) — привычные, но по числам не понять, светлый цвет или тёмный.",
                "**HSL** (`hsl(246 85% 62%)`) — оттенок, насыщенность, светлота. Понятнее, но жёлтый и синий с одинаковой «светлотой» выглядят по-разному яркими.",
                "**OKLCH** (`oklch(57% .2 280)`) — светлота, насыщенность, оттенок, рассчитанные под восприятие глаза. Одинаковая светлота действительно выглядит одинаково — идеально для палитр и тёмной темы. Поддерживается всеми современными браузерами.",
            ]),
            ("code", "css", None, r"""
:root {
  --accent: #5b4cf0;                       /* HEX */
  --accent: hsl(246 85% 62%);              /* HSL */
  --accent: oklch(57% 0.2 280);            /* OKLCH: светлота, насыщенность, оттенок */
  --accent-soft: color-mix(in oklch, var(--accent) 15%, white);   /* смешивание цветов */
}
"""),
        ]),
        ("ramp", "Палитра из одного цвета", [
            "Основу дизайн-системы строят из шкалы оттенков одного цвета: от почти белого (50) до почти чёрного (900). В OKLCH это просто — меняется светлота, а оттенок остаётся тем же:",
            ("html", ramp_html),
            ("code", "css", "tokens.css", r"""
:root {
  --violet-50:  oklch(97% 0.02 280);
  --violet-100: oklch(92% 0.05 280);
  --violet-500: oklch(57% 0.20 280);   /* основной */
  --violet-700: oklch(41% 0.16 280);   /* наведение на кнопку */
  --violet-900: oklch(26% 0.08 280);
}
"""),
            "Светлые ступени (50–100) — фоны и плашки, средние (400–600) — кнопки и ссылки, тёмные (700–900) — наведение, текст на светлых плашках.",
        ]),
        ("harmony", "Цветовые гармонии", [
            "Если нужен второй цвет, его берут по правилам цветового круга:",
            ("html", '<div class="harm">'
                     f'<figure>{dots([280, 280, 280, 280], (35, 50, 65, 80))}<figcaption><b>Монохромная</b> — один оттенок разной светлоты. Спокойно и надёжно</figcaption></figure>'
                     f'<figure>{dots([240, 280, 320])}<figcaption><b>Аналоговая</b> — соседние оттенки. Мягко и гармонично</figcaption></figure>'
                     f'<figure>{dots([280, 100])}<figcaption><b>Комплементарная</b> — противоположные оттенки. Максимальный контраст для акцента</figcaption></figure>'
                     f'<figure>{dots([280, 40, 160])}<figcaption><b>Триада</b> — три оттенка через 120°. Ярко, нужна аккуратность</figcaption></figure>'
                     "</div>"),
            "В интерфейсе почти всегда хватает **монохромной** палитры плюс один акцент для главных действий. Не путайте с правилом 60-30-10 из гайда «Законы дизайна»: гармония выбирает цвета, а 60-30-10 — их пропорции.",
        ]),
        ("neutral", "Нейтральные и смысловые цвета", [
            "**Нейтральные** (серые) занимают 80–90% интерфейса: фон, текст, рамки. Чисто серые выглядят мёртво — добавьте в них каплю основного оттенка: `oklch(97% 0.005 280)` вместо `#f5f5f5`.",
            "**Смысловые** цвета сообщают статус и одинаково понятны во всех продуктах:",
            ("html", '<div class="sem">'
                     '<div style="background: oklch(94% .05 150); color: oklch(38% .12 150)">Успех — зелёный</div>'
                     '<div style="background: oklch(95% .06 85); color: oklch(42% .1 70)">Предупреждение — жёлтый</div>'
                     '<div style="background: oklch(94% .04 25); color: oklch(45% .16 25)">Ошибка — красный</div>'
                     '<div style="background: oklch(94% .04 250); color: oklch(42% .14 250)">Информация — синий</div>'
                     "</div>"),
            "Не используйте красный как фирменный акцент, если в интерфейсе есть ошибки: пользователь перестанет их отличать.",
        ]),
        ("dark", "Тёмная тема: правила", [
            "Тёмная тема — это не инверсия цветов, а отдельная палитра со своими правилами:",
            ("ul", [
                "**Фон не чисто чёрный.** `#121214` вместо `#000`: на чистом чёрном белый текст «дрожит», а тени не видны.",
                "**Чем выше элемент, тем светлее поверхность.** Тени в темноте почти не работают, глубину показывают светлотой: фон `#121214`, карточка `#1e1f23`, всплывающее окно `#2a2b30`.",
                "**Текст не чисто белый.** `#ececf0` или белый с прозрачностью 87% — меньше слепит.",
                "**Акцент светлее и мягче.** Насыщенный фиолетовый с белого фона на тёмном становится тусклым — поднимите светлоту.",
                "**Проверяйте контраст заново** — значения из светлой темы не переносятся.",
            ]),
            ("html", '<div class="themes">'
                     '<div style="background: #f4f4f6; color: #1a1a1f"><small>Светлая</small><div class="mock" style="background: #fff"><b>Фильтр масляный</b>890 ₽ · в наличии<br><span style="background: #5b4cf0; color: #fff">В корзину</span></div></div>'
                     '<div style="background: #121214; color: #ececf0"><small>Тёмная</small><div class="mock" style="background: #1e1f23"><b>Фильтр масляный</b><span style="all: unset; color: #9a9ca6">890 ₽ · в наличии</span><br><span style="background: #8f83ff; color: #121214">В корзину</span></div></div>'
                     "</div>"),
        ]),
        ("css", "Тёмная тема в CSS", [
            "Компоненты используют только переменные-токены, а тема переопределяет их значения. Так работает и этот сайт — переключатель в шапке меняет атрибут `data-theme`:",
            ("code", "css", "styles.css", r"""
:root {
  --bg: #ffffff;
  --text: #1a1a1f;
  --accent: #5b4cf0;
  color-scheme: light;
}

/* Системная тема, если пользователь ничего не выбирал */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #121214;
    --text: #ececf0;
    --accent: #8f83ff;
    color-scheme: dark;     /* тёмные полосы прокрутки и поля ввода */
  }
}

/* Явный выбор пользователя */
:root[data-theme="dark"] { --bg: #121214; --text: #ececf0; --accent: #8f83ff; color-scheme: dark; }

/* Короткая запись для отдельных значений */
.note { background: light-dark(#f2f3f5, #1e1f23); }
"""),
            "Выбор пользователя сохраняйте в `localStorage` и применяйте до отрисовки страницы, иначе при загрузке тёмная тема будет «мигать» белым.",
        ]),
        ("tools", "Инструменты и шпаргалка", [
            ("ul", [
                "**oklch.com** — подбор цвета в OKLCH с проверкой охвата.",
                "**Realtime Colors** — примерка палитры сразу на макете сайта.",
                "**Проверка контраста** — встроена в DevTools браузера: кликните по цвету текста в панели стилей.",
            ]),
            ("tiles", [
                "Один основной цвет + шкала его оттенков.",
                "Нейтральные серые с каплей основного оттенка.",
                "Смысловые цвета только для статусов.",
                "В тёмной теме глубина — светлотой, а не тенями.",
            ], [
                "Пять ярких цветов «чтобы было весело».",
                "Чисто чёрный фон и чисто белый текст.",
                "Тёмная тема через `filter: invert(1)`.",
                "Красный акцент рядом с красными ошибками.",
            ]),
        ]),
    ],
    "next": "Соберите палитру своего проекта в генераторе палитры — он построит шкалу в OKLCH, проверит контраст и выдаст готовые токены. Затем проверьте палитру в обеих темах.",
    "links": [("Генератор палитры", "palette.html"), ("Дизайн-токены", "tokens.html"), ("oklch.com", "https://oklch.com/")],
}

# ---------------------------------------------------------------- Анимации
MOTION_HEAD = """
  <style>
    .ease { display: flex; flex-direction: column; gap: 10px; margin-top: 16px; background: var(--tile); border-radius: 16px; padding: 16px 18px; }
    .ease-row { display: grid; grid-template-columns: 150px minmax(0, 1fr); align-items: center; gap: 12px; font: 12px "JetBrains Mono", monospace; color: var(--muted); }
    .ease-track { height: 28px; border-radius: 14px; background: var(--bg); container-type: inline-size; }
    .ease-dot { width: 20px; height: 20px; margin: 4px; border-radius: 50%; background: var(--accent); animation: ease-move 1.6s infinite alternate var(--e); }
    @keyframes ease-move { to { transform: translateX(calc(100cqw - 28px)); } }
    .micro { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 16px; }
    .micro > div { background: var(--tile); border-radius: 16px; padding: 22px; display: flex; flex-direction: column; align-items: center; gap: 12px; }
    .micro small { font-size: 13px; color: var(--muted); text-align: center; }
    .m-press { border: 0; cursor: pointer; padding: 12px 22px; border-radius: 999px; background: var(--accent); color: #fff; font: 500 15px Onest, sans-serif; transition: transform .1s ease-out, box-shadow .2s; }
    .m-press:hover { box-shadow: 0 6px 18px rgba(91, 76, 240, .35); }
    .m-press:active { transform: scale(.95); }
    .m-like { border: 0; background: none; cursor: pointer; font-size: 34px; line-height: 1; color: var(--muted); }
    .m-like.on { color: #e8457a; animation: like-pop .35s cubic-bezier(.34, 1.56, .64, 1); }
    @keyframes like-pop { 0% { transform: scale(.6); } 100% { transform: scale(1); } }
    .m-copy { border: 1px solid var(--line); background: var(--bg); color: var(--text); cursor: pointer; padding: 10px 18px; border-radius: 10px; font: 500 14px Onest, sans-serif; min-width: 150px; transition: background .2s, color .2s; }
    .m-copy.done { background: #22b07d; color: #fff; border-color: transparent; }
    @media (prefers-reduced-motion: reduce) { .ease-dot, .m-like.on { animation: none; } }
  </style>"""

MOTION = {
    "slug": "motion", "folder": "design", "parent": PARENT, "page": "design",
    "h1": ("Анимации", "и микровзаимодействия"),
    "category": "Анимация",
    "lead": "Зачем нужна анимация, какую длительность и кривую выбрать, что анимировать без тормозов и когда анимация мешает.",
    "facts": ["7 уроков", "~15 минут", "CSS и JS"],
    "icon": "Mo", "color": "ts",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(125, 249, 255, .45) 0%, transparent 60%), linear-gradient(135deg, #0b2f6b, #2f7fd4 55%, #14a3a0)",
    "head_extra": MOTION_HEAD,
    "sections": [
        ("why", "Зачем нужна анимация", [
            "Хорошая анимация не украшает, а объясняет. У неё три задачи:",
            ("ul", [
                "**Обратная связь.** Кнопка откликнулась на нажатие, товар «прилетел» в корзину — пользователь понимает, что действие сработало.",
                "**Связь состояний.** Меню выезжает оттуда, где была кнопка, — понятно, откуда оно взялось и куда денется.",
                "**Внимание.** Мягкая пульсация показывает, куда смотреть. Но только одна на экране.",
            ]),
        ]),
        ("duration", "Длительность", [
            ("ul", [
                "**100–150 мс** — отклик на действие: нажатие, наведение, переключатель.",
                "**200–300 мс** — появление и исчезновение элементов: подсказки, выпадающие меню, модальные окна.",
                "**300–500 мс** — крупные перемещения и переходы между экранами.",
                "Больше 500 мс — только для декоративных и фоновых анимаций, которые ничего не блокируют.",
            ]),
            "Исчезновение делайте **быстрее** появления: убранное пользователю уже не нужно, ждать его незачем.",
        ]),
        ("easing", "Кривые плавности", [
            "Кривая задаёт, как меняется скорость. В природе ничего не движется с постоянной скоростью, поэтому `linear` выглядит механически:",
            ("html", '<div class="ease">'
                     '<div class="ease-row"><span>linear</span><div class="ease-track"><div class="ease-dot" style="--e: linear"></div></div></div>'
                     '<div class="ease-row"><span>ease-in</span><div class="ease-track"><div class="ease-dot" style="--e: ease-in"></div></div></div>'
                     '<div class="ease-row"><span>ease-out</span><div class="ease-track"><div class="ease-dot" style="--e: ease-out"></div></div></div>'
                     '<div class="ease-row"><span>ease-in-out</span><div class="ease-track"><div class="ease-dot" style="--e: ease-in-out"></div></div></div>'
                     '<div class="ease-row"><span>пружина</span><div class="ease-track"><div class="ease-dot" style="--e: cubic-bezier(.34, 1.56, .64, 1)"></div></div></div>'
                     "</div>"),
            ("ul", [
                "**ease-out** (быстро начинается, плавно останавливается) — для появления. Самая частая кривая в интерфейсах.",
                "**ease-in** (медленно начинается, разгоняется) — для исчезновения: элемент «уходит».",
                "**ease-in-out** — для перемещения из точки в точку.",
                "**Пружина** с выходом за край — для игривых акцентов: лайк, бейдж, всплывающая кнопка.",
            ]),
            ("code", "css", None, r"""
:root {
  --ease-out: cubic-bezier(.22, 1, .36, 1);
  --ease-spring: cubic-bezier(.34, 1.56, .64, 1);
  --dur-fast: 120ms;
  --dur-base: 240ms;
}
.menu { transition: opacity var(--dur-base) var(--ease-out), transform var(--dur-base) var(--ease-out); }
"""),
        ]),
        ("perf", "Что анимировать", [
            "Плавно анимируются только `transform` и `opacity`: браузер двигает уже нарисованный слой на видеокарте. Изменение `width`, `height`, `top`, `margin` заставляет пересчитывать раскладку всей страницы — и анимация дёргается.",
            ("code", "css", None, r"""
/* ❌ пересчёт раскладки на каждом кадре */
.drawer { transition: left .3s; left: -300px; }
.drawer.open { left: 0; }

/* ✅ только сдвиг слоя */
.drawer { transition: transform .3s var(--ease-out); transform: translateX(-100%); }
.drawer.open { transform: none; }
"""),
            "`will-change: transform` подсказывает браузеру заранее вынести элемент в слой. Ставьте его точечно и только на то, что действительно анимируется, — каждый слой занимает память.",
        ]),
        ("micro", "Микровзаимодействия", [
            "Маленькие анимации-отклики делают интерфейс «живым». Понажимайте:",
            ("html", '<div class="micro">'
                     '<div><button class="m-press" type="button">Нажми меня</button><small>Кнопка чуть уменьшается при нажатии</small></div>'
                     '<div><button class="m-like" type="button" aria-pressed="false" aria-label="Нравится">♥</button><small>Лайк «выпрыгивает» с пружиной</small></div>'
                     '<div><button class="m-copy" type="button">Скопировать</button><small>Кнопка подтверждает действие</small></div>'
                     "</div>"
                     "<script>"
                     "document.querySelector('.m-like').addEventListener('click', e => { const b = e.currentTarget; const on = b.classList.toggle('on'); b.setAttribute('aria-pressed', on); });"
                     "document.querySelector('.m-copy').addEventListener('click', e => { const b = e.currentTarget; b.classList.add('done'); b.textContent = 'Скопировано ✓'; setTimeout(() => { b.classList.remove('done'); b.textContent = 'Скопировать'; }, 1500); });"
                     "</script>"),
            ("code", "css", None, r"""
.button { transition: transform .1s ease-out; }
.button:active { transform: scale(.95); }

.like.on { animation: like-pop .35s cubic-bezier(.34, 1.56, .64, 1); }
@keyframes like-pop { from { transform: scale(.6); } to { transform: scale(1); } }
"""),
        ]),
        ("transitions", "Появление элементов", [
            "Раньше анимировать появление элемента из `display: none` было нельзя без JavaScript. Теперь для этого есть `@starting-style` — стили, с которых элемент начинает анимацию при появлении:",
            ("code", "css", None, r"""
.toast {
  transition: opacity .25s ease-out, transform .25s ease-out;
  @starting-style {            /* состояние в момент появления */
    opacity: 0;
    transform: translateY(12px);
  }
}
"""),
            "Для плавной смены целых экранов есть **View Transitions API**: браузер сам делает плавный переход между старым и новым состоянием страницы.",
            ("code", "javascript", None, r"""
// Плавно меняем содержимое, если браузер поддерживает API
if (document.startViewTransition) {
  document.startViewTransition(() => renderPage(nextPage));
} else {
  renderPage(nextPage);
}
"""),
        ]),
        ("harm", "Когда анимация мешает", [
            ("ul", [
                "Анимация **блокирует** действие: пока меню медленно выезжает, кликнуть некуда.",
                "Анимация **повторяется** каждый раз, хотя пользователь уже видел её сто раз.",
                "Много движения одновременно — глаз не понимает, куда смотреть.",
                "Параллакс и масштабирование при прокрутке у части людей вызывают головокружение и тошноту.",
            ]),
            "В системах есть настройка «Уменьшить движение». Уважайте её — оставляйте только короткие переходы прозрачности:",
            ("code", "css", None, r"""
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
    scroll-behavior: auto !important;
  }
}
"""),
            ("tiles", [
                "Анимация объясняет, а не украшает.",
                "Отклик — 100–150 мс, появление — 200–300 мс.",
                "Появление — ease-out, исчезновение — быстрее.",
                "Анимируйте только `transform` и `opacity`.",
            ], [
                "`transition: all 1s` на всём подряд.",
                "`linear` для движения интерфейса.",
                "Анимация `width`, `top` и `margin`.",
                "Игнорирование `prefers-reduced-motion`.",
            ]),
        ]),
    ],
    "next": "Пройдитесь по своему интерфейсу и проверьте каждую анимацию: что она объясняет и сколько длится. Посмотрите, как анимации работают в разных стилях галереи.",
    "links": [("Галерея стилей", "styles.html"), ("UI-состояния", "states.html"), ("easings.net", "https://easings.net/ru")],
}

# ---------------------------------------------------------------- Доступность
A11Y_HEAD = """
  <style>
    .focus-demo { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-top: 16px; }
    .focus-demo > div { background: var(--tile); border-radius: 16px; padding: 20px; display: flex; flex-direction: column; gap: 12px; align-items: flex-start; }
    .focus-demo small { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }
    .focus-demo button { border: 0; cursor: pointer; padding: 10px 18px; border-radius: 10px; background: var(--accent); color: #fff; font: 500 14px Onest, sans-serif; }
    .focus-demo .f-bad:focus { outline: none; }
    .focus-demo .f-good:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }
  </style>"""

A11Y = {
    "slug": "a11y", "folder": "design", "parent": PARENT, "page": "design",
    "h1": ("Доступность", "интерфейсов"),
    "category": "Доступность",
    "lead": "Семантика, работа с клавиатуры, фокус, aria-атрибуты, формы и проверка — чтобы сайтом мог пользоваться каждый.",
    "facts": ["7 уроков", "~15 минут", "WCAG 2.2"],
    "icon": "A11y", "color": "link",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(150, 240, 200, .45) 0%, transparent 60%), linear-gradient(135deg, #0b3d2e, #13855c 55%, #2f7fd4)",
    "head_extra": A11Y_HEAD,
    "sections": [
        ("why", "Для кого это", [
            "Доступность нужна не «небольшой группе людей», а почти всем — хотя бы иногда:",
            ("ul", [
                "людям с нарушениями зрения, слуха и моторики, которые пользуются экранными читалками, клавиатурой или увеличением;",
                "пожилым пользователям — мелкий серый текст им просто не прочитать;",
                "всем в «временных» ситуациях: сломанная рука, яркое солнце на экране, телефон в одной руке в транспорте.",
            ]),
            "Международный стандарт — **WCAG 2.2**. В России требования к доступности сайтов госорганов описывает ГОСТ Р 52872-2019. Бонус: доступная разметка лучше понимается поисковиками.",
        ]),
        ("semantics", "Семантика: правильные теги", [
            "Половина доступности — это просто правильные HTML-элементы. Они сами умеют фокус, клавиатуру и объясняют экранной читалке, что это такое:",
            ("code", "markup", None, r"""
<!-- ❌ не фокусируется, не нажимается с клавиатуры, читалка не знает, что это кнопка -->
<div class="button" onclick="addToCart()">В корзину</div>

<!-- ✅ всё работает само -->
<button type="button" onclick="addToCart()">В корзину</button>

<!-- Ориентиры страницы: по ним читалка позволяет прыгать -->
<header>…</header>
<nav aria-label="Основное меню">…</nav>
<main>…</main>
<footer>…</footer>
"""),
            ("ul", [
                "Ссылка ведёт на другую страницу (`<a href>`), кнопка выполняет действие (`<button>`).",
                "Заголовки `h1`–`h6` идут по порядку без пропусков: по ним незрячие пользователи «листают» страницу.",
            ]),
        ]),
        ("keyboard", "Клавиатура и фокус", [
            "Всё, что можно сделать мышью, должно делаться клавишами `Tab`, `Enter`, `Space`, стрелками и `Esc`. А пользователь всегда должен видеть, где сейчас фокус. Нажмите `Tab`, чтобы перейти к кнопкам:",
            ("html", '<div class="focus-demo">'
                     '<div><small>Фокус спрятан</small><button class="f-bad" type="button">Оформить заказ</button></div>'
                     '<div><small>Фокус виден</small><button class="f-good" type="button">Оформить заказ</button></div>'
                     "</div>"),
            ("code", "css", None, r"""
/* Никогда так не делайте */
*:focus { outline: none; }

/* Фокус только при работе с клавиатуры, а не при клике мышью */
:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}
"""),
            ("ul", [
                "Порядок `Tab` совпадает с визуальным порядком. Не используйте `tabindex` больше нуля.",
                "Модальное окно держит фокус внутри себя и закрывается по `Esc`; после закрытия фокус возвращается на кнопку, которая его открыла.",
                "Добавьте ссылку «Перейти к содержимому» первой на странице — чтобы не проходить всё меню на каждой странице.",
            ]),
        ]),
        ("aria", "ARIA-атрибуты", [
            "**Первое правило ARIA:** не используйте ARIA, если есть подходящий HTML-элемент. ARIA только описывает элемент для читалки, но не добавляет ему поведения.",
            ("code", "markup", None, r"""
<!-- Кнопка-иконка без текста: читалке нужно имя -->
<button type="button" aria-label="Добавить в избранное">♥</button>

<!-- Раскрывающееся меню: состояние открыто/закрыто -->
<button type="button" aria-expanded="false" aria-controls="filters">Фильтры</button>
<div id="filters" hidden>…</div>

<!-- Текущая страница в меню -->
<a href="/design.html" aria-current="page">Дизайн</a>

<!-- Уведомления, которые читалка произнесёт сама -->
<div role="status" aria-live="polite">Товар добавлен в корзину</div>
"""),
        ]),
        ("forms", "Формы", [
            ("code", "markup", None, r"""
<label for="phone">Телефон</label>
<input id="phone" type="tel" autocomplete="tel"
       aria-invalid="true" aria-describedby="phone-error">
<p id="phone-error">Введите 11 цифр, например 8 914 123-45-67</p>
"""),
            ("ul", [
                "У каждого поля есть видимая подпись `<label>`. Плейсхолдер — не подпись: он исчезает при вводе.",
                "Ошибка написана текстом рядом с полем и связана с ним через `aria-describedby`.",
                "`autocomplete` позволяет браузеру подставить имя, телефон и адрес — это удобно всем.",
                "Не ограничивайте время на заполнение формы без возможности продлить.",
            ]),
        ]),
        ("media", "Изображения и медиа", [
            ("ul", [
                "У информативной картинки — `alt` с её смыслом: `alt=\"Масляный фильтр, вид сбоку\"`.",
                "У декоративной — пустой `alt=\"\"`, чтобы читалка её пропустила.",
                "Иконки рядом с текстом скрывайте от читалки: `aria-hidden=\"true\"`.",
                "У видео — субтитры, у аудио — расшифровка.",
                "Ничего не мигает чаще трёх раз в секунду.",
            ]),
        ]),
        ("check", "Как проверить", [
            ("ul", [
                "**Без мыши.** Пройдите главный сценарий только клавиатурой: найти товар, добавить в корзину, оформить.",
                "**Увеличение 200%.** Ничего не должно обрезаться и наезжать.",
                "**Lighthouse и axe DevTools** — автоматически находят примерно треть проблем: контраст, подписи, alt.",
                "**Экранная читалка.** NVDA на Windows, VoiceOver на macOS и iPhone, TalkBack на Android — послушайте свой сайт хотя бы пять минут.",
            ]),
            ("tiles", [
                "Правильные HTML-теги — половина доступности.",
                "Фокус всегда виден.",
                "У полей видимые подписи и понятные ошибки.",
                "Контраст текста не меньше 4,5 : 1.",
            ], [
                "`outline: none` без замены.",
                "`div` и `span` вместо кнопок и ссылок.",
                "Кнопка-иконка без `aria-label`.",
                "Плейсхолдер вместо подписи поля.",
            ]),
        ]),
    ],
    "next": "Пройдите свой сайт только с клавиатуры и запустите Lighthouse. Исправленные проблемы доступности — сильный аргумент на собеседовании.",
    "links": [("UI-состояния", "states.html"), ("Законы дизайна", "laws.html"), ("WCAG 2.2: краткий справочник", "https://www.w3.org/WAI/WCAG22/quickref/")],
}

# ---------------------------------------------------------------- UI-состояния
STATES_HEAD = """
  <style>
    .st-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; margin-top: 16px; }
    .st-grid > div { background: var(--tile); border-radius: 14px; padding: 16px; display: flex; flex-direction: column; align-items: center; gap: 10px; }
    .st-grid small { font-size: 12px; color: var(--muted); }
    .sb { border: 0; padding: 10px 18px; border-radius: 10px; font: 500 14px Onest, sans-serif; color: #fff; background: #5b4cf0; display: inline-flex; align-items: center; gap: 8px; }
    .sb.hover { background: #4a3bd6; }
    .sb.active { background: #3d30b8; transform: scale(.96); }
    .sb.focus { outline: 3px solid #8f83ff; outline-offset: 3px; }
    .sb.disabled { background: #c9cbd2; color: #f4f4f6; }
    .sb .spin { width: 14px; height: 14px; border-radius: 50%; border: 2px solid rgba(255, 255, 255, .4); border-top-color: #fff; animation: spin .8s linear infinite; }
    @keyframes spin { to { transform: rotate(1turn); } }
    .fi { width: 100%; display: flex; flex-direction: column; gap: 4px; font-size: 12px; text-align: left; }
    .fi span { color: var(--muted); }
    .fi div { border: 1.5px solid var(--line); background: var(--bg); border-radius: 10px; padding: 9px 12px; font-size: 14px; color: var(--muted); }
    .fi.focus div { border-color: var(--accent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 25%, transparent); color: var(--text); }
    .fi.filled div { color: var(--text); }
    .fi.error div { border-color: #e0482b; color: var(--text); }
    .fi.error em { color: #e0482b; font-style: normal; }
    .fi.disabled div { background: var(--tile); opacity: .6; }
    .skel { margin-top: 16px; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; }
    .skel > div { background: var(--tile); border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 10px; }
    .skel i { display: block; border-radius: 8px; height: 12px; background: linear-gradient(90deg, var(--line) 25%, var(--bg) 50%, var(--line) 75%); background-size: 200% 100%; animation: shimmer 1.4s infinite linear; }
    .skel i.img { height: 110px; border-radius: 12px; }
    @keyframes shimmer { from { background-position: 200% 0; } to { background-position: -200% 0; } }
    .empty { margin-top: 16px; background: var(--tile); border-radius: 18px; padding: 32px 24px; text-align: center; }
    .empty .ico { font-size: 40px; }
    .empty b { display: block; font-size: 18px; margin-top: 8px; color: var(--text); }
    .lesson .empty p { margin: 6px auto 16px; max-width: 360px; }
    .empty a { display: inline-block; padding: 10px 20px; border-radius: 999px; background: var(--accent); color: #fff; font-weight: 500; }
    .errs { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-top: 16px; }
    .errs > div { background: var(--tile); border-radius: 16px; padding: 18px; font-size: 15px; color: var(--text); }
    .errs small { display: block; font-size: 12px; text-transform: uppercase; letter-spacing: .08em; margin-bottom: 8px; }
    @media (prefers-reduced-motion: reduce) { .skel i, .sb .spin { animation: none; } }
  </style>"""

STATES = {
    "slug": "states", "folder": "design", "parent": PARENT, "page": "design",
    "h1": ("UI-состояния", "компонентов"),
    "category": "Компоненты",
    "lead": "Наведение, нажатие, фокус, загрузка, ошибка, пустой экран и успех — все состояния, которые макет обычно забывает.",
    "facts": ["7 уроков", "~15 минут", "CSS"],
    "icon": "UI", "color": "react",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(97, 218, 251, .45) 0%, transparent 60%), linear-gradient(135deg, #0f131a, #1a2230 55%, #2f4a6e)",
    "head_extra": STATES_HEAD,
    "sections": [
        ("map", "Какие бывают состояния", [
            "Макет обычно показывает один «идеальный» экран. А в реальности у каждого компонента и экрана есть ещё десяток состояний:",
            ("ul", [
                "**Элемента:** обычное, наведение, нажатие, фокус, неактивное, загрузка, выбранное.",
                "**Данных:** загрузка, пусто, ошибка, частично загружено, успех.",
                "**Поля ввода:** пустое, в фокусе, заполненное, с ошибкой, неактивное.",
            ]),
            "Перед сдачей задачи пройдитесь по этому списку — забытые состояния это и есть самые частые баги интерфейса.",
        ]),
        ("buttons", "Состояния кнопки", [
            ("html", '<div class="st-grid">'
                     '<div><span class="sb">Купить</span><small>Обычная</small></div>'
                     '<div><span class="sb hover">Купить</span><small>Наведение</small></div>'
                     '<div><span class="sb active">Купить</span><small>Нажатие</small></div>'
                     '<div><span class="sb focus">Купить</span><small>Фокус с клавиатуры</small></div>'
                     '<div><span class="sb disabled">Купить</span><small>Неактивна</small></div>'
                     '<div><span class="sb"><i class="spin"></i>Оплата…</span><small>Загрузка</small></div>'
                     "</div>"),
            ("code", "css", None, r"""
.button { background: var(--accent); transition: background .15s, transform .1s; }
.button:hover { background: var(--accent-hover); }
.button:active { transform: scale(.96); }
.button:focus-visible { outline: 3px solid var(--accent-soft); outline-offset: 3px; }
.button:disabled { background: var(--disabled); cursor: not-allowed; }
.button[aria-busy="true"] { pointer-events: none; }   /* защита от двойного нажатия */
"""),
            "Кнопка «Оплатить» в состоянии загрузки должна блокироваться — иначе нетерпеливый пользователь заплатит дважды.",
        ]),
        ("inputs", "Состояния поля ввода", [
            ("html", '<div class="st-grid">'
                     '<div class="fi"><span>Телефон</span><div>+7 ___ ___-__-__</div></div>'
                     '<div class="fi focus"><span>Телефон</span><div>+7 914 |</div></div>'
                     '<div class="fi filled"><span>Телефон</span><div>+7 914 123-45-67</div></div>'
                     '<div class="fi error"><span>Телефон</span><div>+7 914 12</div><em>Не хватает 5 цифр</em></div>'
                     '<div class="fi disabled"><span>Телефон</span><div>+7 914 123-45-67</div></div>'
                     "</div>"),
            ("code", "css", None, r"""
.input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }

/* Ошибка показывается после того, как пользователь взаимодействовал с полем,
   а не сразу при открытии формы */
.input:user-invalid,
.input[aria-invalid="true"] { border-color: var(--error); }
"""),
            "Проверяйте поле, когда пользователь закончил ввод (при уходе с поля), а не на каждую букву. И не показывайте ошибки у пустой формы, которую ещё не начали заполнять.",
        ]),
        ("loading", "Загрузка", [
            ("ul", [
                "**До 1 секунды** — ничего не показывайте, индикатор только мелькнёт.",
                "**1–10 секунд** — скелетон (контур будущего содержимого) или спиннер.",
                "**Дольше 10 секунд** — прогресс-бар и объяснение, что происходит.",
            ]),
            "Скелетон лучше спиннера: страница не прыгает, когда данные приходят, и ожидание кажется короче.",
            ("html", '<div class="skel">'
                     '<div><i class="img"></i><i style="width: 80%"></i><i style="width: 50%"></i></div>'
                     '<div><i class="img"></i><i style="width: 70%"></i><i style="width: 40%"></i></div>'
                     "</div>"),
            "**Оптимистичный интерфейс** — показывать результат сразу, не дожидаясь сервера: лайк закрашивается мгновенно, а если запрос не прошёл — откатывается с сообщением.",
        ]),
        ("empty", "Пустые состояния", [
            "Пустой экран — не повод показать пустоту. Он объясняет, почему пусто, и предлагает следующий шаг:",
            ("html", '<div class="empty"><div class="ico">🛒</div><b>В корзине пока пусто</b>'
                     '<p>Найдите запчасть по марке автомобиля или артикулу — доставим завтра.</p><a href="#empty">Перейти в каталог</a></div>'),
            ("ul", [
                "**Первый запуск:** «Здесь будут ваши заказы» + кнопка, как сделать первый.",
                "**Ничего не найдено:** покажите, что искали, и предложите изменить фильтры.",
                "**Всё сделано:** «Все уведомления прочитаны» — это тоже приятное пустое состояние.",
            ]),
        ]),
        ("errors", "Ошибки", [
            "Хорошее сообщение об ошибке отвечает на три вопроса: **что случилось, почему и что делать**.",
            ("html", '<div class="errs">'
                     '<div><small style="color: #e0692b">Плохо</small>Ошибка 500. Что-то пошло не так.</div>'
                     '<div><small style="color: #22b07d">Хорошо</small>Не удалось оформить заказ: сервер оплаты не отвечает. Деньги не списаны. Попробуйте ещё раз через минуту.</div>'
                     "</div>"),
            ("ul", [
                "Ошибка поля — рядом с полем. Ошибка действия — уведомлением. Ошибка страницы — на самой странице с кнопкой «Повторить».",
                "Сохраняйте введённые данные: после ошибки пользователь не должен заполнять форму заново.",
                "Не обвиняйте пользователя: «Неверный формат» → «Введите дату в формате 01.12.2026».",
            ]),
        ]),
        ("success", "Успех и подтверждение", [
            ("ul", [
                "После важного действия подтвердите результат: «Заказ №1001 оформлен, доставим завтра с 10 до 14».",
                "Для обратимых действий вместо «Вы уверены?» лучше уведомление с кнопкой «Отменить» — это быстрее и не раздражает.",
                "Подтверждение «Вы уверены?» оставьте для необратимого: удаление аккаунта, оплата.",
            ]),
            ("tiles", [
                "У каждого компонента — все состояния, а не одно.",
                "Фокус виден, загрузка блокирует повторное нажатие.",
                "Пустой экран предлагает следующий шаг.",
                "Ошибка: что случилось, почему, что делать.",
            ], [
                "Ошибки у формы, которую ещё не начали заполнять.",
                "Спиннер на полсекунды, который просто мигает.",
                "«Что-то пошло не так» без объяснений.",
                "Потеря введённых данных после ошибки.",
            ]),
        ]),
    ],
    "next": "Откройте любой экран своего проекта и проверьте: что увидит пользователь при медленном интернете, пустом списке и ошибке сервера?",
    "links": [("Доступность", "a11y.html"), ("Анимации", "motion.html"), ("Переключатель стилей", "switcher.html")],
}

# ---------------------------------------------------------------- Дизайн-токены
TOKENS_HEAD = """
  <style>
    .tok { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; margin-top: 16px; }
    .tok > div { border: 1px solid var(--line); border-radius: 14px; overflow: hidden; font: 12px "JetBrains Mono", monospace; }
    .tok > div > span { display: block; height: 56px; }
    .tok > div > code { display: block; padding: 8px 10px; color: var(--text); background: none; }
    .levels { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 16px; }
    .levels > div { background: var(--tile); border-radius: 16px; padding: 18px; font-size: 14px; color: var(--text); }
    .levels b { display: block; font-size: 16px; margin-bottom: 6px; }
    .levels code { font-size: 12px; }
    .levels span { display: block; color: var(--muted); margin-top: 6px; }
  </style>"""

tok_items = [("--bg", "фон страницы"), ("--tile", "плитки и блоки"), ("--line", "рамки"), ("--text", "основной текст"),
             ("--muted", "второстепенный текст"), ("--accent", "акцент"), ("--cta-bg", "тёмный блок")]
tok_html = '<div class="tok">' + "".join(
    f'<div><span style="background: var({n})"></span><code>{n}</code></div>' for n, _ in tok_items) + "</div>"

TOKENS = {
    "slug": "tokens", "folder": "design", "parent": PARENT, "page": "design",
    "h1": ("Дизайн-токены", "и дизайн-система"),
    "category": "Дизайн-система",
    "lead": "Что такое токены, как их называть и разделять на уровни, как через них сделать темы — на примере токенов этого сайта.",
    "facts": ["7 уроков", "~15 минут", "CSS и JSON"],
    "icon": "{ }", "color": "sql",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(255, 196, 90, .45) 0%, transparent 60%), linear-gradient(135deg, #10283a, #1d5f7a 55%, #c46f00)",
    "head_extra": TOKENS_HEAD,
    "sections": [
        ("what", "Что такое дизайн-токены", [
            "Токен — это **именованное значение** дизайна: цвет, отступ, радиус, тень, размер шрифта, длительность анимации. Вместо `#5b4cf0` в двадцати местах — одно имя `--accent`.",
            ("ul", [
                "Поменять фирменный цвет — значит поменять одну строку, а не искать его по всему проекту.",
                "Дизайнер в Figma и разработчик в коде говорят на одном языке: «здесь `space-6`, а не 23 пикселя».",
                "Темы (тёмная, брендовая, контрастная) делаются заменой значений, без правки компонентов.",
            ]),
        ]),
        ("levels", "Три уровня токенов", [
            ("html", '<div class="levels">'
                     '<div><b>1. Примитивы</b><code>--violet-500: #5b4cf0</code><span>Вся доступная палитра и шкалы. В компонентах не используются напрямую.</span></div>'
                     '<div><b>2. Семантические</b><code>--accent: var(--violet-500)</code><span>Назначение: «акцент», «фон», «текст ошибки». Именно их меняют темы.</span></div>'
                     '<div><b>3. Компонентные</b><code>--button-bg: var(--accent)</code><span>Настройки конкретного компонента. Нужны в больших системах.</span></div>'
                     "</div>"),
            ("code", "css", None, r"""
:root {
  /* 1. Примитивы */
  --violet-500: #5b4cf0;
  --violet-300: #8f83ff;
  --gray-50: #f2f3f5;

  /* 2. Семантические */
  --accent: var(--violet-500);
  --tile: var(--gray-50);

  /* 3. Компонентные */
  --button-bg: var(--accent);
  --button-radius: 999px;
}
"""),
        ]),
        ("site", "Токены этого сайта", [
            "Этот сайт построен на семантических токенах из файла `styles.css`. Переключите тему в шапке — образцы ниже перекрасятся, потому что меняются только значения токенов:",
            ("html", tok_html),
            ("code", "css", "styles.css", r"""
:root {
  --bg: #ffffff;
  --tile: #f2f3f5;
  --line: #e3e4e8;
  --text: #1a1a1f;
  --muted: #6b6f7a;
  --accent: #5b4cf0;
  --radius-xl: 32px;
  --radius-lg: 24px;
}

:root[data-theme="dark"] {
  --bg: #121214;
  --tile: #1e1f23;
  --line: #2e2f35;
  --text: #ececf0;
  --muted: #9a9ca6;
  --accent: #8f83ff;
}
"""),
        ]),
        ("naming", "Как называть токены", [
            ("ul", [
                "**По назначению, а не по значению.** `--text-muted`, а не `--gray-600`: завтра серый станет голубоватым, и имя `--gray-600` начнёт врать.",
                "**Единая схема:** категория → свойство → вариант → состояние. Например: `--color-text-muted`, `--color-button-bg-hover`, `--space-4`, `--radius-lg`.",
                "**Шкалы — числами или размерами:** `--space-1…12`, `--radius-sm/md/lg/xl`. Так понятно, что больше, а что меньше.",
                "**Без «магии»:** `--blue-for-promo-banner-2` — признак, что токен на самом деле не нужен.",
            ]),
        ]),
        ("themes", "Темы через токены", [
            "Компоненты используют только семантические токены. Тема — это просто другой набор их значений. Так же делают брендовые темы для разных клиентов:",
            ("code", "css", None, r"""
/* Тёмная тема */
:root[data-theme="dark"] { --bg: #121214; --text: #ececf0; --accent: #8f83ff; }

/* Брендовая тема для партнёра: меняем только акцент и скругления */
:root[data-brand="partner"] { --accent: #e30613; --radius-lg: 8px; }

/* Компонент о темах не знает ничего */
.button { background: var(--accent); border-radius: var(--radius-lg); color: var(--bg); }
"""),
        ]),
        ("format", "Токены в JSON и Figma", [
            "В больших командах токены хранят в JSON в формате **W3C Design Tokens** и генерируют из них CSS, код для iOS и Android. В Figma токены живут в **Variables** — их можно выгрузить и синхронизировать с кодом.",
            ("code", "json", "tokens.json", r"""
{
  "color": {
    "accent": { "$value": "#5b4cf0", "$type": "color" },
    "text":   { "$value": "#1a1a1f", "$type": "color" }
  },
  "space": {
    "4": { "$value": "16px", "$type": "dimension" }
  }
}
"""),
            "Инструменты вроде **Style Dictionary** превращают такой файл в CSS-переменные, Swift и Kotlin — источник правды один для всех платформ.",
        ]),
        ("system", "Из чего состоит дизайн-система", [
            ("ul", [
                "**Токены** — цвета, типографика, отступы, радиусы, тени, анимации.",
                "**Компоненты** — кнопки, поля, карточки, модальные окна со всеми состояниями.",
                "**Паттерны** — как из компонентов собирать формы, таблицы, пустые состояния.",
                "**Гайдлайны** — когда что использовать, тон текстов, доступность.",
                "**Документация** — витрина компонентов (например, Storybook) с примерами кода.",
            ]),
            "Посмотрите, как устроены открытые дизайн-системы: **Material Design 3** от Google, **Gravity UI** от Яндекса, **Human Interface Guidelines** от Apple.",
            ("tiles", [
                "Компоненты используют только семантические токены.",
                "Имя токена — про назначение, а не про значение.",
                "Тема = другой набор значений тех же токенов.",
                "Один источник правды для дизайна и кода.",
            ], [
                "Цвета и отступы «на глаз» прямо в компонентах.",
                "Токен `--gray-500` в стилях кнопки.",
                "Тёмная тема копированием всех стилей.",
                "Сотни токенов, которые никто не использует.",
            ]),
        ]),
    ],
    "next": "Выпишите все цвета и отступы своего проекта и сведите их к токенам. Почти всегда окажется, что 40 разных серых на самом деле — 5.",
    "links": [("Генератор палитры", "palette.html"), ("Цвет и палитры", "colors.html"), ("Gravity UI", "https://gravity-ui.com/")],
}

GUIDES = [COLORS, MOTION, A11Y, STATES, TOKENS]
