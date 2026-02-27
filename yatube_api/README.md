# Yatube API

REST API для социальной сети публикаций **Yatube**

Проект реализован на Django REST Framework и предоставляет возможность:

-   создавать публикации
-   оставлять комментарии
-   подписываться на авторов
-   просматривать сообщества
-   использовать JWT-аутентификацию

После запуска проекта документация доступна по адресу:

http://127.0.0.1:8000/redoc/

------------------------------------------------------------------------

# Технологии

-   Python 3.9
-   Django 3.2
-   Django REST Framework
-   Simple JWT
-   SQLite3

------------------------------------------------------------------------

# Установка и запуск

## 1. Клонирование репозитория

    git clone <URL_вашего_репозитория>
    cd yatube_api

## 2. Создание виртуального окружения

    python3.9 -m venv venv

Активация окружения:

Linux / MacOS:

    source venv/bin/activate

Windows:

    venv\Scripts\activate

## 3. Установка зависимостей

    pip install -r requirements.txt

## 4. Применение миграций

    python manage.py migrate

## 5. Запуск сервера

    python manage.py runserver

Проект будет доступен по адресу:

http://127.0.0.1:8000/

------------------------------------------------------------------------

# Аутентификация

В проекте используется JWT-аутентификация.

## Получение токена

POST /api/v1/jwt/create/

Пример тела запроса:

    {
      "username": "string",
      "password": "string"
    }

Ответ:

    {
      "refresh": "string",
      "access": "string"
    }

## Обновление токена

POST /api/v1/jwt/refresh/

## Проверка токена

POST /api/v1/jwt/verify/

Для доступа к защищённым эндпоинтам необходимо передавать токен в
заголовке:

Authorization: Bearer `<access_token>`{=html}

------------------------------------------------------------------------

# Эндпоинты API

## Публикации

GET /api/v1/posts/
POST /api/v1/posts/\
GET /api/v1/posts/{id}/
PUT /api/v1/posts/{id}/
PATCH /api/v1/posts/{id}/
DELETE /api/v1/posts/{id}/

Поддерживается пагинация с параметрами limit и offset.

## Комментарии

GET /api/v1/posts/{post_id}/comments/
POST /api/v1/posts/{post_id}/comments/
GET /api/v1/posts/{post_id}/comments/{id}/
PUT /api/v1/posts/{post_id}/comments/{id}/
PATCH /api/v1/posts/{post_id}/comments/{id}/
DELETE /api/v1/posts/{post_id}/comments/{id}/

## Сообщества

GET /api/v1/groups/
GET /api/v1/groups/{id}/

## Подписки

GET /api/v1/follow/
POST /api/v1/follow/

Тело запроса:

    {
      "following": "username"
    }

------------------------------------------------------------------------

# Права доступа

-   Неаутентифицированные пользователи имеют доступ только для чтения
-   Создание, изменение и удаление объектов доступно только
    авторизованным пользователям
-   Редактировать и удалять публикации и комментарии может только их
    автор
-   Эндпоинт /follow/ доступен только авторизованным пользователям

------------------------------------------------------------------------

# Автор

Заикин Тимофей
