from .base import Base

from sqlalchemy.orm import Mapped


class Program(Base):
    __tablename__ = "programs"

    name: Mapped[str]
    description: Mapped[str]
    author: Mapped[str]
    size_file: Mapped[str]
