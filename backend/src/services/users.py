from backend.src.utils.repository import AbstractRepository
from backend.src.schemas.users import UserAddSchemas


class UsersService:
    def __init__(self, user_repo: AbstractRepository):
        self.user_repo: AbstractRepository = user_repo

    async def create_new_user(self, creds: UserAddSchemas):
        user_dict = creds.model_dump()
        user_id = await self.user_repo.add_one(user_dict)
        return user_id
