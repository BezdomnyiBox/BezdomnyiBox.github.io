// Ленивая загрузка декоративных шрифтов Google Fonts.
// Элемент с data-fonts="Unbounded:wght@500;700;900|Caveat:wght@700" подгружает свои шрифты,
// когда до него остаётся около 600px прокрутки. Из кода: window.loadFonts('Poiret One').
// Основные шрифты сайта (Onest, JetBrains Mono) подключаются в <head> как обычно.
(function () {
  var loaded = {};

  function loadFonts(spec) {
    if (!spec) return;
    var fresh = spec.split('|').map(function (f) { return f.trim(); })
      .filter(function (f) { return f && !loaded[f]; });
    if (!fresh.length) return;
    fresh.forEach(function (f) { loaded[f] = true; });
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://fonts.googleapis.com/css2?' +
      fresh.map(function (f) { return 'family=' + f.replace(/ /g, '+'); }).join('&') + '&display=swap';
    document.head.appendChild(link);
  }
  window.loadFonts = loadFonts;

  function init() {
    var els = document.querySelectorAll('[data-fonts]');
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { loadFonts(el.dataset.fonts); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        loadFonts(e.target.dataset.fonts);
        io.unobserve(e.target);
      });
    }, { rootMargin: '600px 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
