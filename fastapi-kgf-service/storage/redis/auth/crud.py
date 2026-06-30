from redis.asyncio import Redis
import uuid

from core.config import settings
from core.schemas import UserRead

redis = Redis(
    host=settings.redis.connection.host,
    port=settings.redis.connection.port,
    db=settings.redis.database.sessions,
    decode_responses=settings.redis.decode_response,
)


async def save_session(
    user: UserRead,
) -> str:
    session_id = f"{uuid.uuid4().hex}"
    await redis.set(
        session_id,
        user.model_dump_json(),
        ex=settings.redis.auth.lifetime_seconds,
    )
    return session_id
