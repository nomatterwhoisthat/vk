# Тестовое VK

Проект собирает данные с [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts), сохраняет их в PostgreSQL, агрегирует количество постов на пользователя и отображает топ пользователей через веб-дашборд.

---

## Структура проекта

📦 `vk/`  
├─ 📁 `infra/`  
│  ├─ 📄 `docker-compose.yml`  
│  ├─ 📄 `Dockerfile`  
│  ├─ 📄 `.env`  
│  └─ 📁 `scripts/`  
│     ├─ 📄 `extract.py`  
│     ├─ 📄 `transform.py`  
│     └─ 📄 `dashboard.py`  
|     └─ 📄 `test_transform.py`
├─ 📄 `run.sh`  
└─ 📄 `Makefile`
└─ 📄 `README.md`


## Требования

- Docker и Docker Compose
- Python 3.12 (для локального запуска и тестов)
- База данных PostgreSQL (поднимается через Docker)


# Инструкция по запуску приложения

1. **Предварительно установите Docker** для вашей системы.

2. **Склонируйте репозиторий**:

   ```bash
   git clone <URL_репозитория>
   cd <название_папки_с_репозиторием>
   ```

3. **Создайте и активируйте виртуальное окружение**:

   - **Для Mac или Linux**:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

   - **Для Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. **В корне проекта выполните**:

    ```bash
    chmod +x run.sh
    ./run.sh
    ```

## Что делает скрипт?

1. Поднимает контейнеры 

2. Ждёт 10 секунд пока БД готова

3. Запускает extract.py → transform.py

4. Выводит топ пользователей в консоль и можно посмотреть результат по адресу: [http://localhost:8000/top](http://localhost:8000/top)

### Пример SQL-запроса для выборки из итоговой таблицы `top_users_by_posts`

```sql
SELECT user_id, posts_cnt, calculated_at
FROM top_users_by_posts
ORDER BY posts_cnt DESC;
```

### Запуск теста
   ```bash
   make test
   ```