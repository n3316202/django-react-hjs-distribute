# config/settings/dev.py
#개발 전용 설정만 덮어쓴다"는 의미
from .base import *  

DEBUG = True

#ALLOWED_HOSTS = ["example.com", "myapi.com"] 
#도메인에서 오는 요청만 Django가 처리
ALLOWED_HOSTS = ["*"]