from __future__ import annotations

from typing import Any

from sqlalchemy import ForeignKey, String, Index
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

from .base import Base


class Prediction(Base):
    __tablename__ = "predictions"
    __table_args__ = (Index("idx_pred_race", "race_id"),)

    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"))
    model_version: Mapped[str] = mapped_column(String(50))
    payload: Mapped[dict[str, Any]] = mapped_column(JSONB)
