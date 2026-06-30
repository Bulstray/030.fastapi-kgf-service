import bcrypt

from core.schemas import UserRead
from storage.redis.auth import crud as auth_crud
from sqlalchemy.ext.asyncio import AsyncSession


from storage.db.user import crud as user_crud


async def validate_basic_auth_user(
    session: AsyncSession,
    email: str,
    password: str,
) -> str | None:

    is_user = await user_crud.get_user_by_email(
        session,
        email.lower(),
    )

    if is_user and bcrypt.checkpw(
        password=password.encode("utf-8"),
        hashed_password=is_user.hashed_password.encode("utf-8"),
    ):

        user = UserRead.model_validate(is_user)

        return await auth_crud.save_session(user)

    return None
