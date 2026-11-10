PARENT = ("Дизайн", "../design.html")

FONTS_HEAD = """
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=PT+Serif:wght@400;700&family=PT+Sans:wght@400;700&family=Unbounded:wght@500;700&family=Caveat:wght@600&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=PT+Serif:wght@400;700&family=PT+Sans:wght@400;700&family=Unbounded:wght@500;700&family=Caveat:wght@600&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=PT+Serif:wght@400;700&family=PT+Sans:wght@400;700&family=Unbounded:wght@500;700&family=Caveat:wght@600&display=swap"></noscript>
  <style>
    .font-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 12px; margin-top: 16px; }
    .font-card { background: var(--tile); border-radius: 16px; padding: 18px 20px; }
    .font-card span { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }
    .lesson .font-card p { font-size: 22px; line-height: 1.25; margin: 8px 0; color: var(--text); max-width: none; }
    .font-card small { color: var(--muted); font-size: 13px; }
    .pair-card h5 { font-size: 26px; line-height: 1.15; margin: 8px 0 6px; color: var(--text); font-weight: 700; }
    .lesson .pair-card p { font-size: 15px; line-height: 1.55; margin: 0 0 8px; color: var(--muted); }
    .scale-demo { margin-top: 16px; background: var(--tile); border-radius: 16px; padding: 12px 20px; overflow: hidden; }
    .scale-demo div { display: flex; align-items: baseline; gap: 16px; padding: 4px 0; border-bottom: 1px solid var(--line); white-space: nowrap; color: var(--text); line-height: 1.2; }
    .scale-demo div:last-child { border-bottom: 0; }
    .scale-demo code { width: 72px; flex: none; color: var(--muted); font-size: 12px; }
    .hier-demo { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-top: 16px; }
    .hier-demo > div { background: var(--tile); border-radius: 16px; padding: 20px; color: var(--text); }
    .hier-demo .tag { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .08em; }
    .hier-demo .bad * { font-size: 15px !important; font-weight: 400 !important; color: var(--text) !important; text-transform: none !important; letter-spacing: 0 !important; margin: 0 !important; }
  </style>"""

LAWS_HEAD = """
  <style>
    .law-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 16px; }
    .law-fig { margin: 0; background: var(--tile); border-radius: 16px; padding: 20px; display: flex; flex-direction: column; align-items: center; gap: 14px; }
    .law-fig figcaption { font-size: 13px; color: var(--muted); text-align: center; }
    .dots { display: grid; grid-template-columns: repeat(6, 14px); gap: 10px; }
    .dots i { width: 14px; height: 14px; border-radius: 50%; background: var(--muted); display: block; }
    .dots.grouped { display: flex; gap: 26px; }
    .dots.grouped > div { display: grid; grid-template-columns: repeat(2, 14px); gap: 6px; }
    .dots i.acc { background: var(--accent); border-radius: 3px; }
    .dots.region { display: flex; gap: 10px; }
    .dots.region > div { display: grid; grid-template-columns: repeat(2, 14px); gap: 8px; padding: 8px; border-radius: 10px; }
    .dots.region > div:first-child { background: color-mix(in srgb, var(--accent) 18%, transparent); }
    .hier { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-top: 16px; }
    .hier > div { background: var(--tile); border-radius: 16px; padding: 20px; color: var(--text); font-size: 15px; }
    .hier .label { font-size: 12px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin-bottom: 10px; display: block; }
    .hier .good b { display: block; font-size: 22px; font-weight: 600; margin-bottom: 4px; }
    .hier .good s { text-decoration: none; display: block; color: var(--muted); margin-bottom: 14px; }
    .hier .good u { text-decoration: none; display: inline-block; padding: 8px 16px; border-radius: 999px; background: var(--accent); color: #fff; font-weight: 500; }
    .hier .bad b, .hier .bad s, .hier .bad u { font-weight: 400; text-decoration: none; display: block; }
    .ratio { display: flex; height: 56px; border-radius: 14px; overflow: hidden; margin-top: 16px; font-size: 13px; font-weight: 500; }
    .ratio div { display: grid; place-items: center; }
    .contrast { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 16px; }
    .contrast div { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 16px; font-size: 15px; }
    .contrast small { display: block; margin-top: 6px; font-size: 12px; color: #6b6f7a; }
    .fitts { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-top: 16px; }
    .fitts > div { background: var(--tile); border-radius: 16px; padding: 20px; display: flex; flex-direction: column; gap: 12px; }
    .fitts .label { font-size: 12px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); }
    .fitts .tiny { align-self: flex-end; font-size: 11px; padding: 2px 6px; border: 1px solid var(--line); border-radius: 4px; color: var(--muted); }
    .fitts .big { padding: 14px; border-radius: 12px; background: var(--accent); color: #fff; text-align: center; font-weight: 500; }
    .chunk { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 16px; }
    .chunk div { background: var(--tile); border-radius: 16px; padding: 20px; text-align: center; font: 500 22px/1.2 "JetBrains Mono", monospace; color: var(--text); }
    .chunk small { display: block; font: 400 13px/1.4 Onest, sans-serif; color: var(--muted); margin-top: 8px; }
  </style>"""

