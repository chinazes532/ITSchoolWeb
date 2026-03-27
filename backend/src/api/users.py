from typing import Annotated

from fastapi import APIRouter, Depends
from backend.src.schemas.users import UserAddSchemas

from backend.src.services.users import UsersService
from backend.src.api.dependencies import users_service


user_router = APIRouter(
    prefix="/users",
    tags=["👤 Пользователи"],
)


@user_router.post("/", name="Добавление пользователя в БД")
async def new_user(
        data: UserAddSchemas,
        user_service: Annotated[UsersService, Depends(users_service)]
):
    user_id = await user_service.create_new_user(data)
    return {"user_id": user_id}