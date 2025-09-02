from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class RaceEntry(Base):
    __tablename__ = "race_entries"
    __table_args__ = (
        UniqueConstraint("race_id", "rider_id"),
        Index("idx_entries_race_bike", "race_id", "bike_no", unique=True),
    )

    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"))
    rider_id: Mapped[int] = mapped_column(ForeignKey("riders.id"))
    bike_no: Mapped[int] = mapped_column(Integer())
    line_group: Mapped[str] = mapped_column(String(50))
    handicap: Mapped[str | None] = mapped_column(String(50), nullable=True)
