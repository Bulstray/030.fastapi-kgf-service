from fastapi import APIRouter

from .auth import router as auth_routes


router = APIRouter()

router.include_router(auth_routes)
