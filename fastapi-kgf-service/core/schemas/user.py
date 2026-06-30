from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    first_name: str
    last_name: str
    email: str
