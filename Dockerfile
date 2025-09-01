# syntax=docker/dockerfile:1

FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Установим системные зависимости (если понадобятся)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl tini && \
    rm -rf /var/lib/apt/lists/*

# Скопируем зависимости отдельно для кеша слоев
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем исходники
COPY app /app/app

# Необязательно, но удобно (проверка здоровья)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://127.0.0.1:8000/health || exit 1

EXPOSE 8000

# tini — аккуратный init-процесс
ENTRYPOINT ["/usr/bin/tini", "--"]

# Uvicorn без --reload (прод)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
