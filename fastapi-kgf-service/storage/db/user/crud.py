from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from sqlalchemy import select


async def get_user_by_email(
    session: AsyncSession,
    email: str,
) -> User | None:
    stmt = select(User).where(email == User.email)
    result = await session.scalars(stmt)
    return result.first()
