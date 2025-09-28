FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y postgresql-client cron curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY scripts/ scripts/
COPY .env .env


RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y postgresql-client cron curl && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install --no-cache-dir requests psycopg2-binary python-dotenv fastapi uvicorn


CMD ["cron", "-f"]
