from pydantic_settings import BaseSettings
from pydantic import Field

class CommonConfig(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


class DatabaseConfig(CommonConfig):
    db_name: str = Field(..., alias="DB_NAME")
    db_user: str = Field(..., alias="DB_USER")
    db_password: str = Field(..., alias="DB_PASSWORD")
    db_host: str = Field(..., alias="DB_HOST")
    db_port: int = Field(..., alias="DB_PORT")

    def sqlalchemy_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class RedisConfig(CommonConfig):
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")


class EmailConfig(CommonConfig):
    gmail_sender: str = Field(..., alias="GMAIL_SENDER")
    gmail_password: str = Field(..., alias="GMAIL_PASSWORD")
    admin_mail: str = Field(..., alias="ADMIN_MAIL")


class FrontendUrl(CommonConfig):
    url: str = Field(..., alias="FRONTEND_URL")


class Settings:
    database = DatabaseConfig()
    email = EmailConfig()
    frontend = FrontendUrl()
    redis = RedisConfig()


config = Settings()
