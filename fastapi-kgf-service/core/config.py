from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class ApiV1Prefix:
    prefix: str = "/v1"
    programs: str = "/programs"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class StoragePath(BaseModel):
    programs: Path = BASE_DIR / "uploads/programs"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    paths: StoragePath = StoragePath()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
