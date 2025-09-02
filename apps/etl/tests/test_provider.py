from __future__ import annotations

import asyncio
from datetime import date, datetime
from typing import Literal, Sequence, Tuple

from apps.etl.providers.base import (
    Odds,
    OddsItem,
    Provider,
    Race,
    RaceCard,
    RaceEntry,
    Results,
    ResultItem,
    Schedule,
    ScheduleItem,
    Venue,
)


class DummyProvider(Provider):
    async def list_venues(self, date: date) -> Sequence[Venue]:
        return [Venue(id="1", name="Example Venue")]

    async def list_races(self, date: date) -> Sequence[Race]:
        return [Race(id="R1", date=date, venue_id="1", race_no=1)]

    async def get_race_card(self, race_id: str) -> RaceCard:
        race = Race(id=race_id, date=date.today(), venue_id="1", race_no=1)
        entry = RaceEntry(rider_id="RID1", gate=1)
        return RaceCard(race=race, entries=[entry])

    async def get_odds(self, race_id: str, when: Literal["pre", "post"] = "pre") -> Odds:
        item = OddsItem(bet_type="win", combo="1", odds=2.0)
        return Odds(race_id=race_id, items=[item], captured_at=datetime.now())

    async def get_results(self, race_id: str) -> Results:
        result = ResultItem(rider_id="RID1", position=1)
        return Results(race_id=race_id, items=[result])

    async def get_schedule(self, date_range: Tuple[date, date]) -> Schedule:
        item = ScheduleItem(race_id="R1", date=date_range[0])
        return Schedule(items=[item])


def test_dummy_provider() -> None:
    provider = DummyProvider()
    today = date.today()

    venues = asyncio.run(provider.list_venues(today))
    assert venues and venues[0].name == "Example Venue"

    races = asyncio.run(provider.list_races(today))
    assert races[0].race_no == 1

    card = asyncio.run(provider.get_race_card("R1"))
    assert card.race.id == "R1" and card.entries[0].rider_id == "RID1"

    odds = asyncio.run(provider.get_odds("R1"))
    assert odds.items[0].odds == 2.0

    results = asyncio.run(provider.get_results("R1"))
    assert results.items[0].position == 1

    schedule = asyncio.run(provider.get_schedule((today, today)))
    assert schedule.items[0].race_id == "R1"
