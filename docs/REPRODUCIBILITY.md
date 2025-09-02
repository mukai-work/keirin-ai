# Reproducibility

This document explains how to recreate datasets, features, and model training runs in a reproducible manner.

## Feature Snapshots

Create immutable snapshots of source tables and derived features:

```bash
make features.snapshot DATE=YYYY-MM-DD
```

The command materializes Parquet files under `data/snapshots/YYYYMMDD/` and updates `features/version.json` and the feature store.

## Verification

Verify that a snapshot matches its recorded manifest:

```bash
make features.verify VER=vYYYYMMDD-N
```

Row counts, column hashes, and null ratios are compared against the manifest so that data drift is detected early.

## Reproducing Training

Re-run model training for a previously released version with identical dependencies and random seeds:

```bash
make reproduce VER=vYYYYMMDD-N
```

Metrics should match the original run within ±1%.
