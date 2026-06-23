from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI


@asynccontextmanager
def lifespan(app: FastAPI) -> AsyncIterator[None]:
    pass
