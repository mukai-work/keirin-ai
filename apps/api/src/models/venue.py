from __future__ import annotations

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Venue(Base):
    __tablename__ = "venues"
    __table_args__ = (UniqueConstraint("code"),)

    code: Mapped[str] = mapped_column(String(10))
    name: Mapped[str] = mapped_column(String(100))
    prefecture: Mapped[str] = mapped_column(String(100))
