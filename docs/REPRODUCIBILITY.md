# 再現性

このドキュメントはデータセット、特徴量、モデル学習を再現可能に再作成する方法を説明します。

## 特徴量スナップショット

ソーステーブルと派生特徴量の不変なスナップショットを作成します:

```bash
make features.snapshot DATE=YYYY-MM-DD
```

コマンドは `data/snapshots/YYYYMMDD/` 配下に Parquet ファイルを作成し、`features/version.json` とフィーチャーストアを更新します。

## 検証

スナップショットが記録されたマニフェストと一致するか確認します:

```bash
make features.verify VER=vYYYYMMDD-N
```

行数、カラムハッシュ、Null 割合がマニフェストと比較され、データドリフトを早期に検出します。

## 学習の再現

公開済みバージョンのモデル学習を同一の依存関係と乱数シードで再実行します:

```bash
make reproduce VER=vYYYYMMDD-N
```

指標は元の実行結果と ±1% の範囲で一致するはずです。

