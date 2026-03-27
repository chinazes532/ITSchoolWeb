from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, create_async_engine, async_sessionmaker
from backend.config import config

engine = create_async_engine(
    url=config.database.sqlalchemy_url(),
    echo=True
)
async_session = async_sessionmaker(engine,
                                   expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


async def create_db():
    from backend.src.db.models.users import User

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)