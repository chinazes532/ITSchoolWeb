import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

import redis.asyncio as aioredis

from backend.src.db.database import create_db
from backend.src.api.users import user_router

from backend.config import config


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is enable")
    redis = await aioredis.from_url(
        config.redis.redis_url,
        decode_responses=True
    )

    try:
        await redis.ping()
        print("✅ Redis connected successfully")
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")

    await create_db()

    yield

    await redis.aclose()

    print("App is disable")


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)

origins = [
    "http://localhost:3000",
    config.frontend.url,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )