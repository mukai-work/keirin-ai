from __future__ import annotations

from typing import Any

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class LabelTask(Base):
    __tablename__ = "label_tasks"

    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"))
    type: Mapped[str] = mapped_column(String(20))
    payload: Mapped[dict[str, Any]] = mapped_column(JSONB)
    status: Mapped[str] = mapped_column(String(20))
    assigned_to: Mapped[int | None] = mapped_column(Integer, nullable=True)
