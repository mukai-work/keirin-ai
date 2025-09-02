# syntax=docker/dockerfile:1
FROM node:20 AS base
WORKDIR /app

FROM base AS build
COPY apps/web/package.json apps/web/pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY apps/web/ .
ARG NODE_ENV=production
RUN pnpm build

FROM node:20 AS runtime
WORKDIR /app
ENV NODE_ENV=production
COPY --from=build /app/.output ./.output
EXPOSE 3000
CMD ["node", ".output/server/index.mjs"]
