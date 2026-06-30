from fastapi import APIRouter

from core.config import settings

from .programs_page import router as program_page_router

router = APIRouter(prefix=settings.rest_prefix.programs)

router.include_router(program_page_router)
