REACT_ICON = ('<svg viewBox="-11.5 -10.2 23 20.5" fill="none" stroke="#61dafb" stroke-width="1">'
              '<circle r="2.05" fill="#61dafb" stroke="none"/><ellipse rx="11" ry="4.2"/>'
              '<ellipse rx="11" ry="4.2" transform="rotate(60)"/><ellipse rx="11" ry="4.2" transform="rotate(120)"/></svg>')

REACT = {
    "slug": "react",
    "h1": ("React", "за один вечер"),
    "category": "Frontend · React",
    "lead": "Минимум, чтобы уверенно писать компоненты: JSX, состояние, эффекты, формы, контекст и свои хуки. Примеры на TypeScript.",
    "facts": ["React 19 · TypeScript", "8 уроков", "~20 минут"],
    "icon": "Re", "icon_html": REACT_ICON, "color": "react",
    "bg": "radial-gradient(50% 90% at 85% 15%, rgba(97, 218, 251, .45) 0%, transparent 60%), linear-gradient(135deg, #0f131a, #1a2230 60%, #1f3346)",
    "sections": [
        ("components", "Компоненты и JSX", [
            "Компонент — это функция, которая принимает **props** и возвращает разметку. JSX похож на HTML, но это JavaScript: вместо `class` пишут `className`, а выражения вставляют в фигурных скобках.",
            ("code", "tsx", "src/components/PartCard.tsx", r"""
type PartCardProps = {
  title: string;
  price: number;
  inStock: boolean;
};

export function PartCard({ title, price, inStock }: PartCardProps) {
  return (
    <article className="card">
      <h3>{title}</h3>
      <p>{price.toLocaleString('ru-RU')} ₽</p>
      {inStock ? <span>В наличии</span> : <span>Под заказ</span>}
    </article>
  );
}

// Использование
<PartCard title="Фильтр масляный" price={890} inStock />
"""),
            ("ul", [
                "Имя компонента пишется с большой буквы, иначе React примет его за HTML-тег.",
                "Компонент возвращает **один** корневой элемент. Если обёртка не нужна — используйте фрагмент `<>...</>`.",
            ]),
        ]),
        ("state", "Состояние: useState", [
            "Состояние — данные, которые меняются со временем. Когда вызывается функция-сеттер, React перерисовывает компонент с новым значением.",
            ("code", "tsx", "src/components/Counter.tsx", r"""
import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(c => c + 1)}>
      В корзине: {count}
    </button>
  );
}
"""),
            "Состояние **нельзя менять напрямую**. Для массивов и объектов создавайте новую копию — иначе React не заметит изменений.",
            ("code", "tsx", None, r"""
const [items, setItems] = useState<CartItem[]>([]);

// ❌ мутация — экран не обновится
items.push(newItem);

// ✅ новый массив
setItems(prev => [...prev, newItem]);
setItems(prev => prev.filter(i => i.id !== id));
setItems(prev => prev.map(i => (i.id === id ? { ...i, qty: i.qty + 1 } : i)));
"""),
        ]),
        ("effects", "Эффекты: useEffect", [
            "`useEffect` нужен для синхронизации с внешним миром: запросы к API, подписки, таймеры. Второй аргумент — массив зависимостей: эффект перезапускается, когда меняется любая из них.",
            ("code", "tsx", "src/components/PartList.tsx", r"""
import { useEffect, useState } from 'react';

export function PartList({ query }: { query: string }) {
  const [parts, setParts] = useState<Part[]>([]);

  useEffect(() => {
    const controller = new AbortController();

    fetch(`/api/parts?q=${encodeURIComponent(query)}`, { signal: controller.signal })
      .then(res => res.json())
      .then(setParts)
      .catch(err => {
        if (err.name !== 'AbortError') console.error(err);
      });

    return () => controller.abort(); // очистка: отменяем старый запрос при смене query
  }, [query]);

  return <ul>{parts.map(p => <li key={p.id}>{p.title}</li>)}</ul>;
}
"""),
            ("ul", [
                "`[]` — эффект выполнится один раз после первой отрисовки.",
                "Без массива — после **каждой** отрисовки. Почти всегда это ошибка.",
                "Функция, которую вернул эффект, — очистка: она вызывается перед следующим запуском и при удалении компонента.",
            ]),
            "В реальных проектах загрузку данных удобнее отдать **TanStack Query**: он сам кеширует ответы, повторяет запросы и хранит статус загрузки.",
        ]),
        ("lists", "Списки и ключи", [
            "Списки рендерят через `map`. Каждому элементу нужен стабильный уникальный `key` — по нему React понимает, какой элемент изменился.",
            ("code", "tsx", None, r"""
<ul>
  {orders.map(order => (
    <li key={order.id}>
      Заказ №{order.number} — {order.status}
    </li>
  ))}
</ul>
"""),
            "Не используйте индекс массива как `key`, если список можно сортировать или удалять из него элементы: состояние «переедет» к соседним строкам.",
        ]),
        ("forms", "Формы", [
            "В **управляемом** поле значение хранится в состоянии, а `onChange` обновляет его на каждый ввод.",
            ("code", "tsx", "src/components/SearchForm.tsx", r"""
import { useState, type FormEvent } from 'react';

export function SearchForm({ onSearch }: { onSearch: (q: string) => void }) {
  const [query, setQuery] = useState('');

  function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault(); // не перезагружать страницу
    onSearch(query.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Артикул или название" />
      <button type="submit" disabled={!query.trim()}>Найти</button>
    </form>
  );
}
"""),
            "Для больших форм с валидацией берите **React Hook Form + Zod**: меньше перерисовок и вся валидация в одной схеме.",
        ]),
        ("context", "Общее состояние и контекст", [
            "Если двум компонентам нужны одни данные, состояние **поднимают** в ближайшего общего родителя и передают вниз через props. Когда props приходится пробрасывать через много уровней, используют **контекст**.",
            ("code", "tsx", "src/context/CartContext.tsx", r"""
import { createContext, useContext, useState, type ReactNode } from 'react';

type CartContextValue = { count: number; add: () => void };

const CartContext = createContext<CartContextValue | null>(null);

export function CartProvider({ children }: { children: ReactNode }) {
  const [count, setCount] = useState(0);
  return (
    <CartContext.Provider value={{ count, add: () => setCount(c => c + 1) }}>
      {children}
    </CartContext.Provider>
  );
}

export function useCart() {
  const ctx = useContext(CartContext);
  if (!ctx) throw new Error('useCart нужно вызывать внутри CartProvider');
  return ctx;
}
"""),
            "Контекст не заменяет менеджер состояния: при каждом изменении перерисуются все его потребители. Для частых обновлений есть Zustand или Redux Toolkit.",
        ]),
        ("hooks", "Свои хуки", [
            "Свой хук — функция с именем на `use`, которая собирает повторяющуюся логику из других хуков.",
            ("code", "tsx", "src/hooks/useDebounce.ts", r"""
import { useEffect, useState } from 'react';

export function useDebounce<T>(value: T, delay = 300): T {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);

  return debounced;
}

// Поиск не дёргает API на каждую букву
const debouncedQuery = useDebounce(query, 400);
"""),
            ("ul", [
                "Хуки вызываются только на верхнем уровне компонента — не внутри `if`, циклов и колбэков.",
                "Порядок вызова хуков должен быть одинаковым при каждой отрисовке.",
            ]),
        ]),
        ("tooling", "Инструменты", [
            ("code", "bash", None, r"""
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
npm run dev
"""),
            ("ul", [
                "**Vite** — сборка и dev-сервер.",
                "**React Router** — страницы и навигация.",
                "**TanStack Query** — загрузка и кеширование данных с сервера.",
                "**Tailwind CSS + shadcn/ui** — стили и готовые компоненты.",
                "**React Hook Form + Zod** — формы и валидация.",
            ]),
            ("tiles", [
                "Интерфейс — функция от состояния: меняйте данные, а не DOM.",
                "Состояние иммутабельно: новые объекты и массивы вместо мутаций.",
                "У каждого элемента списка — стабильный `key`.",
                "Эффект — только для синхронизации с внешним миром.",
            ], [
                "Забытая зависимость в массиве `useEffect` — устаревшие данные.",
                "`useEffect` для вычислений, которые можно сделать прямо при рендере.",
                "Хранить в состоянии то, что выводится из других данных (например, сумму корзины).",
                "Вызов хука внутри условия.",
            ]),
        ]),
    ],
    "next": "Соберите маленькое приложение: каталог с поиском, корзина на контексте и загрузка данных через TanStack Query. Это покрывает большую часть вопросов по React на собеседованиях.",
    "links": [("Документация React", "https://react.dev/learn"), ("Учебник по TypeScript", "typescript.html")],
}

