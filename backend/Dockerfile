FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/.env .

COPY backend/ ./backend/

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python3", "backend/main.py"]
