from backend.src.services.users import UsersService
from backend.src.repositories.users import UserRepository
from backend.src.services.email import SMTPEmailService


def users_service():
    return UsersService(UserRepository())