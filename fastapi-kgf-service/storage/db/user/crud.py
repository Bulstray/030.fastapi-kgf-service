from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from sqlalchemy import select
from core.config import SuperUser


async def get_user_by_email(
    session: AsyncSession,
    email: str,
) -> User | None:
    stmt = select(User).where(email == User.email)
    result = await session.scalars(stmt)
    return result.first()


async def create_user(
    session: AsyncSession,
    super_user: SuperUser,
):
    user = User(**super_user.model_dump())
    session.add(user)
    await session.commit()
