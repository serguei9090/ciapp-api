# syntax=docker/dockerfile:1.7
FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["flask","--app","app","run","--host=0.0.0.0","--port=5000"]
