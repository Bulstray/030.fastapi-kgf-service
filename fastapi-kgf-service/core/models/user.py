from sqlalchemy.orm import Mapped

from .base import Base
from .mixin import IntIdPkMixin


class User(IntIdPkMixin, Base):
    __tablename__ = "users"

    email: Mapped[str]
    hashed_password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    is_superuser: Mapped[bool]
