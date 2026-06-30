from fastapi import APIRouter

from .auth import router as auth_router
from .programs import router as programs_router
from .home import router as home_router


router = APIRouter()

router.include_router(auth_router)
router.include_router(programs_router)
router.include_router(home_router)
