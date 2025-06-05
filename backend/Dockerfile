FROM python:3.12-slim

WORKDIR /app

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    libtiff5-dev \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements 복사 및 설치
COPY backend/ .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# 소스 복사
COPY backend/ ./backend/
COPY backend/manage.py .

