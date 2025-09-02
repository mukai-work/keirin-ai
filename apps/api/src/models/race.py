from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, UniqueConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .venue import Venue


class Race(Base):
    __tablename__ = "races"
    __table_args__ = (
        UniqueConstraint("venue_id", "date", "race_no"),
        Index("idx_races_date_venue", "date", "venue_id"),
    )

    venue_id: Mapped[int] = mapped_column(ForeignKey("venues.id"))
    date: Mapped[date] = mapped_column(Date())
    race_no: Mapped[int] = mapped_column(Integer())
    name: Mapped[str] = mapped_column(String(100))
    grade: Mapped[str] = mapped_column(String(20))
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    venue: Mapped[Venue] = relationship(backref="races")
