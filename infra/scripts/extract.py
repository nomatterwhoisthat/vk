import os
import requests
import psycopg2
from datetime import datetime
from time import sleep

DSN = os.getenv("POSTGRES_DSN", "postgresql://postgres:password@db:5432/postgres")
API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")

def fetch_posts(retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(API_URL, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"[{datetime.now()}] Ошибка запроса: {e}, попытка {attempt+1}/{retries}")
            sleep(delay)
    return []

def save_posts(posts):
    if not posts:
        print(f"[{datetime.now()}] Нет данных для сохранения")
        return
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS raw_users_by_posts (
            id INT PRIMARY KEY,
            user_id INT,
            title TEXT,
            body TEXT,
            fetched_at TIMESTAMP
        )
    """)
    for post in posts:
        cur.execute("""
            INSERT INTO raw_users_by_posts (id, user_id, title, body, fetched_at)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (post['id'], post['userId'], post['title'], post['body'], datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
    print(f"[{datetime.now()}] Сохранено {len(posts)} постов")

if __name__ == "__main__":
    posts = fetch_posts()
    save_posts(posts)
