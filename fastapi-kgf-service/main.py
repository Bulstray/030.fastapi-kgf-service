import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core.config import settings, BASE_DIR
from app_lifespan import lifespan

from rest import router as main_router

app = FastAPI(lifespan=lifespan)

STATIC_PATH = BASE_DIR / "static"
app.mount(
    "/static",
    StaticFiles(directory=STATIC_PATH),
    name="static",
)

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.run.host,
        port=settings.run.port,
    )
