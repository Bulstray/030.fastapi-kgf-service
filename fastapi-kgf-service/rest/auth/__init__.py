from fastapi import APIRouter

from core.config import settings

from .login_page import router as login_page_router


router = APIRouter(
    prefix=settings.rest_prefix.login,
)

router.include_router(login_page_router)