FONTS = {
    "slug": "fonts", "folder": "design", "parent": PARENT, "page": "design",
    "h1": ("Шрифты", "и типографика"),
    "category": "Типографика",
    "lead": "Как выбрать шрифт с кириллицей, собрать пару, настроить размеры и интервалы и правильно подключить веб-шрифты.",
    "facts": ["8 уроков", "~15 минут", "Google Fonts"],
    "icon": "Aa", "color": "css",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(255, 214, 140, .4) 0%, transparent 60%), linear-gradient(135deg, #062a36, #0b4a5a 55%, #0f766e)",
    "head_extra": FONTS_HEAD,
    "sections": [
        ("kinds", "Виды шрифтов", [
            "Шрифт задаёт тон ещё до того, как прочитан текст. Сначала определите, к какой группе он относится:",
            ("html", """<div class="font-grid">
            <div class="font-card"><span>Антиква (serif)</span><p style="font-family: 'PT Serif', serif">Съешь же ещё этих мягких французских булок</p><small>PT Serif — статьи, книги, ощущение солидности</small></div>
            <div class="font-card"><span>Гротеск (sans-serif)</span><p style="font-family: Onest, sans-serif">Съешь же ещё этих мягких французских булок</p><small>Onest — интерфейсы и лендинги, нейтрально и современно</small></div>
            <div class="font-card"><span>Моноширинный</span><p style="font-family: 'JetBrains Mono', monospace; font-size: 18px">Съешь же ещё этих мягких булок</p><small>JetBrains Mono — код, цифры в таблицах, технический стиль</small></div>
            <div class="font-card"><span>Акцидентный (display)</span><p style="font-family: Unbounded, sans-serif; font-weight: 700">Съешь же ещё этих булок</p><small>Unbounded — только для крупных заголовков</small></div>
            <div class="font-card"><span>Рукописный</span><p style="font-family: Caveat, cursive; font-size: 28px">Съешь же ещё этих мягких французских булок</p><small>Caveat — акценты и подписи, не для длинного текста</small></div>
          </div>"""),
        ]),
        ("choose", "Как выбрать шрифт", [
            ("ul", [
                "**Кириллица.** Проверяйте её первым делом: у многих красивых шрифтов её нет, и браузер подставит системный шрифт.",
                "**Начертания.** Нужны минимум три: обычное (400), среднее (500) и жирное (700). Вариативные шрифты содержат все толщины в одном файле.",
                "**Высота строчных (x-height).** Чем она больше, тем лучше читается мелкий текст в интерфейсе.",
                "**Цифры.** Для таблиц и цен нужны моноширинные цифры: `font-variant-numeric: tabular-nums`.",
                "**Лицензия.** Шрифты Google Fonts распространяются по лицензии OFL — их можно использовать в коммерческих проектах.",
            ]),
            "Хорошие бесплатные шрифты с кириллицей: **Onest, Manrope, Inter, Golos UI, PT Sans / PT Serif, Montserrat, Rubik, Unbounded, JetBrains Mono**.",
        ]),
        ("pairs", "Пары шрифтов", [
            "Правило: **не больше двух гарнитур** на сайте. Пара работает, когда шрифты контрастны по роли, а не спорят друг с другом.",
            ("html", """<div class="font-grid">
            <div class="font-card pair-card"><span>Акцидентный + гротеск</span><h5 style="font-family: Unbounded, sans-serif">Запчасти за 2 часа</h5><p style="font-family: Onest, sans-serif">Заголовок с характером, текст спокойный и читаемый. Подходит для лендингов.</p></div>
            <div class="font-card pair-card"><span>Антиква + гротеск</span><h5 style="font-family: 'PT Serif', serif">История одного заказа</h5><p style="font-family: 'PT Sans', sans-serif">Классическое сочетание для блогов и медиа: заголовок солидный, текст лёгкий.</p></div>
            <div class="font-card pair-card"><span>Одна гарнитура</span><h5 style="font-family: Onest, sans-serif; font-weight: 700">Личный кабинет</h5><p style="font-family: Onest, sans-serif">Самый надёжный вариант: контраст создают толщина и размер, а не разные шрифты.</p></div>
          </div>"""),
        ]),
        ("scale", "Размеры и модульная шкала", [
            "Размеры не подбирают на глаз, а берут из **шкалы**: базовый размер умножают на постоянный коэффициент. Ниже — шкала 16 px × 1,25:",
            ("html", """<div class="scale-demo">
            <div><code>49 px</code><span style="font-size: 49px; font-weight: 600">Заголовок</span></div>
            <div><code>39 px</code><span style="font-size: 39px; font-weight: 600">Заголовок</span></div>
            <div><code>31 px</code><span style="font-size: 31px; font-weight: 600">Заголовок раздела</span></div>
            <div><code>25 px</code><span style="font-size: 25px; font-weight: 500">Подзаголовок</span></div>
            <div><code>20 px</code><span style="font-size: 20px; font-weight: 500">Крупный текст</span></div>
            <div><code>16 px</code><span style="font-size: 16px">Основной текст интерфейса</span></div>
            <div><code>13 px</code><span style="font-size: 13px">Подписи и метаданные</span></div>
          </div>"""),
            ("code", "css", "styles.css", r"""
:root {
  --text-sm: 0.8rem;                              /* 13px */
  --text-base: 1rem;                              /* 16px */
  --text-lg: 1.25rem;                             /* 20px */
  --text-xl: 1.563rem;                            /* 25px */
  --text-2xl: clamp(1.75rem, 1.2rem + 2vw, 2.44rem); /* 28–39px: растёт с шириной экрана */
}
"""),
            "Основной текст на сайте — **16–18 px**, меньше 14 px не опускайтесь. `clamp()` делает заголовки «резиновыми» без медиазапросов.",
        ]),
        ("spacing", "Интерлиньяж, длина строки и трекинг", [
            ("ul", [
                "**Межстрочный интервал** (`line-height`): 1,5–1,7 для текста, 1,1–1,25 для крупных заголовков. Чем крупнее шрифт, тем плотнее строки.",
                "**Длина строки**: 45–75 знаков. Длинные строки утомляют, глаз теряет начало следующей. В CSS удобно задать `max-width: 65ch`.",
                "**Трекинг** (`letter-spacing`): крупным заголовкам — немного отрицательный (−0,02em), мелкому тексту в верхнем регистре — положительный (+0,06em).",
                "**Абзацы** разделяйте отступом, а не пустой строкой и не красной строкой.",
            ]),
            ("code", "css", None, r"""
body    { font-size: 1rem; line-height: 1.6; }
h1, h2  { line-height: 1.15; letter-spacing: -0.02em; }
.caps   { text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.08em; }
article { max-width: 65ch; }
"""),
        ]),
        ("hierarchy", "Типографическая иерархия", [
            "Иерархия показывает, что читать первым. Её создают **размер, толщина, цвет и регистр** — обычно хватает двух-трёх приёмов одновременно.",
            ("html", """<div class="hier-demo">
            <div class="bad"><span class="tag">Без иерархии</span><p>Заказ №1001</p><p>Фильтр масляный, 2 шт.</p><p>Доставка завтра с 10:00 до 14:00</p><p>1 780 ₽</p></div>
            <div><span class="tag">С иерархией</span><div style="font-size: 22px; font-weight: 600; margin-top: 6px">1 780 ₽</div><div style="font-weight: 500; margin-top: 2px">Фильтр масляный, 2 шт.</div><div style="color: var(--muted); font-size: 14px; margin-top: 8px">Заказ №1001 · доставка завтра с 10:00 до 14:00</div></div>
          </div>"""),
            "Проверка: прищурьтесь и посмотрите на экран. Самое важное должно оставаться заметным, даже когда текст не читается.",
        ]),
        ("loading", "Подключение веб-шрифтов", [
            "Проще всего подключить шрифт из Google Fonts. `display=swap` показывает текст сразу системным шрифтом и подменяет его, когда загрузится нужный:",
            ("code", "markup", "index.html", r"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;700&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;700&display=swap" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;700&display=swap"></noscript>
"""),
            "Для продакшена шрифт лучше хранить у себя — так быстрее и не зависит от внешнего сервиса:",
            ("code", "css", "fonts.css", r"""
@font-face {
  font-family: 'Onest';
  src: url('/fonts/onest-variable.woff2') format('woff2');
  font-weight: 100 900;     /* вариативный шрифт: все толщины в одном файле */
  font-display: swap;
}

body {
  font-family: 'Onest', system-ui, -apple-system, 'Segoe UI', sans-serif;  /* запасные шрифты */
}
"""),
        ]),
        ("rules", "Шпаргалка", [
            ("tiles", [
                "Одна-две гарнитуры на весь сайт.",
                "Размеры — из шкалы, а не «на глаз».",
                "Текст 16–18 px, интерлиньяж 1,5–1,7, строка до 75 знаков.",
                "Всегда проверяйте кириллицу и нужные начертания.",
            ], [
                "Три-четыре разных шрифта на одной странице.",
                "Декоративный или рукописный шрифт в длинном тексте.",
                "Серый текст на сером фоне — низкий контраст.",
                "Текст во всю ширину широкого экрана.",
            ]),
        ]),
    ],
    "next": "Посмотрите, как шрифты работают в разных стилях, — в галерее раздела «Дизайн» к каждому стилю подобрана своя гарнитура.",
    "links": [("Законы дизайна", "laws.html"), ("Галерея стилей", "styles.html"), ("Google Fonts с кириллицей", "https://fonts.google.com/?subset=cyrillic")],
}

LAWS = {
    "slug": "laws", "folder": "design", "parent": PARENT, "page": "design",
    "h1": ("Законы", "дизайна"),
    "category": "Основы",
    "lead": "Гештальт, иерархия, сетка, цвет и законы UX — Фиттса, Хика, Миллера и Якоба — с живыми примерами.",
    "facts": ["8 уроков", "~15 минут", "UI и UX"],
    "icon": "UX", "color": "link",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(150, 240, 200, .4) 0%, transparent 60%), linear-gradient(135deg, #10314a, #1d5fae 55%, #22b07d)",
    "head_extra": LAWS_HEAD,
    "sections": [
        ("gestalt", "Гештальт: как мы группируем", [
            "Мозг сам объединяет элементы в группы. Дизайнер управляет этим через расстояния, похожесть и общий фон.",
            ("html", """<div class="law-row">
            <figure class="law-fig"><div class="dots grouped"><div><i></i><i></i><i></i><i></i></div><div><i></i><i></i><i></i><i></i></div><div><i></i><i></i><i></i><i></i></div></div><figcaption><b>Близость.</b> Одинаковые точки, но разные расстояния — и мы видим три группы</figcaption></figure>
            <figure class="law-fig"><div class="dots"><i></i><i class="acc"></i><i></i><i class="acc"></i><i></i><i class="acc"></i><i class="acc"></i><i></i><i class="acc"></i><i></i><i class="acc"></i><i></i></div><figcaption><b>Сходство.</b> Элементы одного цвета и формы читаются как одна группа</figcaption></figure>
            <figure class="law-fig"><div class="dots region"><div><i></i><i></i><i></i><i></i></div><div><i></i><i></i><i></i><i></i></div></div><figcaption><b>Общая область.</b> Фон или рамка объединяют сильнее, чем расстояние</figcaption></figure>
          </div>"""),
            ("ul", [
                "Подпись к полю формы ставьте **ближе к своему полю**, чем к соседнему.",
                "Все ссылки на сайте — одного цвета, все кнопки одного типа — одной формы.",
                "Связанные данные (цена, количество, итог) — в одной карточке.",
            ]),
        ]),
        ("hierarchy", "Визуальная иерархия", [
            "Взгляд должен понимать, куда смотреть первым, вторым и третьим. Главное выделяют **размером, контрастом, цветом и положением**.",
            ("html", """<div class="hier">
            <div class="bad"><span class="label">Всё одинаково важно</span><b>Фильтр масляный</b><s>В наличии на складе, доставка завтра</s><b>890 ₽</b><u>Добавить в корзину</u></div>
            <div class="good"><span class="label">Есть главное</span><b>890 ₽</b><s>Фильтр масляный · в наличии, доставка завтра</s><u>В корзину</u></div>
          </div>"""),
            "На экране должно быть **одно главное действие**. Если выделено всё — не выделено ничего.",
        ]),
        ("crap", "Четыре принципа: контраст, повтор, выравнивание, близость", [
            ("ul", [
                "**Контраст.** Если элементы разные — делайте их явно разными. Чуть-чуть отличающиеся размеры выглядят как ошибка.",
                "**Повтор.** Одинаковые элементы оформлены одинаково на всех страницах: отступы, радиусы, стили кнопок.",
                "**Выравнивание.** Каждый элемент визуально связан с другим. Ничего не стоит «где-то рядом».",
                "**Близость.** Связанное — рядом, несвязанное — разнесено.",
            ]),
            "Эти четыре принципа сформулировала Робин Уильямс в книге «Дизайн для недизайнеров» — с них удобно начинать любой разбор макета.",
        ]),
        ("grid", "Сетка и отступы", [
            "Отступы берут из небольшой шкалы, кратной 4 или 8 пикселям. Тогда интерфейс выглядит аккуратно даже без дизайнера.",
            ("code", "css", "styles.css", r"""
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
}

.card    { padding: var(--space-6); gap: var(--space-3); }
.section { padding-block: var(--space-12); }
"""),
            ("ul", [
                "Внутренний отступ блока меньше, чем расстояние между блоками.",
                "Пустое пространство — не «лишнее место», а способ показать группы и дать глазу отдохнуть.",
            ]),
        ]),
        ("color", "Цвет и контраст", [
            "Правило **60-30-10**: 60% — нейтральный фон, 30% — второстепенный цвет, 10% — акцент для главных действий.",
            ("html", """<div class="ratio"><div style="flex: 60; background: #f2f3f5; color: #1a1a1f">60% фон</div><div style="flex: 30; background: #2b2b30; color: #fff">30%</div><div style="flex: 10; background: #5b4cf0; color: #fff">10%</div></div>"""),
            "Текст должен быть контрастным. Стандарт доступности **WCAG** требует отношения яркостей не меньше **4,5 : 1** для обычного текста и **3 : 1** для крупного:",
            ("html", """<div class="contrast">
            <div style="color: #999999">Серый #999 на белом<small>2,8 : 1 — не проходит</small></div>
            <div style="color: #767676">Серый #767676 на белом<small>4,5 : 1 — минимум</small></div>
            <div style="color: #1a1a1f">Почти чёрный на белом<small>17 : 1 — отлично</small></div>
          </div>"""),
            "Не передавайте смысл **только цветом**: к красной рамке ошибки добавьте текст и иконку — около 8% мужчин различают цвета хуже обычного.",
        ]),
        ("fitts", "Закон Фиттса", [
            "Чем крупнее цель и чем она ближе, тем быстрее и точнее в неё попадают. Главные кнопки делают большими и ставят там, куда уже смотрит пользователь.",
            ("html", """<div class="fitts">
            <div><span class="label">Плохо</span><span>Оформить заказ на 1 780 ₽?</span><span class="tiny">ок</span></div>
            <div><span class="label">Хорошо</span><span>Оформить заказ на 1 780 ₽?</span><span class="big">Оформить заказ</span></div>
          </div>"""),
            ("ul", [
                "Минимальный размер области нажатия на телефоне — **44 × 44 px**.",
                "Кликабельной делайте всю карточку или строку, а не только маленькую ссылку внутри.",
                "Опасные действия («Удалить») — подальше от частых («Сохранить»).",
            ]),
        ]),
        ("hick", "Законы Хика и Миллера", [
            "**Закон Хика:** время принятия решения растёт с числом вариантов. Меню из 20 пунктов, тариф из 7 вариантов, форма на 15 полей — всё это замедляет и пугает.",
            ("ul", [
                "Показывайте 3–5 главных вариантов, остальное — в «Ещё».",
                "Выделяйте рекомендуемый вариант.",
                "Разбивайте длинные формы на шаги.",
            ]),
            "**Закон Миллера:** в кратковременной памяти помещается немного — около 7 ± 2 элементов. Информацию разбивают на группы (чанки):",
            ("html", """<div class="chunk"><div>89141234567<small>трудно проверить</small></div><div>8 914 123-45-67<small>читается группами</small></div></div>"""),
        ]),
        ("jakob", "Закон Якоба и эффект эстетики", [
            "**Закон Якоба:** большую часть времени люди проводят на других сайтах и ждут, что ваш работает так же. Логотип слева ведёт на главную, корзина справа вверху, ссылки подчёркнуты или выделены цветом. Ломать привычки стоит только ради заметной выгоды.",
            "**Эффект эстетики-юзабилити:** красивый интерфейс кажется пользователям удобнее, и они прощают ему мелкие недочёты. Поэтому визуальная аккуратность — не украшение, а часть удобства.",
            ("tiles", [
                "Одно главное действие на экране.",
                "Связанное — рядом, разное — явно разное.",
                "Отступы и размеры — из шкалы.",
                "Контраст текста не меньше 4,5 : 1.",
            ], [
                "Пять кнопок одного цвета и размера.",
                "Мелкие кнопки на телефоне.",
                "Смысл, переданный только цветом.",
                "«Креативная» навигация, которую нужно изучать.",
            ]),
        ]),
    ],
    "next": "Возьмите любой экран своего проекта и разберите его по этим законам: где главное действие, как сгруппированы элементы, хватает ли контраста. Затем посмотрите, как те же принципы работают в разных стилях.",
    "links": [("Шрифты и типографика", "fonts.html"), ("Галерея стилей", "styles.html"), ("Laws of UX", "https://lawsofux.com/")],
}

GUIDES = [FONTS, LAWS]
