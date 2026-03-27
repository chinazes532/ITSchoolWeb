from backend.src.db.models.users import User
from backend.src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
