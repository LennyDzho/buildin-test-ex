# Кейс-задание от buildin.ai

Данный репозиторий содержит реализацию кейс-задания для компании buildin.ai. В нем предоставлена простая реализация api для создания, получения и обновления инцидентов.

Ссылка на задание: [перейти](https://buildin.ai/share/e83a7360-91b2-4dda-88d1-44166182d964?code=1N7GCX)

## Требования

### Технологии:

- Python

- Любой знакомый тебе веб-фреймворк (предпочитаем что-то из стека в вакансии: FastAPI/Flask/Django)

- Любое простое персистентное хранилище (SQLite/Postgres/MySQL и тп)

### Функциональность:

Инцидент должен иметь:

- id

- текст/описание

- статус (любой вменяемый набор, не 0/1)

- источник (например, operator / monitoring / partner)

- время создания



### Итого нужны 3 вещи:

1. **Создать инцидент**

2. **Получить список инцидентов (с фильтром по статусу)**

3. **Обновить статус инцидента по id**

Если не найден — вернуть 404.

---

## Запуск

### DockerCompose

1. Заполните файл `.env` на основе `.env.example`

```json
# App config
DEBUG=False
api_key=your_api_key_here

# Database
DB_NAME=database
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

Если хотите, чтобы подключилось к вашей локальной бд, то укажите `DB_HOST=host.docker.internal`

Также не забудьте создать базу данных в Postgres перед запуском.

2. Выполните команду в терминале из корня проекта:

```shell
docker-compose up --build
```

### Локально

1. Создайте виртуальное окружение

```shell
poetry env use python3.13
```

2. Активируйте виртуальное окружение

```shell
poetry shell
```

3. Установите зависимости

```shell
poetry install
```

4. Заполните файл `.env` на основе `.env.example`

```json
# App config
DEBUG=False
api_key=your_api_key_here

# Database
DB_NAME=database
DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```

Также не забудьте создать базу данных в Postgres перед запуском.

5. Запустите миграции

```shell
alembic upgrade head 
```

6. Запустите приложение

```shell
uvicorn src.main:app --host=0.0.0.0 --port=8000
```

---

## Использование API

### Создать инцидент (Create Incident)

- Метод: POST
- Эндпоинт: `/incidents/`

### Пример запроса

```shell
curl http://localhost:8000/api/incidents \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: YOUR_SECRET_TOKEN' \
  --data '{
  "description": "",
  "status": "new",
  "source": "operator"
}'
```

#### Тело запроса (JSON):

```json
{
    "description": "Описание инцидента",
    "status": "open",
    "source": "operator"
}
```

#### Ответ (JSON):

```json
{
  "incident": {
    "id": 1,
    "description": "string",
    "status": "new",
    "source": "operator",
    "created_at": "2025-11-10T00:35:30.167Z"
  }
}
```

### Получить список инцидентов (List Incidents)

- Метод: GET
- Эндпоинт: `/incidents/`

### Пример запроса

```shell
curl 'http://localhost:8000/api/incidents?status=' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

#### Тело запроса (JSON):

```json
{}
```

#### Ответ (JSON):

```json
{
  "incident": {
    "id": 1,
    "description": "string",
    "status": "new",
    "source": "operator",
    "created_at": "2025-11-10T00:35:30.167Z"
  }
}
```

## Обновить статус инцидента (Update Incident Status)

- Метод: PUT
- Эндпоинт: `/incidents/status`

### Пример запроса

```shell
curl http://localhost:8000/api/incidents/status \
  --request PATCH \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: your_api_key_here' \
  --data '{
  "incident_id": 1,
  "status": "in_progress"
}'
```

#### Тело запроса (JSON):

```json
{
    "incident_id": 1,
    "status": "in_progress"
}
```

#### Ответ (JSON):

```json
{
  "incident": {
    "id": 1,
    "description": "string",
    "status": "in_progress",
    "source": "operator",
    "created_at": "2025-11-10T00:35:30.167Z"
  }
}
```


