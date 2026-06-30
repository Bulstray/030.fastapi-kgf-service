from pathlib import Path

from pydantic import BaseModel, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class RestPrefix(BaseModel):
    programs: str = "/programs"


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class RedisAuthConfig(BaseModel):
    deadline_seconds: int = 42000


class RedisConfig(BaseModel):
    url: RedisDsn
    auth: RedisAuthConfig = RedisAuthConfig()


class StoragePath(BaseModel):
    programs: Path = BASE_DIR / "uploads/programs"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            ".env.template",
            ".env",
        ),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    paths: StoragePath = StoragePath()
    rest_prefix: RestPrefix = RestPrefix()
    db: DatabaseConfig
    redis: RedisConfig


settings = Settings()
