from sqlalchemy.orm import Mapped

from .base import Base
from .mixin.int_id_pk import IntIdPkMixin


class Program(IntIdPkMixin, Base):
    __tablename__ = "programs"

    name: Mapped[str]
    description: Mapped[str]
    author: Mapped[str]
    size_file: Mapped[str]

    path: Mapped[str]
    original_name_file: Mapped[str]
