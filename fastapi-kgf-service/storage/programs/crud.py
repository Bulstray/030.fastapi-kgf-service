from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Program


async def get_all_programs(session: AsyncSession) -> list[Program]:
    stmt = select(Program).order_by(Program.id)
    result = await session.scalars(stmt)
    return list(result.all())
