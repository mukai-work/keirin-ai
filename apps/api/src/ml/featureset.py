"""Feature engineering utilities."""

from __future__ import annotations

from datetime import date
from typing import Optional, Tuple

import pandas as pd


def build_features(
    *,
    race_id: Optional[int] = None,
    date_range: Optional[Tuple[date, date]] = None,
) -> pd.DataFrame:
    """Build features for a race or a date range.

    Args:
        race_id: Identifier of the target race. Mutually exclusive with ``date_range``.
        date_range: Inclusive start and end dates. Mutually exclusive with ``race_id``.

    Returns:
        ``pandas.DataFrame`` containing engineered features.

    Raises:
        ValueError: If neither or both of ``race_id`` and ``date_range`` are provided.
    """
    if (race_id is None) == (date_range is None):
        msg = "Either race_id or date_range must be provided, but not both"
        raise ValueError(msg)

    # TODO: implement feature extraction logic.
    return pd.DataFrame()
