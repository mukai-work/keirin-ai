"""Dataset preparation utilities."""

from __future__ import annotations

from datetime import date, timedelta
from typing import Tuple

import pandas as pd


def make_datasets(
    df: pd.DataFrame, cutoff_date: date
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split a dataframe into train/validation/test sets.

    The split is performed using fixed windows relative to ``cutoff_date``:

    - Train: data strictly before ``cutoff_date - 60 days``
    - Validation: data in ``[cutoff_date - 60 days, cutoff_date - 14 days)``
    - Test: data in ``[cutoff_date - 14 days, cutoff_date]``

    Args:
        df: DataFrame containing at least a ``date`` column of ``datetime64`` type.
        cutoff_date: Reference end date for the split.

    Returns:
        A tuple of ``(train_df, valid_df, test_df)`` where each dataframe is indexed from zero.
    """
    train_end = cutoff_date - timedelta(days=60)
    valid_end = cutoff_date - timedelta(days=14)

    train_end_ts = pd.Timestamp(train_end)
    valid_end_ts = pd.Timestamp(valid_end)
    cutoff_ts = pd.Timestamp(cutoff_date)

    train_df = df[df["date"] < train_end_ts]
    valid_df = df[(df["date"] >= train_end_ts) & (df["date"] < valid_end_ts)]
    test_df = df[(df["date"] >= valid_end_ts) & (df["date"] <= cutoff_ts)]

    return (
        train_df.reset_index(drop=True),
        valid_df.reset_index(drop=True),
        test_df.reset_index(drop=True),
    )
