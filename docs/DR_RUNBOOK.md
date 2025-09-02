# Disaster Recovery Runbook

This document provides the steps to back up and restore the PostgreSQL database used by Keirin Prediction AI.

## Backups

Nightly full backups and WAL archives are stored in object storage. A manual backup can be triggered with:

```bash
scripts/backup.sh
```

## Point-in-time Recovery

Restore the database to a specific time, such as the previous day at 23:00:

```bash
scripts/restore.sh --timestamp "YYYY-MM-DD 23:00:00"
```

Stop application services before running the restore and verify the system state once recovery completes.
