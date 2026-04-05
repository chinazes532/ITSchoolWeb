FROM python:3.11-slim
WORKDIR /app

# Устанавливаем системные зависимости для сборки пакетов (например, psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
# Переменные окружения пробросит docker-compose, копировать .env не нужно

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# CMD лучше оставить в docker-compose или прописать тут корректно
