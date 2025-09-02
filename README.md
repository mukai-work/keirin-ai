# Keirin Prediction AI

Minimal scaffold for a future Keirin prediction application.

## Prerequisites
- Node.js 18+ and pnpm
- Python 3.11+
- Docker (optional)

## Setup
Install TypeScript dependencies:
```bash
cd apps/web
pnpm install
cd ../..
```

Install Python dependencies:
```bash
pip install -r apps/api/requirements.txt
```

## Development
### API
Run the FastAPI server:
```bash
uvicorn src.main:app --app-dir apps/api --reload
```

### Web
The web app currently contains sample TypeScript code.

## Testing
Run linters and tests:
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