TS = {
    "slug": "typescript",
    "h1": ("TypeScript", "без лишней теории"),
    "category": "Frontend · TypeScript",
    "lead": "Типы, которые ловят ошибки до запуска: базовые типы, интерфейсы, дженерики, сужение типов, утилиты и проверка данных с сервера.",
    "facts": ["TypeScript 5", "8 уроков", "~20 минут"],
    "icon": "TS", "color": "ts",
    "bg": "radial-gradient(50% 90% at 90% 10%, rgba(140, 200, 255, .5) 0%, transparent 60%), linear-gradient(135deg, #123a6b, #1d5fae 55%, #2f7fd4)",
    "sections": [
        ("why", "Зачем TypeScript", [
            "TypeScript — это JavaScript с типами. Компилятор проверяет код **до запуска** и подсказывает в редакторе. В браузер уходит обычный JavaScript.",
            ("code", "typescript", None, r"""
function total(price: number, qty: number): number {
  return price * qty;
}

total(890, '2'); // ❌ ошибка компиляции: string нельзя передать вместо number
"""),
            "Включайте строгий режим — без него TypeScript пропускает половину ошибок:",
            ("code", "json", "tsconfig.json", r"""
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true
  }
}
"""),
        ]),
        ("basics", "Базовые типы и вывод типов", [
            ("code", "typescript", None, r"""
let title: string = 'Фильтр';
let price = 890;              // тип number выведен автоматически
const status = 'paid';        // тип — литерал 'paid', а не просто string
let tags: string[] = ['двигатель', 'ТО'];
let point: [number, number] = [43.1, 131.9]; // кортеж

// Объединение (union): одно из нескольких значений
type OrderStatus = 'new' | 'paid' | 'shipped' | 'cancelled';
let orderStatus: OrderStatus = 'new';
orderStatus = 'lost'; // ❌ такого значения нет в типе
"""),
            "Пишите типы явно там, где их не вывести: параметры функций, публичные API, пустое состояние `useState<Part[]>([])`. В остальных местах доверяйте выводу.",
        ]),
        ("objects", "Объекты: type и interface", [
            ("code", "typescript", None, r"""
interface Part {
  readonly id: number;   // нельзя изменить после создания
  title: string;
  price: number;
  brand?: string;        // необязательное поле: string | undefined
}

type Order = {
  id: number;
  items: Part[];
  status: OrderStatus;
};

// Расширение
interface ExpressOrder extends Order {
  deliveryHours: number;
}
type PaidOrder = Order & { paidAt: Date };
"""),
            "Разница небольшая: `interface` можно расширять и дополнять, а `type` умеет объединения и сложные выражения. Частое правило — `interface` для объектов, `type` для всего остального. Главное — единообразие в проекте.",
        ]),
        ("functions", "Функции", [
            ("code", "typescript", None, r"""
// Параметр по умолчанию и необязательный параметр
function formatPrice(value: number, currency = '₽', compact?: boolean): string {
  return compact ? `${Math.round(value / 1000)}к ${currency}` : `${value} ${currency}`;
}

// Тип функции — например, для колбэка в props
type OnSelect = (partId: number) => void;

// Асинхронная функция возвращает Promise
async function fetchPart(id: number): Promise<Part> {
  const res = await fetch(`/api/parts/${id}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json() as Promise<Part>;
}
"""),
            "Обратите внимание: `as Promise<Part>` ничего не проверяет, а только **обещает** компилятору тип. Данные с сервера надёжнее проверять схемой — об этом последний урок.",
        ]),
        ("generics", "Дженерики", [
            "Дженерик — тип-параметр. Функция или тип работают с любым типом, но сохраняют связь между входом и выходом.",
            ("code", "typescript", None, r"""
function first<T>(items: T[]): T | undefined {
  return items[0];
}

const part = first(parts);      // Part | undefined
const tag = first(['a', 'b']);  // string | undefined

// Обёртка ответа API для любых данных
interface ApiResponse<T> {
  data: T;
  total: number;
  page: number;
}

async function getJson<T>(url: string): Promise<T> {
  const res = await fetch(url);
  return res.json() as Promise<T>;
}

const list = await getJson<ApiResponse<Part[]>>('/api/parts?page=1');
list.data[0]?.title; // автодополнение работает

// Ограничение: у T обязательно есть поле id
function byId<T extends { id: number }>(items: T[], id: number): T | undefined {
  return items.find(i => i.id === id);
}
"""),
        ]),
        ("narrowing", "Сужение типов", [
            "Когда у значения тип-объединение, TypeScript **сужает** его после проверок `typeof`, `in`, `instanceof` или сравнения поля.",
            ("code", "typescript", None, r"""
type Payment =
  | { method: 'card'; cardLast4: string }
  | { method: 'cash' }
  | { method: 'invoice'; inn: string };

function describe(p: Payment): string {
  switch (p.method) {
    case 'card':
      return `Карта •• ${p.cardLast4}`;   // здесь TypeScript знает про cardLast4
    case 'cash':
      return 'Наличными курьеру';
    case 'invoice':
      return `Счёт для ИНН ${p.inn}`;
    default: {
      const unreachable: never = p;      // ошибка, если забыли обработать новый вариант
      return unreachable;
    }
  }
}
"""),
            "Такой тип называется **размеченным объединением** (discriminated union): общее поле `method` говорит, какой это вариант. Ветка с `never` заставит обработать новый способ оплаты, когда его добавят.",
        ]),
        ("utility", "Утилитарные типы", [
            ("code", "typescript", None, r"""
type PartPreview = Pick<Part, 'id' | 'title'>;       // только эти поля
type NewPart = Omit<Part, 'id'>;                       // всё, кроме id
type PartPatch = Partial<Part>;                        // все поля необязательные
type StrictPart = Required<Part>;                      // все поля обязательные
type PricesByBrand = Record<string, number>;           // объект-словарь
type Status = Order['status'];                         // тип одного поля
type Loaded = Awaited<ReturnType<typeof fetchPart>>;   // Part — результат функции
"""),
            "Утилиты избавляют от копирования: тип для формы создания — это `Omit<Part, 'id'>`, а не новый интерфейс, который со временем разойдётся с оригиналом.",
        ]),
        ("unknown", "any, unknown и проверка данных", [
            ("ul", [
                "`any` выключает проверку типов — ошибки доживут до продакшена. Избегайте.",
                "`unknown` — «что-то неизвестное»: использовать можно только после проверки.",
            ]),
            "Данные из сети, `localStorage` и форм на самом деле `unknown`. Схема **Zod** проверяет их во время выполнения и сама выводит тип:",
            ("code", "typescript", None, r"""
import { z } from 'zod';

const PartSchema = z.object({
  id: z.number(),
  title: z.string().min(1),
  price: z.number().nonnegative(),
  brand: z.string().optional(),
});

type Part = z.infer<typeof PartSchema>; // тип выводится из схемы — не нужно описывать дважды

const json: unknown = await res.json();
const part = PartSchema.parse(json);    // бросит ошибку, если сервер прислал не то
"""),
            ("tiles", [
                "`strict: true` с первого дня.",
                "Типизируйте границы: параметры функций, props, ответы API.",
                "Размеченные объединения вместо пачки необязательных полей.",
                "Внешние данные — через схему (Zod), а не через `as`.",
            ], [
                "`any`, «чтобы заработало».",
                "`as` вместо проверки: тип совпадает только на бумаге.",
                "Копии типов вместо `Pick` и `Omit`.",
                "Выключенный `strict` в старом проекте «на потом».",
            ]),
        ]),
    ],
    "next": "Включите `strict` в своём проекте и избавьтесь от всех `any` — это лучшая практика по TypeScript. Затем переведите ответы API на схемы Zod.",
    "links": [("TypeScript Handbook", "https://www.typescriptlang.org/docs/handbook/intro.html"), ("Учебник по React", "react.html")],
}

