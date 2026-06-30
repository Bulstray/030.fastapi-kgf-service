from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class UserRead(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
