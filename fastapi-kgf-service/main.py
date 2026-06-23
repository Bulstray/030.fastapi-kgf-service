import uvicorn
from fastapi import FastAPI

from core.config import settings
from lifespan import lifespan

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.run.host,
        port=settings.run.port,
    )
