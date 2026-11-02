// Список гайдов на странице guides.html.
// Чтобы добавить гайд, допишите объект в нужный список и сохраните файл.
//
//   title       — название
//   description — одна-две фразы, о чём гайд
//   url         — ссылка: свой учебник ("guides/имя.html") или внешний сайт ("https://...")
//   category    — подпись над названием (например, "PHP · Symfony")
//   icon        — текст на иконке (2–3 символа)
//   color       — цвет иконки: php | sf | react | ts | css | docker | sql | ml | git | link

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
    title: 'ООП на PHP 8',
    description: 'Инкапсуляция, наследование, интерфейсы, композиция, SOLID и объекты-значения.',
    url: 'guides/oop.html',
    category: 'Основы',
    icon: 'ООП',
    color: 'php'
  },
  {
    title: 'HTTP и REST API',
    description: 'Методы, коды ответов, проектирование ресурсов, ошибки, аутентификация и CORS.',
    url: 'guides/rest-api.html',
    category: 'Backend',
    icon: 'API',
    color: 'link'
  },
  {
    title: 'SQL на примерах PostgreSQL',
    description: 'JOIN, GROUP BY, CTE, оконные функции, индексы и транзакции.',
    url: 'guides/sql.html',
    category: 'Базы данных',
    icon: 'SQL',
    color: 'sql'
  },
  {
    title: 'React за один вечер',
    description: 'Компоненты, состояние, эффекты, формы, контекст и свои хуки на TypeScript.',
    url: 'guides/react.html',
    category: 'Frontend',
    icon: 'Re',
    color: 'react'
  },
  {
    title: 'TypeScript без лишней теории',
    description: 'Типы, дженерики, сужение типов, утилиты и проверка данных через Zod.',
    url: 'guides/typescript.html',
    category: 'Frontend',
    icon: 'TS',
    color: 'ts'
  },
  {
    title: 'Docker для разработчика',
    description: 'Dockerfile, Compose, сети, тома и многоэтапная сборка.',
    url: 'guides/docker.html',
    category: 'DevOps',
    icon: 'Do',
    color: 'docker'
  },
  {
    title: 'Git для командной работы',
    description: 'Ветки, хорошие коммиты, отмена изменений, конфликты и pull request.',
    url: 'guides/git.html',
    category: 'Инструменты',
    icon: 'git',
    color: 'git'
  },
  {
    title: 'Машинное обучение для разработчика',
    description: 'scikit-learn, метрики, переобучение, YOLO и модель в FastAPI.',
    url: 'guides/ml.html',
    category: 'Data · ML',
    icon: 'ML',
    color: 'ml'
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
