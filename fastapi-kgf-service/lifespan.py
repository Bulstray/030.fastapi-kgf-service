from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from core.config import settings


@asynccontextmanager
def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings.paths.programs.mkdir(exist_ok=True, parents=True)

    yield None
