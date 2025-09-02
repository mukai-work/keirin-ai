from __future__ import annotations

from datetime import date
from typing import Any

from sqlalchemy import Date, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class SegmentMetric(Base):
    __tablename__ = "segment_metrics"

    segment_key: Mapped[str] = mapped_column(String(50))
    segment_value: Mapped[str] = mapped_column(String(50))
    from_date: Mapped[date] = mapped_column(Date)
    to_date: Mapped[date] = mapped_column(Date)
    model_version: Mapped[str] = mapped_column(String(50))
    metrics: Mapped[dict[str, Any]] = mapped_column(JSONB)
