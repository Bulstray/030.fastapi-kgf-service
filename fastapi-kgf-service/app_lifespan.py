from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.config import settings
from core.models import db_helper
from storage.db.user import crud as user_crud


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    settings.paths.programs.mkdir(
        exist_ok=True,
        parents=True,
    )

    async with db_helper.session_factory() as session:
        if (
            await user_crud.get_user_by_email(
                session,
                settings.super_user.email,
            )
            is None
        ):
            await user_crud.create_user(session, settings.super_user)

    yield None

    await db_helper.dispose()
