import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from backend.src.db.database import create_db
from backend.src.api.users import user_router

import sys


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is enable")
    print(sys.path)
    await create_db()

    yield

    print("App is disable")


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)

origins = [
    "http://localhost:3000",
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
        factory=True
    )