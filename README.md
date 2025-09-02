# Keirin Prediction AI

将来の競輪予測アプリケーションのための最小限の足場となるリポジトリです。

## 前提条件
- Node.js 18 以上および pnpm
- Python 3.11 以上
- Docker（任意）

## セットアップ
TypeScript の依存関係をインストール:
```bash
cd apps/web
pnpm install
cd ../..
```

Python の依存関係をインストール:
```bash
pip install -r apps/api/requirements.txt
```

## 開発
### API
FastAPI サーバーを起動:
```bash
uvicorn src.main:app --app-dir apps/api --reload
```

### Web
Web アプリには現在サンプルの TypeScript コードが含まれています。

## テスト
リンターとテストを実行:
```bash
pnpm lint
pnpm test
PYTHONPATH=apps/api pytest
ruff apps/api
mypy apps/api
```

## ローカルビルド&実行
このリポジトリは Docker Compose と Taskfile を使った一括セットアップに対応しています。

### 前提ツール
- Node 20 LTS / pnpm 9
- Python 3.11 / uv
- Docker (BuildKit 有効)
- go-task (タスクランナー)

### 初期セットアップと起動
`.env` テンプレートをコピーした後、以下を実行します。
```bash
task bootstrap
task up
```
- UI: http://localhost:3000
- API: http://localhost:8000/docs

### 本番相当ビルド
```bash
task build
```
作成されたイメージを使用して `docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build` などで起動できます。

