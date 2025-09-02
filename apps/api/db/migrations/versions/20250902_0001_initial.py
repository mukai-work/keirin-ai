"""initial tables

Revision ID: 20250902_0001_initial
Revises: 
Create Date: 2025-09-02 00:01:00
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20250902_0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "venues",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("code", sa.String(length=10), nullable=False, unique=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("prefecture", sa.String(length=100), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_table(
        "races",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("venue_id", sa.Integer(), sa.ForeignKey("venues.id"), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("race_no", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("grade", sa.String(length=20), nullable=False),
        sa.Column("start_time", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("venue_id", "date", "race_no"),
    )
    op.create_index("idx_races_date_venue", "races", ["date", "venue_id"])

    op.create_table(
        "riders",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("registration_no", sa.Integer(), nullable=False, unique=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("birthplace", sa.String(length=100), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("klass", sa.String(length=20), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )

    op.create_table(
        "race_entries",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("race_id", sa.Integer(), sa.ForeignKey("races.id"), nullable=False),
        sa.Column("rider_id", sa.Integer(), sa.ForeignKey("riders.id"), nullable=False),
        sa.Column("bike_no", sa.Integer(), nullable=False),
        sa.Column("line_group", sa.String(length=50), nullable=False),
        sa.Column("handicap", sa.String(length=50)),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("race_id", "rider_id"),
    )
    op.create_index(
        "idx_entries_race_bike", "race_entries", ["race_id", "bike_no"], unique=True
    )

    op.create_table(
        "odds",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("race_id", sa.Integer(), sa.ForeignKey("races.id"), nullable=False),
        sa.Column("bet_type", sa.String(length=20), nullable=False),
        sa.Column("combo", sa.String(length=20), nullable=False),
        sa.Column("odds", sa.Numeric(10, 2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("idx_odds_race_bet", "odds", ["race_id", "bet_type"])

    op.create_table(
        "predictions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("race_id", sa.Integer(), sa.ForeignKey("races.id"), nullable=False),
        sa.Column("model_version", sa.String(length=50), nullable=False),
        sa.Column("payload", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("idx_pred_race", "predictions", ["race_id"])


def downgrade() -> None:
    op.drop_index("idx_pred_race", table_name="predictions")
    op.drop_table("predictions")

    op.drop_index("idx_odds_race_bet", table_name="odds")
    op.drop_table("odds")

    op.drop_index("idx_entries_race_bike", table_name="race_entries")
    op.drop_table("race_entries")

    op.drop_table("riders")

    op.drop_index("idx_races_date_venue", table_name="races")
    op.drop_table("races")

    op.drop_table("venues")
