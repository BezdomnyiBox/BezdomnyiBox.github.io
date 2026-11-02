// Тема: сохранённый выбор, иначе системная настройка.
// Подключается в <head> без defer, чтобы тема применилась до отрисовки и не было вспышки.
(function () {
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem('theme'); } catch (e) {}
  var system = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  root.dataset.theme = saved || system;

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.theme-toggle')) return;
    var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
  });
})();
