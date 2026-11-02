// Общие шапка и подвал для всех страниц.
// Подключение: <script src="layout.js" data-base="" data-page="home" defer></script>
//   data-base — путь до корня сайта ("" для корня, "../" для страниц в папке guides/)
//   data-page — какой пункт меню подсветить: home | guides
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
        '<div><h4>Технологии</h4><ul>' +
          '<li><a href="' + base + 'index.html#tech">PHP</a></li>' +
          '<li><a href="' + base + 'index.html#tech">Symfony</a></li>' +
          '<li><a href="' + base + 'index.html#tech">React</a></li>' +
          '<li><a href="' + base + 'index.html#tech">TypeScript</a></li>' +
        '</ul></div>' +
        '<div><h4>Гайды</h4><ul>' +
          '<li><a href="' + base + 'guides.html">Все гайды</a></li>' +
          '<li><a href="' + base + 'guides/symfony-patterns.html">Паттерны в Symfony</a></li>' +
          '<li><a href="' + base + 'guide.html">Учебник по стилям</a></li>' +
        '</ul></div>' +
        '<div><h4>Обо мне</h4><ul>' +
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
        '<p class="footer-legal">© 2026 Владимир. Сайт свёрстан вручную на HTML, CSS и чистом JavaScript, без фреймворков. Как он устроен — в <a href="' + base + 'guide.html">учебнике по стилям</a>.</p>' +
      '</div>' +
    '</div>';

  document.querySelector('[data-layout="header"]').innerHTML = header;
  var footerEl = document.querySelector('[data-layout="footer"]');
  footerEl.innerHTML = footer;
  // «Контакты» ведут на блок #contact, а если его на странице нет — на подвал
  if (!document.getElementById('contact')) footerEl.id = 'contact';
})();
