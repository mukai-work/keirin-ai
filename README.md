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
