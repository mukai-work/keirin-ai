from __future__ import annotations

from sqlalchemy import ForeignKey, Numeric, String, Index
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Odds(Base):
    __tablename__ = "odds"
    __table_args__ = (
        Index("idx_odds_race_bet", "race_id", "bet_type"),
    )

    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"))
    bet_type: Mapped[str] = mapped_column(String(20))
    combo: Mapped[str] = mapped_column(String(20))
    odds: Mapped[float] = mapped_column(Numeric(10, 2))
