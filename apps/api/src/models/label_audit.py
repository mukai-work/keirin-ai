from __future__ import annotations

from typing import Any

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class LabelAudit(Base):
    __tablename__ = "label_audit"

    task_id: Mapped[int] = mapped_column(ForeignKey("label_tasks.id"))
    before: Mapped[dict[str, Any] | None] = mapped_column(JSONB)
    after: Mapped[dict[str, Any] | None] = mapped_column(JSONB)
    operator: Mapped[str] = mapped_column(String(50))
