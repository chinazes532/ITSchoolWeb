from celery import Celery
from backend.config import config

celery_app = Celery(
    "worker",
    broker=config.redis.redis_url,
    backend=config.redis.redis_url,
    include=[
        "backend.src.tasks.email_task"
    ],
)

celery_app.conf.update(
    task_serializer="json",
    result_expires=3600,
)