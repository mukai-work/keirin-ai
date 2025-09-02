from __future__ import annotations

from sqlalchemy import ForeignKey, Index, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ShapValue(Base):
    __tablename__ = "shap_values"
    __table_args__ = (
        Index("ix_shap_race_id", "race_id"),
        Index("ix_shap_feature_name", "feature_name"),
        Index("ix_shap_model_version", "model_version"),
    )

    race_id: Mapped[int] = mapped_column(ForeignKey("races.id"))
    rider_id: Mapped[int] = mapped_column(ForeignKey("riders.id"))
    model_version: Mapped[str] = mapped_column(String(50))
    feature_name: Mapped[str] = mapped_column(String(100))
    shap_value: Mapped[float] = mapped_column(Numeric)
    abs_value: Mapped[float] = mapped_column(Numeric)
