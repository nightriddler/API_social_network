# API для блога 

### Краткое описание API

Проект был написан в качестве обучения для вымышленного блога и реализовывает набор принципов которых придерживаются для написания API (REST API).
Написан на Django Rest Framework 3.12.

- Аутентификация по JWT-токену
- Работа со всеми публикациями блога `/posts/` и отдельно `/posts/{ID}/`
- Работа со списоком всех комментариев `/posts/{post_id}/comments/`и комментариев для публикации по id `/posts/{post_id}/comments/{comment_id}/`
- Работа с подпичиками `/follow/`
- Работа с группами `/group/`

### Развертка проекта
1. Клонируем репозиторий `git clone <ссылка_на_репозиторий>`
2. Устанавливаем виртуальное окружение `python -m venv venv` и активируем его `source venv/Scripts/activate`
3. Устанавливаем зависимости `pip install -r requirements.txt` и запускаем сервер `python manage.py runserver`

### Документация
В директории `/static/` доступна документация в формате Redoc.

Удобно посмотреть можно тут - https://editor.swagger.io/ (а также при запуске проекта, по адресу `http://127.0.0.1:8000/redoc/`).

![2021-07-29_20-08-48](https://user-images.githubusercontent.com/75097575/127526974-34733c16-fc43-4c9d-9b52-c8ec0a75d1fc.png)
