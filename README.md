# BezdomnyiBox.github.io

Сайт: https://bezdomnyibox.github.io

Чистые HTML, CSS и JavaScript без сборки. Всё, что запушено в `main`, через минуту появляется на сайте (GitHub Pages).

## Структура

| Файл | Что внутри |
|---|---|
| `index.html` | Главная: технологии и примеры |
| `guides.html` | Страница «Гайды» — карточки строятся из `guides-data.js` |
| `guides-data.js` | **Список гайдов и полезных ссылок** — сюда добавлять новые |
| `guides/*.html` | Учебники (например, `symfony-patterns.html`) |
| `guide.html` | Учебник по стилям сайта |
| `layout.js` | Общие шапка и подвал для всех страниц |
| `styles.css` | Общие стили и цвета светлой и тёмной темы |
| `docs.css` | Вёрстка учебников: оглавление, уроки, подсветка кода |
| `theme.js` | Переключатель темы |

## Как добавить ссылку на гайд

Откройте `guides-data.js` и допишите объект в список `LINKS` (внешние материалы) или `OWN_GUIDES` (свои учебники):

```js
{
  title: 'Название',
  description: 'О чём материал',
  url: 'https://...',
  category: 'PHP',
  icon: 'php',
  color: 'php' // php | sf | react | ts | css | link
},
```

## Как добавить свой учебник

1. Скопируйте `guides/symfony-patterns.html` в `guides/новое-имя.html` и замените содержимое.
2. Добавьте его в `OWN_GUIDES` в `guides-data.js`.

## Как посмотреть локально

```bash
python -m http.server 8000
```

Затем откройте http://localhost:8000. Открывать `index.html` двойным кликом не стоит: часть скриптов в таком режиме не загрузится.
