from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class Settings(BaseSettings):
    run: RunConfig = RunConfig()


settings = Settings()
