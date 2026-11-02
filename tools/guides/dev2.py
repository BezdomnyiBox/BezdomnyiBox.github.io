OOP = {
    "slug": "oop",
    "h1": ("ООП", "на PHP 8"),
    "category": "Основы · ООП",
    "lead": "Классы, инкапсуляция, наследование, интерфейсы, композиция, SOLID и объекты-значения — на современном PHP.",
    "facts": ["PHP 8.2+", "8 уроков", "~25 минут"],
    "icon": "ООП", "color": "php",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(224, 92, 245, .45) 0%, transparent 60%), linear-gradient(135deg, #2e3166, #4f5394 55%, #6c70b8)",
    "sections": [
        ("classes", "Класс и объект", [
            "Класс — описание: какие данные хранит объект и что он умеет делать. Объект — конкретный экземпляр класса.",
            ("code", "php", "src/Entity/Part.php", r"""
final class Part
{
    // Свойства объявлены прямо в конструкторе (constructor promotion)
    public function __construct(
        private readonly int $id,
        private string $title,
        private int $priceKopecks,
    ) {}

    public function title(): string
    {
        return $this->title;
    }

    public function rename(string $title): void
    {
        $this->title = $title;
    }
}

$filter = new Part(1, 'Фильтр масляный', 89000);
echo $filter->title();
"""),
        ]),
        ("encapsulation", "Инкапсуляция", [
            "Объект сам защищает свои правила (**инварианты**). Данные закрыты (`private`), а менять их можно только через методы, которые проверяют корректность.",
            ("code", "php", "src/Cart/Cart.php", r"""
final class Cart
{
    /** @var array<int, int> partId => количество */
    private array $items = [];

    public function add(int $partId, int $qty = 1): void
    {
        if ($qty < 1) {
            throw new \InvalidArgumentException('Количество должно быть больше нуля');
        }
        $this->items[$partId] = ($this->items[$partId] ?? 0) + $qty;
    }

    public function count(): int
    {
        return array_sum($this->items);
    }
}
"""),
            ("ul", [
                "`public` — доступно всем.",
                "`protected` — классу и его наследникам.",
                "`private` — только самому классу. По умолчанию делайте всё `private` и открывайте по необходимости.",
            ]),
        ]),
        ("inheritance", "Наследование и абстрактные классы", [
            ("code", "php", None, r"""
abstract class Notification
{
    public function __construct(protected readonly string $recipient) {}

    // Общий алгоритм для всех наследников
    public function send(): void
    {
        $this->deliver($this->render());
    }

    abstract protected function render(): string;            // каждый наследник реализует сам
    abstract protected function deliver(string $text): void;
}

final class SmsNotification extends Notification
{
    protected function render(): string
    {
        return 'Заказ готов к выдаче';
    }

    protected function deliver(string $text): void
    {
        // отправка SMS на $this->recipient
    }
}
"""),
            "Наследование выражает отношение **«является»**: SMS-уведомление является уведомлением. Если хочется унаследоваться ради пары полезных методов — это сигнал использовать композицию.",
        ]),
        ("interfaces", "Интерфейсы и полиморфизм", [
            "Интерфейс — контракт: какие методы есть у объекта, без реализации. **Полиморфизм** — код работает с любым объектом, который выполняет контракт.",
            ("code", "php", None, r"""
interface PaymentGateway
{
    public function charge(int $amountKopecks, string $orderId): string;
}

final class CardGateway implements PaymentGateway
{
    public function charge(int $amountKopecks, string $orderId): string
    {
        return 'card-tx-' . $orderId;
    }
}

final class SbpGateway implements PaymentGateway
{
    public function charge(int $amountKopecks, string $orderId): string
    {
        return 'sbp-tx-' . $orderId;
    }
}

// Сервису всё равно, какой шлюз ему передали
final class Checkout
{
    public function __construct(private readonly PaymentGateway $gateway) {}

    public function pay(Order $order): string
    {
        return $this->gateway->charge($order->totalKopecks(), $order->id());
    }
}
"""),
        ]),
        ("composition", "Композиция вместо наследования", [
            "Композиция — объект **содержит** другие объекты и делегирует им работу. Её проще менять и тестировать, чем глубокие иерархии наследования.",
            ("code", "php", None, r"""
// ❌ Наследование ради кода: разве CachedPriceList «является» PriceList?
class CachedPriceList extends PriceList { /* ... */ }

// ✅ Композиция: объект собирается из других объектов
final class PriceService
{
    public function __construct(
        private readonly PriceList $prices,
        private readonly DiscountPolicy $discounts,
    ) {}

    public function finalPrice(int $partId, Customer $customer): int
    {
        $base = $this->prices->priceOf($partId);
        return $this->discounts->apply($base, $customer);
    }
}
"""),
        ]),
        ("solid", "SOLID", [
            ("ul", [
                "**S — Single Responsibility.** У класса одна причина для изменения. `OrderService` не должен формировать PDF и отправлять письма.",
                "**O — Open/Closed.** Новое поведение добавляется новым классом, а не правкой старого (стратегии, события).",
                "**L — Liskov Substitution.** Наследник подставляется вместо родителя без сюрпризов: не бросает новых исключений и не ослабляет гарантии.",
                "**I — Interface Segregation.** Несколько маленьких интерфейсов лучше одного огромного: `Readable` и `Writable` вместо `Storage` на 20 методов.",
                "**D — Dependency Inversion.** Зависьте от абстракций: конструктор принимает `PaymentGateway`, а не `CardGateway`.",
            ]),
            "На собеседовании мало перечислить принципы — приведите пример нарушения из своего кода и расскажите, как исправили.",
        ]),
        ("modern", "Современный PHP: enum, readonly, final", [
            ("code", "php", "src/Order/OrderStatus.php", r"""
enum OrderStatus: string
{
    case New = 'new';
    case Paid = 'paid';
    case Shipped = 'shipped';

    public function label(): string
    {
        return match ($this) {
            self::New => 'Новый',
            self::Paid => 'Оплачен',
            self::Shipped => 'Отправлен',
        };
    }
}

$status = OrderStatus::from('paid');   // OrderStatus::Paid
echo $status->label();                  // «Оплачен»
"""),
            ("ul", [
                "`enum` вместо строковых констант: опечатка в статусе станет ошибкой.",
                "`readonly` — свойство нельзя изменить после конструктора.",
                "`final` — запрет наследования. Ставьте по умолчанию, снимайте осознанно.",
                "`static` — принадлежит классу, а не объекту. Подходит для фабричных методов, но статическое состояние — это глобальные переменные.",
                "**Трейты** (`trait`) копируют методы в класс. Используйте редко: это не замена композиции.",
            ]),
        ]),
        ("value", "Объекты-значения", [
            "Объект-значение (Value Object) описывает значение, а не сущность: деньги, адрес, телефон. Он **неизменяем**, проверяет себя при создании и сравнивается по содержимому.",
            ("code", "php", "src/Customer/Phone.php", r"""
final readonly class Phone
{
    public string $value;

    public function __construct(string $raw)
    {
        $digits = preg_replace('/\D+/', '', $raw);
        if (strlen($digits) !== 11) {
            throw new \InvalidArgumentException("Некорректный телефон: $raw");
        }
        $this->value = '+7' . substr($digits, 1);
    }

    public function equals(self $other): bool
    {
        return $this->value === $other->value;
    }
}

new Phone('8 (914) 123-45-67');   // +79141234567
"""),
            ("tiles", [
                "Данные закрыты, изменения — через методы с проверками.",
                "Зависимости — через конструктор и интерфейсы.",
                "Композиция по умолчанию, наследование — для отношения «является».",
                "Value Objects для денег, телефонов, адресов.",
            ], [
                "Публичные свойства, которые меняют откуда угодно.",
                "Наследование на 4+ уровня ради переиспользования кода.",
                "«Божественный» класс на 2000 строк, который делает всё.",
                "Статические хелперы с состоянием вместо сервисов.",
            ]),
        ]),
    ],
    "next": "Закрепите ООП паттернами — они показывают, как эти принципы работают в настоящем фреймворке.",
    "links": [("Паттерны в Symfony", "symfony-patterns.html"), ("Руководство PHP: классы и объекты", "https://www.php.net/manual/ru/language.oop5.php")],
}

