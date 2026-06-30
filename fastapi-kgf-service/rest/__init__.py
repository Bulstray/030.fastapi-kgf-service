from fastapi import APIRouter

from .auth import router as auth_routes
from .programs import router as programs_routes


router = APIRouter()

router.include_router(auth_routes)
router.include_router(programs_routes)
