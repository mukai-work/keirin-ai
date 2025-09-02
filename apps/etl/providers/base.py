from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, datetime
from typing import Literal, Sequence, Tuple

from pydantic import BaseModel, ConfigDict


class Venue(BaseModel):
    id: str
    name: str
    model_config = ConfigDict(frozen=True, extra="forbid")


class Race(BaseModel):
    id: str
    date: date
    venue_id: str
    race_no: int
    model_config = ConfigDict(frozen=True, extra="forbid")


class RaceEntry(BaseModel):
    rider_id: str
    gate: int
    model_config = ConfigDict(frozen=True, extra="forbid")


class RaceCard(BaseModel):
    race: Race
    entries: Sequence[RaceEntry]
    model_config = ConfigDict(frozen=True, extra="forbid")


class OddsItem(BaseModel):
    bet_type: str
    combo: str
    odds: float
    model_config = ConfigDict(frozen=True, extra="forbid")


class Odds(BaseModel):
    race_id: str
    items: Sequence[OddsItem]
    captured_at: datetime
    model_config = ConfigDict(frozen=True, extra="forbid")


class ResultItem(BaseModel):
    rider_id: str
    position: int
    model_config = ConfigDict(frozen=True, extra="forbid")


class Results(BaseModel):
    race_id: str
    items: Sequence[ResultItem]
    model_config = ConfigDict(frozen=True, extra="forbid")


class ScheduleItem(BaseModel):
    race_id: str
    date: date
    model_config = ConfigDict(frozen=True, extra="forbid")


class Schedule(BaseModel):
    items: Sequence[ScheduleItem]
    model_config = ConfigDict(frozen=True, extra="forbid")


class Provider(ABC):
    """Abstract base class for data providers."""

    @abstractmethod
    async def list_venues(self, date: date) -> Sequence[Venue]:
        """List venues scheduled for the given date."""

    @abstractmethod
    async def list_races(self, date: date) -> Sequence[Race]:
        """List races scheduled for the given date."""

    @abstractmethod
    async def get_race_card(self, race_id: str) -> RaceCard:
        """Get race card information for a race."""

    @abstractmethod
    async def get_odds(self, race_id: str, when: Literal["pre", "post"] = "pre") -> Odds:
        """Get odds for a race at pre or post time."""

    @abstractmethod
    async def get_results(self, race_id: str) -> Results:
        """Get results for a race."""

    @abstractmethod
    async def get_schedule(self, date_range: Tuple[date, date]) -> Schedule:
        """Get schedule for races within a date range."""
