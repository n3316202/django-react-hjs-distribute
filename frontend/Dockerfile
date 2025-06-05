# ⚙️ 1단계: React 빌드
FROM node:22.14.0 AS build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json* ./frontend/
WORKDIR /app/frontend


RUN npm install 
COPY frontend/ ./

RUN npm run build

# ⚙️ 2단계: Nginx로 정적 파일 서빙
FROM nginx:alpine

COPY --from=build /app/frontend/dist /usr/share/nginx/html

# default.conf는 루트 context에서 복사해야 하므로 compose에서 mount하거나 context에 포함 필요
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]