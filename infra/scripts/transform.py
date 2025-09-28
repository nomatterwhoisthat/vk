import os
import psycopg2
from datetime import datetime

DSN = os.getenv("POSTGRES_DSN", "postgresql://postgres:password@db:5432/postgres")

def transform():
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS top_users_by_posts (
            user_id INT PRIMARY KEY,
            posts_cnt INT,
            calculated_at TIMESTAMPTZ
        )
    """)

   
    cur.execute("SET TIME ZONE 'Europe/Moscow';")

    cur.execute("""
        INSERT INTO top_users_by_posts (user_id, posts_cnt, calculated_at)
        SELECT user_id, COUNT(*), NOW()
        FROM raw_users_by_posts
        GROUP BY user_id
        ON CONFLICT (user_id)
        DO UPDATE SET posts_cnt = EXCLUDED.posts_cnt, calculated_at = EXCLUDED.calculated_at
    """)

    conn.commit()
    cur.close()
    conn.close()
    print(f"[{datetime.now()}] Таблица top_users_by_posts обновлена (время РФ)")


if __name__ == "__main__":
    transform()
