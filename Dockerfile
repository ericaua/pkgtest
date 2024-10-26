# syntax=docker/dockerfile:1

FROM python:3.12.7-slim-bookworm
ENV PYTHONUNBUFFERED=True
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN --mount=source=dist,target=/dist uv pip install --system --no-cache /dist/*.whl
ENTRYPOINT ["python", "-m", "pkgtest"]
