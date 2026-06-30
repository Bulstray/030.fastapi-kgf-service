from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from core.config import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        pool_size: int,
        max_overflow: int,
    ) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=settings.db.echo,
            echo_pool=settings.db.echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=f"{settings.db.url}",
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
