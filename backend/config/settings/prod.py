# config/settings/dev.py
#개발 전용 설정만 덮어쓴다"는 의미
from .base import *  

DEBUG = True

#ALLOWED_HOSTS = ["example.com", "myapi.com"] 
#도메인에서 오는 요청만 Django가 처리
ALLOWED_HOSTS = ["*"]


#dev_4
print('이전',BASE_DIR)

import os
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('이후',BASE_DIR)

# 정적파일 URL 경로
STATIC_URL = '/static/'
# collectstatic 명령어로 모이는 폴더 (EC2 내 정적파일 모음 경로)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# (개발 중에만) 추가 정적파일 경로 지정 가능
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# dev_5 경로 조절 주의
from dotenv import load_dotenv

PARENT_DIR = BASE_DIR.parent  # 예: /app

print('베이스_의 부모',PARENT_DIR)
load_dotenv(dotenv_path=PARENT_DIR / '.env.prod')  # 또는 '.env.prod' 등

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret")
print('시크릿키',SECRET_KEY)

# dev_6 DB 변경

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'distribute',
        'USER': 'distribute',
        'PASSWORD': 'distribute',
        'HOST': 'db',
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST', 'localhost'),
#         'PORT': os.getenv('DB_PORT', '3306'),
#     }
# }

# dev_7
CSRF_TRUSTED_ORIGINS = [
    "http://52.79.37.117",
    "http://52.79.37.117:8080",
]