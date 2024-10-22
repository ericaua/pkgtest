# syntax=docker/dockerfile:1

FROM python:3.12.7-slim-bookworm
ENV PYTHONUNBUFFERED=True
RUN pip install uv
RUN --mount=source=dist,target=/dist uv pip install --system --no-cache /dist/*.whl
ENTRYPOINT ["python", "-m", "pkgtest"]
