# Q&A API

Простое API для вопросов и ответов, построенное на FastAPI, SQLAlchemy и PostgreSQL. Позволяет создавать вопросы и добавлять к ним ответы с полным набором CRUD операций.

## API Endpoints

### Вопросы
- `GET /api/v1/questions/` - Список всех вопросов
- `POST /api/v1/questions/` - Создать новый вопрос
- `GET /api/v1/questions/{id}` - Получить вопрос и все ответы на него
- `DELETE /api/v1/questions/{id}` - Удалить вопрос (вместе с ответами)

### Ответы
- `POST /api/v1/questions/{question_id}/answers/` - Добавить ответ к вопросу
- `GET /api/v1/answers/{id}` - Получить конкретный ответ
- `DELETE /api/v1/answers/{id}` - Удалить ответ

## Быстрый старт

### Использование Docker (Рекомендуется)

1. Клонируйте репозиторий
    ```bash
    git clone https://github.com/leesache/Q-A-API.git
    ```
2. Запустите приложение с Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. API будет доступно по адресу `http://localhost:8000`
4. Документация API по адресу `http://localhost:8000/docs`

### Ручная настройка

1. Установите зависимости:
   ```bash
   cd src
   pip install -r requirements.txt
   ```

2. Настройте подключение к базе данных в файле `.env`:
   ```
   DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/database_name
   ```

3. Запустите миграции базы данных:
   ```bash
   cd src
   alembic upgrade head
   ```

4. Запустите приложение находясь в папке src:
   ```bash
   python -m main
   ```

## Структура проекта

```
src/
├── app/
│   ├── api_routes/         # Определения API маршрутов
│   ├── crud/               # Операции с базой данных
│   ├── db/                 # Конфигурация базы данных
│   ├── models/             # SQLAlchemy модели
│   └── schemas/            # Pydantic схемы
├── migrations/             # Миграции Alembic
├── main.py                 # Точка входа приложения
└── requirements.txt        # Python зависимости
```

## Переменные окружения

Посмотрите на файл .env.template и расположите свой .env в той же директории

- `DATABASE_URL` - Строка подключения к PostgreSQL (обязательно)
