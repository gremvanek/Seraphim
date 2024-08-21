
# Seraphim

**Seraphim** — это удобное веб-приложение, предназначенное для упрощения управления проектами и задачами. Оно предоставляет интуитивно понятный интерфейс для создания, управления и отслеживания ваших задач и проектов в одном месте.

## Основные функции

- **Управление проектами:** Создавайте и управляйте несколькими проектами, каждый из которых может включать в себя множество задач.
- **Управление задачами:** Организуйте задачи внутри проектов, устанавливайте приоритеты и сроки выполнения.
- **Отслеживание прогресса:** Визуализируйте прогресс выполнения проектов и задач с помощью удобных графиков и диаграмм.
- **Интеграции:** Возможность интеграции с другими инструментами для более эффективного управления рабочим процессом.
- **Аутентификация:** Безопасная система регистрации и авторизации пользователей.

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/gremvanek/Seraphim.git
cd Seraphim
```

### 2. Установка зависимостей

Перед установкой убедитесь, что у вас установлен [Python](https://www.python.org/) версии 3.8 или выше.

```bash
pip install -r requirements.txt
```

### 3. Настройка базы данных

Создайте файл `.env` в корневой папке проекта и настройте необходимые переменные окружения, такие как параметры подключения к базе данных.

### 4. Применение миграций

```bash
alembic upgrade head
```

### 5. Запуск приложения

```bash
uvicorn main:app --reload
```

После этого приложение будет доступно по адресу `http://127.0.0.1:8000`.

## Используемые технологии

- **FastAPI** — для разработки API.
- **SQLAlchemy** — для взаимодействия с базой данных.
- **Alembic** — для управления миграциями базы данных.
- **Pydantic** — для валидации данных.
- **Jinja2** — для шаблонизации.
- **SQLite/PostgreSQL/MySQL** — поддерживаемые базы данных.

## Вклад

Мы приветствуем вклад в развитие проекта. Если у вас есть предложения, вы можете создать issue или pull request в репозитории.

## Авторы

- **gremvanek** — основной разработчик.

