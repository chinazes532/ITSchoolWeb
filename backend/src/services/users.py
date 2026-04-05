from backend.src.services.email import AbstractEmailService
from backend.src.utils.repository import AbstractRepository
from backend.src.schemas.users import UserAddSchemas
from backend.src.tasks.email_task import send_admin_notification


class UsersService:
    def __init__(self,
                 user_repo: AbstractRepository,
                 email_service: AbstractEmailService,
                 admin_email: str
                 ):
        self.user_repo: AbstractRepository = user_repo
        self.email_service: AbstractEmailService = email_service
        self.admin_email: str = admin_email

    async def create_new_user(self, creds: UserAddSchemas):
        user_dict = creds.model_dump()
        user_id = await self.user_repo.add_one(user_dict)
        send_admin_notification.delay(
            full_name=creds.full_name,
            phone=creds.phone[4:]
        )
        return user_id
