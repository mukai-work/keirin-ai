from __future__ import annotations

from datetime import datetime

from typing import Any

from sqlalchemy import DateTime, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class AnalyticsRun(Base):
    __tablename__ = "analytics_runs"

    kind: Mapped[str] = mapped_column(String(20))
    params: Mapped[dict[str, Any] | None] = mapped_column(JSONB)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(String(20))
    metrics: Mapped[dict[str, Any] | None] = mapped_column(JSONB)
