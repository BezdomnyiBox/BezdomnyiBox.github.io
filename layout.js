// Общие шапка и подвал для всех страниц.
// Подключение: <script src="layout.js" data-base="" data-page="home" defer></script>
//   data-base — путь до корня сайта ("" для корня, "../" для страниц в папках guides/ и design/)
//   data-page — какой пункт меню подсветить: home | guides | design | ai
(function () {
  var script = document.currentScript;
  var base = script.dataset.base || '';
  var page = script.dataset.page || '';

  var LINKS = {
    resume: 'https://vladivostok.hh.ru/resume/4f7e2fceff09cc13af0039ed1f6261486c3437',
    telegram: 'https://t.me/BojooYkt',
    github: 'https://github.com/BezdomnyiBox',
    source: 'https://github.com/BezdomnyiBox/BezdomnyiBox.github.io'
  };

  // Счётчик посещений Яндекс Метрики (номер из metrika.yandex.ru). 0 — счётчик выключен.
  // Считаются посещения, источники переходов, карта кликов и переходы по внешним ссылкам.
  // Вебвизор (запись действий посетителя) не включён.
  var YANDEX_METRIKA = 114154700;

  function current(name) { return page === name ? ' aria-current="page"' : ''; }
  function ext(url, text, cls) {
    return '<a' + (cls ? ' class="' + cls + '"' : '') + ' href="' + url + '" target="_blank" rel="noopener">' + text + '</a>';
  }
  var logo = '<a class="logo" href="' + (base || './') + '"><i>&lt;/&gt;</i>Владимир</a>';

  var header =
    '<div class="wrap">' + logo +
      '<nav class="site-nav">' +
        '<a href="' + base + 'index.html#tech">Технологии</a>' +
        '<a href="' + base + 'guides.html"' + current('guides') + '>Гайды</a>' +
        '<a href="' + base + 'design.html"' + current('design') + '>Дизайн</a>' +
        '<a href="' + base + 'ai.html"' + current('ai') + '>AI</a>' +
        '<a href="#contact">Контакты</a>' +
      '</nav>' +
      '<div class="header-actions">' +
        '<button class="theme-toggle" type="button" aria-label="Переключить тему">' +
          '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>' +
          '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>' +
        '</button>' +
        ext(LINKS.resume, 'Резюме', 'btn-outline') +
      '</div>' +
    '</div>';

  var footer =
    '<div class="wrap">' +
      '<div class="footer-top">' + logo +
        '<div class="footer-social">' +
          ext(LINKS.telegram, 'Telegram', 'pill ghost sm') +
          ext(LINKS.resume, 'HH.ru', 'pill ghost sm') +
          ext(LINKS.github, 'GitHub', 'pill ghost sm') +
        '</div>' +
      '</div>' +
      '<div class="footer-cols">' +
        '<div><p class="footer-h">Технологии</p><ul>' +
          '<li><a href="' + base + 'index.html#tech">PHP</a></li>' +
          '<li><a href="' + base + 'index.html#tech">Symfony</a></li>' +
          '<li><a href="' + base + 'index.html#tech">React</a></li>' +
          '<li><a href="' + base + 'index.html#tech">TypeScript</a></li>' +
        '</ul></div>' +
        '<div><p class="footer-h">Гайды</p><ul>' +
          '<li><a href="' + base + 'guides.html">Все гайды</a></li>' +
          '<li><a href="' + base + 'guides/symfony-patterns.html">Паттерны в Symfony</a></li>' +
          '<li><a href="' + base + 'guides/rest-api.html">HTTP и REST API</a></li>' +
          '<li><a href="' + base + 'guides/sql.html">SQL</a></li>' +
          '<li><a href="' + base + 'guides/react.html">React</a></li>' +
        '</ul></div>' +
        '<div><p class="footer-h">Дизайн</p><ul>' +
          '<li><a href="' + base + 'design.html">Весь раздел</a></li>' +
          '<li><a href="' + base + 'design/showcase.html">Витрина из Pinterest</a></li>' +
          '<li><a href="' + base + 'design/switcher.html">Переключатель стилей</a></li>' +
          '<li><a href="' + base + 'design/styles.html">Галерея стилей</a></li>' +
          '<li><a href="' + base + 'design/palette.html">Генератор палитры</a></li>' +
          '<li><a href="' + base + 'design/fonts.html">Шрифты</a></li>' +
          '<li><a href="' + base + 'design/laws.html">Законы дизайна</a></li>' +
          '<li><a href="' + base + 'design/colors.html">Цвет и палитры</a></li>' +
        '</ul></div>' +
        '<div><p class="footer-h">AI и LLM</p><ul>' +
          '<li><a href="' + base + 'ai.html">Весь раздел</a></li>' +
          '<li><a href="' + base + 'projects/ai-assistant.html">Кейс: AI-ассистент</a></li>' +
          '<li><a href="' + base + 'ai/tool-calling.html">Вызов инструментов</a></li>' +
          '<li><a href="' + base + 'ai/llm-security.html">Безопасность LLM</a></li>' +
          '<li><a href="' + base + 'ai/symfony-ai.html">Symfony AI</a></li>' +
        '</ul></div>' +
        '<div><p class="footer-h">Обо мне</p><ul>' +
          '<li><a href="' + base + 'projects/crm.html">Проект: мини-CRM</a></li>' +
          '<li><a href="' + base + 'projects/ai-assistant.html">Проект: AI-ассистент</a></li>' +
          '<li>' + ext(LINKS.resume, 'Резюме') + '</li>' +
          '<li>' + ext(LINKS.github, 'Репозитории на GitHub') + '</li>' +
          '<li>' + ext(LINKS.source, 'Исходный код сайта') + '</li>' +
        '</ul></div>' +
      '</div>' +
      '<div class="footer-promo">' +
        '<div><h3>Ищу команду, где смогу расти<br>и приносить пользу</h3><p>Отвечу в Telegram в течение дня.</p></div>' +
        ext(LINKS.telegram, 'Написать в Telegram', 'pill') +
      '</div>' +
      '<div class="footer-bottom">' +
        '<div class="footer-contact">@BojooYkt<small>Telegram — самый быстрый способ связаться</small></div>' +
        '<p class="footer-legal">© 2026 Владимир. Сайт свёрстан вручную на HTML, CSS и чистом JavaScript, без фреймворков. Как он устроен — в <a href="' + base + 'guide.html">учебнике по стилям</a>.' +
          (YANDEX_METRIKA ? ' Посещения считает Яндекс Метрика.' : '') + '</p>' +
      '</div>' +
    '</div>';

  document.querySelector('[data-layout="header"]').innerHTML = header;
  var footerEl = document.querySelector('[data-layout="footer"]');
  footerEl.innerHTML = footer;
  // «Контакты» ведут на блок #contact, а если его на странице нет — на подвал
  if (!document.getElementById('contact')) footerEl.id = 'contact';

  // Считаем только посещения настоящего сайта, а не локального просмотра.
  // Это официальный код Метрики, разложенный по строкам: пока tag.js грузится,
  // вызовы ym() копятся в очереди, а потом скрипт их выполняет.
  if (YANDEX_METRIKA && location.hostname === 'bezdomnyibox.github.io') {
    window.ym = window.ym || function () { (window.ym.a = window.ym.a || []).push(arguments); };
    window.ym.l = Date.now();
    var counter = document.createElement('script');
    counter.async = true;
    counter.src = 'https://mc.yandex.ru/metrika/tag.js?id=' + YANDEX_METRIKA;
    document.head.appendChild(counter);
    window.ym(YANDEX_METRIKA, 'init', {
      ssr: true,
      clickmap: true,
      referrer: document.referrer,
      url: location.href,
      accurateTrackBounce: true,
      trackLinks: true
    });
  }
})();
