// Список гайдов на странице guides.html.
// Чтобы добавить гайд, допишите объект в нужный список и сохраните файл.
//
//   title       — название
//   description — одна-две фразы, о чём гайд
//   url         — ссылка: свой учебник ("guides/имя.html") или внешний сайт ("https://...")
//   category    — подпись над названием (например, "PHP · Symfony")
//   icon        — текст на иконке (2–3 символа)
//   color       — цвет иконки: php | sf | react | ts | css | link

// Учебники, написанные для этого сайта
window.OWN_GUIDES = [
  {
    title: 'Паттерны проектирования в Symfony',
    description: '10 паттернов на реальных примерах: Strategy, Decorator, Observer, Adapter и другие — так, как их применяют в Symfony 7.',
    url: 'guides/symfony-patterns.html',
    category: 'PHP · Symfony',
    icon: 'sf',
    color: 'sf'
  },
  {
    title: 'Учебник по стилям',
    description: 'Как свёрстан этот сайт: токены, тёмная тема, градиенты, объёмные иконки на CSS.',
    url: 'guide.html',
    category: 'CSS',
    icon: 'css',
    color: 'css'
  }
];

// Полезные внешние материалы
window.LINKS = [
  {
    title: 'Паттерны проектирования на PHP',
    description: 'Каталог паттернов с объяснениями и примерами кода на PHP. Refactoring.Guru.',
    url: 'https://refactoring.guru/ru/design-patterns/php',
    category: 'PHP',
    icon: 'php',
    color: 'php'
  },
  {
    title: 'Документация Symfony',
    description: 'Официальная документация фреймворка: сервисы, события, Messenger, безопасность.',
    url: 'https://symfony.com/doc/current/index.html',
    category: 'Symfony',
    icon: 'sf',
    color: 'link'
  }
];