ML = {
    "slug": "ml",
    "h1": ("Машинное обучение", "для разработчика"),
    "category": "Data · ML",
    "lead": "Как обучаются модели, первая модель на scikit-learn, метрики, переобучение, компьютерное зрение и как встроить модель в веб-сервис.",
    "facts": ["Python · scikit-learn", "8 уроков", "~25 минут"],
    "icon": "ML", "color": "ml",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(255, 170, 200, .45) 0%, transparent 60%), linear-gradient(135deg, #4a0d2c, #8c1c48 55%, #c2305f)",
    "sections": [
        ("basics", "Что такое машинное обучение", [
            "Вместо того чтобы писать правила руками, мы показываем модели примеры, и она сама находит закономерности.",
            ("ul", [
                "**Обучение с учителем** — правильные ответы известны. **Классификация** предсказывает класс (закажет снова или нет), **регрессия** — число (цена детали).",
                "**Обучение без учителя** — ответов нет, ищем структуру: сегменты клиентов, аномалии.",
                "**Признаки** (features) — входные данные модели. **Целевая переменная** (target) — то, что предсказываем.",
            ]),
        ]),
        ("data", "Данные и разбиение", [
            ("code", "python", None, r"""
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("orders.csv")
print(df.head())          # первые строки
print(df.describe())      # статистика по числовым колонкам
print(df.isna().sum())    # пропуски по колонкам

X = df[["total", "items_count", "days_since_last_order", "city"]]
y = df["will_reorder"]    # 1 — сделал повторный заказ, 0 — нет

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
"""),
            "Тестовую выборку откладывают **до** обучения и используют один раз — для честной оценки. Модель, проверенная на тех же данных, на которых училась, всегда выглядит лучше, чем есть.",
        ]),
        ("model", "Первая модель", [
            "`Pipeline` склеивает подготовку данных и модель в один объект — одинаковая обработка гарантированно применится и при обучении, и при предсказании.",
            ("code", "python", None, r"""
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

preprocess = ColumnTransformer([
    ("num", StandardScaler(), ["total", "items_count", "days_since_last_order"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["city"]),
])

model = Pipeline([
    ("prep", preprocess),
    ("clf", LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)                         # обучение
predictions = model.predict(X_test)                 # ответы: 0 или 1
probabilities = model.predict_proba(X_test)[:, 1]   # вероятность класса 1
"""),
        ]),
        ("metrics", "Метрики качества", [
            ("code", "python", None, r"""
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
"""),
            ("ul", [
                "**Accuracy** — доля верных ответов. Обманчива при дисбалансе: если повторно заказывают 5%, модель «никто не закажет» получит 95%.",
                "**Precision** — из тех, кого модель назвала «закажет», сколько действительно заказали.",
                "**Recall** — из всех, кто заказал, скольких модель нашла.",
                "**F1** — баланс precision и recall.",
                "Для регрессии: **MAE** (средняя ошибка в единицах цели) и **RMSE** (сильнее штрафует за большие ошибки).",
            ]),
        ]),
        ("overfitting", "Переобучение и кросс-валидация", [
            "**Переобучение** — модель запомнила обучающие примеры, но плохо работает на новых. Признак: высокое качество на train и заметно ниже на test.",
            ("code", "python", None, r"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

forest = Pipeline([
    ("prep", preprocess),
    ("clf", RandomForestClassifier(n_estimators=300, max_depth=8, random_state=42)),
])

scores = cross_val_score(forest, X_train, y_train, cv=5, scoring="f1")
print(scores.mean(), scores.std())   # средний F1 и разброс по 5 разбиениям
"""),
            "Кросс-валидация обучает модель 5 раз на разных частях данных, и оценка получается устойчивее, чем на одном разбиении. С переобучением борются простыми моделями, ограничением глубины, регуляризацией и бóльшим объёмом данных.",
        ]),
        ("cv", "Компьютерное зрение и нейросети", [
            "Для изображений, текста и звука используют нейросети. Обычно их не обучают с нуля, а берут **предобученную** модель и дообучают на своих данных.",
            ("code", "python", None, r"""
from ultralytics import YOLO

model = YOLO("yolov8n.pt")           # предобученная модель детекции
results = model("parts_photo.jpg")    # найти объекты на фото

for box in results[0].boxes:
    name = results[0].names[int(box.cls)]
    print(name, float(box.conf), box.xyxy.tolist())

# Дообучение на своих классах (описание датасета — в data.yaml)
model.train(data="data.yaml", epochs=50, imgsz=640)
"""),
            ("ul", [
                "**Детекция** — где на картинке объекты (рамки). **Классификация** — что изображено. **Сегментация** — точные контуры.",
                "Инструменты: **PyTorch** для своих моделей, **Ultralytics YOLO** для детекции, **OpenCV** для обработки изображений.",
            ]),
        ]),
        ("deploy", "Модель в веб-сервисе", [
            "Обученную модель сохраняют в файл и загружают в API один раз при старте.",
            ("code", "python", "train.py", r"""
import joblib

joblib.dump(model, "reorder_model.joblib")
"""),
            ("code", "python", "app/main.py", r"""
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("reorder_model.joblib")   # загружаем один раз при старте


class Customer(BaseModel):
    total: float
    items_count: int
    days_since_last_order: int
    city: str


@app.post("/predict")
def predict(customer: Customer):
    X = pd.DataFrame([customer.model_dump()])
    return {"reorder_probability": float(model.predict_proba(X)[0, 1])}
"""),
        ]),
        ("process", "Как устроен ML-проект", [
            ("ul", [
                "**Постановка:** что предсказываем и какая метрика важна бизнесу.",
                "**Данные:** сбор, очистка, пропуски, выбросы.",
                "**Бейзлайн:** простая модель или даже правило «как в прошлом месяце» — точка отсчёта.",
                "**Итерации:** признаки, модели, подбор параметров — каждый шаг сравнивается с бейзлайном.",
                "**Внедрение и мониторинг:** данные со временем меняются, качество модели нужно отслеживать.",
            ]),
            ("tiles", [
                "Тестовая выборка откладывается до обучения и используется один раз.",
                "Подготовка данных — внутри `Pipeline`.",
                "Метрика выбирается под задачу; accuracy подходит не всегда.",
                "Начинайте с простого бейзлайна.",
            ], [
                "Утечка данных: признак, который «знает» ответ (например, дата повторного заказа).",
                "Масштабирование на всех данных до разбиения на train и test.",
                "Accuracy на несбалансированных классах.",
                "Сразу нейросеть там, где хватит логистической регрессии.",
            ]),
        ]),
    ],
    "next": "Возьмите данные своего проекта — например, заказы — и попробуйте предсказать повторную покупку. Даже простая модель с честной оценкой — сильный пункт в резюме.",
    "links": [("Начало работы со scikit-learn", "https://scikit-learn.org/stable/getting_started.html"), ("Документация Ultralytics YOLO", "https://docs.ultralytics.com/")],
}

GIT = {
    "slug": "git",
    "h1": ("Git", "для командной работы"),
    "category": "Инструменты · Git",
    "lead": "Ежедневный цикл, ветки, хорошие коммиты, отмена изменений, конфликты и pull request — то, что нужно с первого дня в команде.",
    "facts": ["Git 2.40+", "7 уроков", "~15 минут"],
    "icon": "git", "color": "git",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(255, 190, 150, .45) 0%, transparent 60%), linear-gradient(135deg, #4d1409, #a12d17 55%, #e04a2b)",
    "sections": [
        ("basics", "Ежедневный цикл", [
            ("code", "bash", None, r"""
git status                     # что изменилось
git diff                       # сами изменения
git add src/Cart.php           # добавить файл в коммит (git add -p — по кусочкам)
git commit -m "feat(cart): лимит количества товара"
git pull --rebase              # забрать чужие изменения и поставить свои поверх
git push
"""),
            "Путь изменения: **рабочая папка** → `git add` → **индекс** → `git commit` → **локальный репозиторий** → `git push` → **удалённый репозиторий** (GitHub).",
        ]),
        ("branches", "Ветки", [
            ("code", "bash", None, r"""
git switch -c feature/cart-limit    # создать ветку и перейти в неё
# ... коммиты ...
git push -u origin feature/cart-limit

git switch main
git pull
git merge feature/cart-limit        # влить ветку (в команде — через pull request)
git branch -d feature/cart-limit    # удалить влитую ветку
"""),
            "Правило команды: в `main` напрямую не коммитят. Каждая задача — своя ветка и pull request.",
        ]),
        ("commits", "Хорошие коммиты", [
            ("ul", [
                "**Один коммит — одно логическое изменение.** Исправление бага и рефакторинг — разные коммиты.",
                "Сообщение отвечает на вопрос «что изменилось и зачем», а не «что я делал».",
                "Популярный формат — Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`.",
            ]),
            ("code", "bash", None, r"""
# ❌
git commit -m "fix"
git commit -m "правки"

# ✅
git commit -m "fix(checkout): не списывать остаток при отмене оплаты"
git commit -m "feat(catalog): фильтр по марке автомобиля"
"""),
        ]),
        ("undo", "Отмена изменений", [
            ("code", "bash", None, r"""
git restore src/Cart.php           # отменить правки в файле (до git add)
git restore --staged src/Cart.php  # убрать из индекса, правки останутся
git commit --amend                 # поправить последний коммит (пока он не запушен!)
git reset --soft HEAD~1            # отменить последний коммит, изменения останутся в индексе
git revert a1b2c3d                 # новый коммит, отменяющий старый, — безопасно для main
git stash                          # спрятать незакоммиченное, чтобы переключить ветку
git stash pop                      # вернуть спрятанное
"""),
            "**Главное правило:** не переписывайте историю, которую уже отправили в общую ветку (`--amend`, `reset`, `rebase`). Для отмены опубликованного есть `git revert`.",
        ]),
        ("conflicts", "Конфликты", [
            "Конфликт возникает, когда двое изменили одни и те же строки. Git останавливается и размечает оба варианта:",
            ("code", "text", "src/cart.ts", r"""
<<<<<<< HEAD
const LIMIT = 10;
=======
const LIMIT = 20;
>>>>>>> feature/cart-limit
"""),
            ("ul", [
                "Оставьте нужный вариант (или объедините оба) и удалите маркеры.",
                "`git add` файл, затем `git commit` (при merge) или `git rebase --continue` (при rebase).",
                "Чтобы конфликтов было меньше: короткие ветки, частый `git pull --rebase`, форматирование и логика — в разных коммитах.",
            ]),
        ]),
        ("pr", "Pull request и ревью", [
            ("ul", [
                "Перед PR подтяните `main`, прогоните тесты и линтер, перечитайте свой diff.",
                "В описании PR: что сделано, зачем и как проверить. Для интерфейса — скриншоты.",
                "PR на 300–400 строк ревьюят внимательно, а на 2000 строк ставят «LGTM» не глядя.",
                "Комментарии в ревью — про код, а не про человека. На замечание отвечайте исправлением или аргументом.",
            ]),
        ]),
        ("safety", "Что не должно попасть в репозиторий", [
            ("code", "ignore", ".gitignore", r"""
.env
.env.local
node_modules/
vendor/
__pycache__/
*.log
.idea/
"""),
            "Если секрет (пароль, токен, ключ) попал в коммит — **сразу смените его**. Удаление файла следующим коммитом не помогает: секрет остаётся в истории.",
            ("tiles", [
                "Ветка на задачу, pull request на ветку.",
                "Маленькие коммиты с понятным сообщением.",
                "`git pull --rebase` перед пушем.",
                "`git revert` для отмены опубликованного.",
            ], [
                "Коммит `.env` с паролями.",
                "`push --force` в общую ветку.",
                "Один гигантский коммит «сделал задачу».",
                "Сообщения вида «fix», «wip», «правки».",
            ]),
        ]),
    ],
    "next": "Заведите привычку: каждая задача — ветка, pull request и осмысленные коммиты, даже в личных проектах. Работодатели смотрят историю коммитов на GitHub.",
    "links": [("Pro Git на русском", "https://git-scm.com/book/ru/v2"), ("Conventional Commits", "https://www.conventionalcommits.org/ru/v1.0.0/")],
}

API = {
    "slug": "rest-api",
    "h1": ("HTTP и REST API", "для бэкендера"),
    "category": "Backend · API",
    "lead": "Как устроен HTTP, как проектировать ресурсы, коды ответов, формат ошибок, аутентификация и CORS — с примерами на Symfony.",
    "facts": ["HTTP · REST", "8 уроков", "~20 минут"],
    "icon": "API", "color": "link",
    "bg": "radial-gradient(50% 90% at 88% 12%, rgba(150, 240, 200, .45) 0%, transparent 60%), linear-gradient(135deg, #0b3d2e, #13855c 55%, #22b07d)",
    "sections": [
        ("http", "Запрос и ответ", [
            ("code", "http", "Запрос", r"""
POST /api/orders HTTP/1.1
Host: shop.example.ru
Content-Type: application/json
Authorization: Bearer eyJhbGciOi...

{"items": [{"partId": 42, "qty": 1}], "delivery": "courier"}
"""),
            ("code", "http", "Ответ", r"""
HTTP/1.1 201 Created
Location: /api/orders/1001
Content-Type: application/json

{"id": 1001, "status": "new", "total": 1490}
"""),
            "В запросе есть **метод**, **путь**, **заголовки** и иногда **тело**. В ответе — **код статуса**, заголовки и тело.",
        ]),
        ("methods", "Методы", [
            ("ul", [
                "`GET` — получить. Не меняет данные, можно кешировать.",
                "`POST` — создать или запустить действие.",
                "`PUT` — заменить ресурс целиком.",
                "`PATCH` — изменить часть полей.",
                "`DELETE` — удалить.",
            ]),
            "**Идемпотентность** — повтор запроса даёт тот же результат. `GET`, `PUT` и `DELETE` идемпотентны, а `POST` нет: два одинаковых `POST /orders` создадут два заказа. Поэтому для платежей передают заголовок `Idempotency-Key`, по которому сервер узнаёт повтор.",
        ]),
        ("codes", "Коды ответов", [
            ("ul", [
                "`200 OK` — успех. `201 Created` — создано (плюс заголовок `Location`). `204 No Content` — успех без тела.",
                "`400 Bad Request` — некорректный запрос. `422 Unprocessable Content` — ошибки валидации.",
                "`401 Unauthorized` — не аутентифицирован («кто вы?»). `403 Forbidden` — нет прав («знаем, кто вы, но нельзя»).",
                "`404 Not Found` — ресурса нет. `409 Conflict` — конфликт состояния (заказ уже оплачен).",
                "`429 Too Many Requests` — превышен лимит запросов.",
                "`5xx` — ошибка сервера, клиент в ней не виноват.",
            ]),
        ]),
        ("design", "Проектирование ресурсов", [
            ("code", "text", None, r"""
GET    /api/parts?brand=bosch&inStock=true&page=2&limit=20   список с фильтрами
GET    /api/parts/42                                         одна деталь
POST   /api/orders                                           создать заказ
GET    /api/orders/1001/items                                вложенный ресурс
PATCH  /api/orders/1001        {"status": "cancelled"}       изменить поле
POST   /api/orders/1001/payments                             действие как ресурс
"""),
            ("ul", [
                "Существительные во множественном числе: `/orders`, а не `/getOrders`.",
                "Фильтры, сортировка и пагинация — в query-параметрах.",
                'Списки возвращайте с метаданными: `{"data": [...], "total": 135, "page": 2}`.',
                "Версию API указывайте в пути (`/api/v1/`) или заголовке; ломающие изменения — только в новой версии.",
            ]),
        ]),
        ("symfony", "Эндпоинты на Symfony", [
            ("code", "php", "src/Controller/OrderController.php", r"""
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpKernel\Attribute\MapRequestPayload;
use Symfony\Component\Routing\Attribute\Route;
use Symfony\Component\Validator\Constraints as Assert;

final class CreateOrderRequest
{
    public function __construct(
        #[Assert\Count(min: 1)]
        public readonly array $items,
        #[Assert\Choice(['courier', 'pickup'])]
        public readonly string $delivery,
    ) {}
}

#[Route('/api/orders')]
final class OrderController extends AbstractController
{
    #[Route('', methods: ['POST'])]
    public function create(#[MapRequestPayload] CreateOrderRequest $request, CheckoutService $checkout): JsonResponse
    {
        $order = $checkout->create($request);   // невалидное тело → 422 автоматически

        return $this->json($order, Response::HTTP_CREATED, [
            'Location' => '/api/orders/' . $order->getId(),
        ]);
    }

    #[Route('/{id}', methods: ['GET'])]
    public function show(Order $order): JsonResponse   // 404, если такого заказа нет
    {
        return $this->json($order);
    }
}
"""),
            "`#[MapRequestPayload]` превращает JSON в объект и валидирует его, а сущность `Order` Symfony сам находит в базе по `{id}`.",
        ]),
        ("errors", "Формат ошибок", [
            "Клиенту нужен единый и предсказуемый формат ошибок. Стандарт — **Problem Details** (RFC 9457) с типом `application/problem+json`. Symfony с установленным Serializer отвечает на ошибки в JSON-запросах именно так:",
            ("code", "json", None, r"""
{
  "type": "https://symfony.com/errors/validation",
  "title": "Validation Failed",
  "status": 422,
  "detail": "delivery: The value you selected is not a valid choice.",
  "violations": [
    { "propertyPath": "delivery", "title": "The value you selected is not a valid choice." }
  ]
}
"""),
            ("ul", [
                "Не отдавайте наружу текст исключений и стектрейсы — это утечка информации.",
                "Один формат для всех ошибок позволяет фронтенду обрабатывать их одним кодом.",
            ]),
        ]),
        ("auth", "Аутентификация", [
            ("ul", [
                "**Сессия и cookie** — сервер хранит сессию, браузер сам отправляет cookie. Просто и безопасно для своего фронтенда на том же домене. Флаги cookie: `HttpOnly`, `Secure`, `SameSite`.",
                "**JWT** — подписанный токен с данными пользователя в заголовке `Authorization: Bearer ...`. Удобен для мобильных приложений и общения сервисов. Минус — токен сложно отозвать до истечения срока, поэтому access-токен живёт недолго, а для продления используют refresh-токен.",
                "Пароли хранят только в виде хеша (`password_hash`, bcrypt или argon2) — никогда в открытом виде.",
            ]),
        ]),
        ("cors", "CORS и безопасность", [
            "**CORS** — правило браузера: скрипт со страницы `site-a.ru` не может читать ответы API на `api-b.ru`, пока сервер явно не разрешит. Это защита пользователя, а не сервера: curl и Postman CORS не проверяют.",
            ("code", "http", None, r"""
Access-Control-Allow-Origin: https://shop.example.ru
Access-Control-Allow-Methods: GET, POST, PATCH, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
"""),
            "В Symfony CORS удобно настраивать бандлом **NelmioCorsBundle**.",
            ("tiles", [
                "Ресурс — существительное, действие — метод.",
                "Правильный код статуса важнее текста сообщения.",
                "`POST` не идемпотентен — для платежей нужен `Idempotency-Key`.",
                "Единый формат ошибок (Problem Details).",
            ], [
                '`200 OK` с `{"error": "..."}` в теле.',
                "Глаголы в URL: `/api/getOrders`, `/api/deleteOrder`.",
                "`Access-Control-Allow-Origin: *` для API с личными данными.",
                "Стектрейсы и SQL в ответах на продакшене.",
            ]),
        ]),
    ],
    "next": "Опишите API своего проекта в OpenAPI (в Symfony — NelmioApiDocBundle, в FastAPI документация генерируется сама) и проверьте, что каждый эндпоинт отвечает правильными кодами.",
    "links": [("HTTP на MDN", "https://developer.mozilla.org/ru/docs/Web/HTTP"), ("Паттерны в Symfony", "symfony-patterns.html")],
}

GUIDES = [OOP, API, GIT, ML]
