import os
import psycopg2
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()
DSN = os.getenv("POSTGRES_DSN", "postgresql://postgres:password@db:5432/postgres")


@app.get("/top", response_class=HTMLResponse)
def get_top_users_html():
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute("SELECT * FROM top_users_by_posts ORDER BY posts_cnt DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    table = (
        "<table border='1'><tr><th>user_id</th>"
        "<th>posts_cnt</th><th>calculated_at</th></tr>"
    )
    
    for r in rows:
        table += f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>"
    table += "</table>"
    return table


@app.get("/top/json", response_class=JSONResponse)
def get_top_users_json():
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute("SELECT * FROM top_users_by_posts ORDER BY posts_cnt DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"user_id": r[0], "posts_cnt": r[1], "calculated_at": str(r[2])}
        for r in rows
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
