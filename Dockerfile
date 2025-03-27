FROM python:3.12-bookworm AS builder

ENV UV_COMPILE_BYTECODE=1 PYTHONUNBUFFERED=1 UV_LINK_MODE=copy PATH="/app/.venv/bin:$PATH"
WORKDIR /app/

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=ssh uv sync --frozen --no-dev

FROM builder AS production_builder

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=ssh uv sync --frozen --group=prod

FROM builder AS development

COPY . /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=ssh uv sync --frozen

FROM development AS ci

FROM python:3.12-slim-bookworm AS production

ARG VERSION
ENV PYTHONUNBUFFERED=1 SENTRY_RELEASE=${VERSION} PATH="/app/.venv/bin:$PATH" VIRTUAL_ENV="/app/.venv"
WORKDIR /app/

COPY . .
COPY --from=production_builder --chown=app:app /app/ /app/
