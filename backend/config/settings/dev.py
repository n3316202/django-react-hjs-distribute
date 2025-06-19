# config/settings/dev.py
#개발 전용 설정만 덮어쓴다"는 의미
from .base import *  

DEBUG = True

#ALLOWED_HOSTS = ["example.com", "myapi.com"] 
#도메인에서 오는 요청만 Django가 처리
ALLOWED_HOSTS = ["*"]

#dev_11 개발시 Origin 허용 - 배포시 불필요 - Nginx 프록시 이용시 
CORS_ORIGIN_ALLOW_ALL = True 
# <- 모든 호스트 허용

# or 
# CORS_ORIGIN_WHITELIST = (
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000"
# )