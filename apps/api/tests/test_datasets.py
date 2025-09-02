from datetime import date

import pandas as pd

from src.ml.datasets import make_datasets


def test_make_datasets_split() -> None:
    df = pd.DataFrame({"date": pd.date_range("2024-01-01", periods=120)})
    cutoff = date(2024, 4, 30)
    train, valid, test = make_datasets(df, cutoff)

    assert train["date"].max().date() < date(2024, 3, 1)
    assert valid["date"].min().date() >= date(2024, 3, 1)
    assert valid["date"].max().date() < date(2024, 4, 16)
    assert test["date"].min().date() >= date(2024, 4, 16)
    assert test["date"].max().date() <= cutoff
