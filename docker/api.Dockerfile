# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base
RUN pip install --no-cache-dir uv
WORKDIR /app

FROM base AS deps
COPY apps/api/requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

FROM python:3.11-slim AS runtime
WORKDIR /app
COPY --from=deps /usr/local /usr/local
COPY apps/api/ ./
USER 1001
HEALTHCHECK CMD curl -f http://localhost:8000/healthz || exit 1
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
