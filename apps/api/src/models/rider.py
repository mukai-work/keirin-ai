from __future__ import annotations

from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Rider(Base):
    __tablename__ = "riders"
    __table_args__ = (UniqueConstraint("registration_no"),)

    registration_no: Mapped[int] = mapped_column(Integer())
    name: Mapped[str] = mapped_column(String(100))
    birthplace: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer())
    klass: Mapped[str] = mapped_column(String(20))