DOCKER = {
    "slug": "docker",
    "h1": ("Docker", "для разработчика"),
    "category": "DevOps · Docker",
    "lead": "Образы, контейнеры, Dockerfile и Docker Compose — всё, чтобы поднять проект с базой и кешем одной командой.",
    "facts": ["Docker · Compose v2", "7 уроков", "~20 минут"],
    "icon": "Do", "color": "docker",
    "bg": "radial-gradient(50% 90% at 90% 10%, rgba(120, 210, 255, .5) 0%, transparent 60%), linear-gradient(135deg, #0b2f6b, #1d63ed 60%, #2496ed)",
    "sections": [
        ("concepts", "Образ и контейнер", [
            ("ul", [
                "**Образ** — неизменяемый шаблон: система, зависимости и код. Собирается по `Dockerfile`.",
                "**Контейнер** — запущенный экземпляр образа. Из одного образа можно запустить сколько угодно контейнеров.",
                "**Реестр** (Docker Hub) — хранилище готовых образов: `postgres:16`, `redis:7`, `nginx`.",
            ]),
            "Главная польза: у всех разработчиков и на сервере одинаковое окружение. Фраза «у меня работает» перестаёт быть проблемой.",
        ]),
        ("dockerfile", "Dockerfile", [
            "Dockerfile — рецепт сборки образа. Пример для бэкенда на FastAPI:",
            ("code", "docker", "backend/Dockerfile", r"""
FROM python:3.12-slim

WORKDIR /app

# Сначала только зависимости: этот слой кешируется и не пересобирается при правке кода
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Потом код
COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""),
            "Каждая инструкция создаёт **слой**. Docker переиспользует слои, пока их входные файлы не изменились, — поэтому редко меняющееся ставят выше, а код копируют последним.",
        ]),
        ("commands", "Основные команды", [
            ("code", "bash", None, r"""
docker build -t zapchasti-api ./backend               # собрать образ с именем
docker run -d -p 8000:8000 --name api zapchasti-api  # запустить в фоне: порт хоста:порт контейнера
docker ps                                            # запущенные контейнеры
docker logs -f api                                   # логи в реальном времени
docker exec -it api sh                               # зайти внутрь контейнера
docker stop api && docker rm api                     # остановить и удалить
docker images                                        # список образов
docker system prune                                  # удалить всё неиспользуемое
"""),
        ]),
        ("compose", "Docker Compose", [
            "Compose описывает несколько сервисов в одном файле и запускает их вместе. Типичный набор — приложение, PostgreSQL и Redis.",
            ("code", "yaml", "compose.yaml", r"""
services:
  api:
    build: ./backend
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      db:
        condition: service_healthy   # ждать, пока база действительно готова

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 5s
      retries: 5

  redis:
    image: redis:7

volumes:
  pgdata:
"""),
            ("code", "bash", None, r"""
docker compose up -d --build        # собрать и запустить всё
docker compose logs -f api          # логи одного сервиса
docker compose exec db psql -U app  # консоль базы
docker compose down                 # остановить (данные в томе сохранятся)
"""),
        ]),
        ("network", "Сети и тома", [
            ("ul", [
                "Сервисы одного Compose-файла видят друг друга **по имени**: из `api` база доступна как `db:5432`, а не `localhost`.",
                "`localhost` внутри контейнера — это сам контейнер.",
                "**Именованный том** (`pgdata`) хранит данные базы между перезапусками. `docker compose down -v` удалит и его — осторожно.",
                "**Bind mount** (`./backend:/app`) пробрасывает папку с компьютера: удобно в разработке, код обновляется без пересборки.",
            ]),
            ("code", "bash", ".env", r"""
DATABASE_URL=postgresql://app:secret@db:5432/app
REDIS_URL=redis://redis:6379/0
"""),
        ]),
        ("multistage", "Многоэтапная сборка", [
            "Фронтенду Node.js нужен только для сборки. Многоэтапный Dockerfile собирает проект в одном образе, а в итоговый кладёт лишь готовые файлы и nginx — образ получается в десятки раз меньше.",
            ("code", "docker", "frontend/Dockerfile", r"""
# Этап 1: сборка
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Этап 2: только статика и nginx
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
"""),
        ]),
        ("practice", "Хорошие практики", [
            ("code", "ignore", ".dockerignore", r"""
node_modules
.git
.env
__pycache__
dist
"""),
            ("tiles", [
                "Фиксируйте версии образов: `postgres:16`, а не `postgres:latest`.",
                "Зависимости копируйте до кода — сборка будет быстрой.",
                "Добавьте `.dockerignore`, чтобы не тащить в образ `node_modules` и `.git`.",
                "Для зависимостей между сервисами — `healthcheck` и `condition: service_healthy`.",
            ], [
                "Секреты внутри образа (`COPY .env`): их увидит любой, у кого есть образ.",
                "Обращение к базе по `localhost` из другого контейнера.",
                "`docker compose down -v` на сервере — и данные базы удалены.",
                "Порт базы (`5432:5432`), открытый наружу на продакшене.",
            ]),
        ]),
    ],
    "next": "Упакуйте свой проект в Compose: приложение, база, Redis и nginx. Если `docker compose up` поднимает всё с нуля на чистой машине — вы знаете Docker на уровне, который ждут от разработчика.",
    "links": [("Документация Docker", "https://docs.docker.com/get-started/"), ("Учебник по SQL", "sql.html")],
}

SQL = {
    "slug": "sql",
    "h1": ("SQL", "на примерах PostgreSQL"),
    "category": "Базы данных · SQL",
    "lead": "Выборки, соединения, группировки, CTE, оконные функции, индексы и транзакции — на схеме интернет-магазина.",
    "facts": ["PostgreSQL 16", "8 уроков", "~25 минут"],
    "icon": "SQL", "color": "sql",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(255, 196, 90, .45) 0%, transparent 60%), linear-gradient(135deg, #182c44, #24476b 55%, #336791)",
    "sections": [
        ("schema", "Схема для примеров", [
            ("code", "sql", "schema.sql", r"""
CREATE TABLE customers (
  id   INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT
);

CREATE TABLE orders (
  id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_id INT NOT NULL REFERENCES customers (id),
  status      TEXT NOT NULL DEFAULT 'new',
  total       NUMERIC(10, 2) NOT NULL,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE parts (
  id    INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  title TEXT NOT NULL,
  stock INT NOT NULL DEFAULT 0
);

CREATE TABLE order_items (
  order_id INT REFERENCES orders (id),
  part_id  INT REFERENCES parts (id),
  qty      INT NOT NULL,
  PRIMARY KEY (order_id, part_id)
);
"""),
            "`REFERENCES` — внешний ключ: база не даст создать заказ несуществующего клиента. `NUMERIC` — точный тип для денег; `FLOAT` для денег не используют из-за ошибок округления.",
        ]),
        ("select", "SELECT и фильтры", [
            ("code", "sql", None, r"""
SELECT id, total, created_at
FROM orders
WHERE status = 'paid'
  AND total >= 5000
  AND created_at >= now() - interval '30 days'
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;   -- третья страница по 20 штук
"""),
            ("ul", [
                "`status IN ('paid', 'shipped')` — одно из значений.",
                "`title ILIKE '%фильтр%'` — поиск по подстроке без учёта регистра.",
                "`city IS NULL` — проверка на NULL. Сравнение `= NULL` не работает никогда.",
            ]),
        ]),
        ("join", "JOIN", [
            ("code", "sql", None, r"""
-- JOIN (он же INNER JOIN): только строки, у которых нашлась пара
SELECT o.id, c.name, o.total
FROM orders o
JOIN customers c ON c.id = o.customer_id;

-- LEFT JOIN: все клиенты, даже без заказов
SELECT c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id;

-- Клиенты, которые ни разу не заказывали
SELECT c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
"""),
            "`LEFT JOIN` сохраняет все строки левой таблицы, а поля правой, для которых пары нет, заполняет `NULL`. На этом построен приём «найти записи без пары».",
        ]),
        ("group", "GROUP BY и агрегаты", [
            ("code", "sql", None, r"""
SELECT c.city,
       COUNT(*)               AS orders_count,
       SUM(o.total)           AS revenue,
       ROUND(AVG(o.total), 2) AS avg_check
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.status = 'paid'
GROUP BY c.city
HAVING SUM(o.total) > 100000   -- фильтр по агрегату
ORDER BY revenue DESC;
"""),
            "Порядок выполнения: `FROM/JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`. Поэтому в `WHERE` нельзя использовать агрегаты — для них есть `HAVING`.",
        ]),
        ("cte", "Подзапросы и CTE", [
            "CTE (`WITH`) — именованный подзапрос. Сложный запрос читается как набор шагов.",
            ("code", "sql", None, r"""
WITH customer_stats AS (
  SELECT customer_id, COUNT(*) AS orders, SUM(total) AS spent
  FROM orders
  WHERE status = 'paid'
  GROUP BY customer_id
)
SELECT c.name, s.orders, s.spent
FROM customer_stats s
JOIN customers c ON c.id = s.customer_id
WHERE s.spent > (SELECT AVG(spent) FROM customer_stats)   -- больше среднего
ORDER BY s.spent DESC;
"""),
        ]),
        ("window", "Оконные функции", [
            "Оконная функция считает значение по группе строк, но, в отличие от `GROUP BY`, **не схлопывает** строки.",
            ("code", "sql", None, r"""
-- Последний заказ каждого клиента
SELECT *
FROM (
  SELECT o.*,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY created_at DESC) AS rn
  FROM orders o
) t
WHERE rn = 1;

-- Выручка по дням и накопительный итог
SELECT created_at::date AS day,
       SUM(total) AS revenue,
       SUM(SUM(total)) OVER (ORDER BY created_at::date) AS revenue_cumulative
FROM orders
GROUP BY created_at::date
ORDER BY day;
"""),
            "Задача «последняя запись в каждой группе» — один из самых частых вопросов на собеседованиях.",
        ]),
        ("indexes", "Индексы и EXPLAIN", [
            "Индекс — отсортированная структура (обычно B-tree), по которой база находит строки без полного перебора таблицы.",
            ("code", "sql", None, r"""
CREATE INDEX idx_orders_customer ON orders (customer_id);
-- Составной индекс: подходит для WHERE status = ... ORDER BY created_at
CREATE INDEX idx_orders_status_created ON orders (status, created_at DESC);

EXPLAIN ANALYZE
SELECT * FROM orders WHERE status = 'paid' ORDER BY created_at DESC LIMIT 20;
-- Seq Scan   — полный перебор таблицы: на больших таблицах медленно
-- Index Scan — поиск по индексу: быстро
"""),
            ("ul", [
                "Индексируйте внешние ключи и поля из частых `WHERE`, `JOIN`, `ORDER BY`.",
                "Порядок полей в составном индексе важен: индекс `(status, created_at)` поможет запросу по `status`, но не запросу только по `created_at`.",
                "Индексы ускоряют чтение, но замедляют запись — не создавайте их «на всякий случай».",
            ]),
        ]),
        ("tx", "Транзакции и N+1", [
            "Транзакция выполняет несколько запросов как одно целое: применяются либо все, либо ни один (свойства **ACID**).",
            ("code", "sql", None, r"""
BEGIN;

UPDATE parts SET stock = stock - 1 WHERE id = 42 AND stock > 0;
INSERT INTO order_items (order_id, part_id, qty) VALUES (1001, 42, 1);

COMMIT;   -- или ROLLBACK, если что-то пошло не так
"""),
            "Проблема **N+1** — частая беда ORM: один запрос за списком заказов и ещё по запросу на клиента каждого заказа. Решение — загрузить связь сразу: `JOIN` в SQL, `leftJoin()->addSelect()` в Doctrine, `selectinload()` в SQLAlchemy.",
            ("tiles", [
                "Сначала `WHERE`, потом `GROUP BY`, потом `HAVING`.",
                "`LEFT JOIN ... WHERE right.id IS NULL` — поиск записей без пары.",
                "`ROW_NUMBER() OVER (PARTITION BY ...)` — топ-N в каждой группе.",
                "Медленный запрос → `EXPLAIN ANALYZE` → индекс.",
            ], [
                "Склейка SQL из строк с пользовательским вводом — SQL-инъекция. Только параметры.",
                "`= NULL` вместо `IS NULL`.",
                "`SELECT *` в коде приложения: лишние данные и поломки при изменении схемы.",
                "N+1 запросов в цикле.",
            ]),
        ]),
    ],
    "next": "Потренируйтесь на своей базе: найдите топ-3 клиентов по выручке в каждом городе (CTE + оконная функция) и ускорьте индексом самый медленный запрос проекта.",
    "links": [("Документация PostgreSQL", "https://www.postgresql.org/docs/current/"), ("Учебник по Docker", "docker.html")],
}

GUIDES = [REACT, TS, DOCKER, SQL]
