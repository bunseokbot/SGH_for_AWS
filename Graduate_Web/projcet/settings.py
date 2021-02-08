"""
Django settings for projcet project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import platform
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$9!ib@j_wk2%a@5%^a!vjbslh10fh_p@z2)wk5p+ff5(+a2lf^'

# 개발시엔 True로 디버그 확인, 배포시엔 False
DEBUG = True    # 우선 사용자 피드백을 위해 켜두자
'''
if platform.system() == 'Windows':
    DEBUG = True
else:
    DEBUG = False
'''


# 호스트 설정
ALLOWED_HOSTS = [
    # 개발용 호스트(모두 허용)
    '*',
    # 배포용 호스트
    #'.ap-northeast-2.compute.amazonaws.com',
]


# 세션 설정
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 브라우저 종료시 세션 파괴
SESSION_COOKIE_AGE = 60*10                 # 10분 지나면 세션 파괴


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projcet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'projcet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'graduate_help',
        'USER': 'root',
        'PASSWORD': '8813',
        'HOST': '3.34.126.50',
        'PORT': '3306',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# static file 경로 설정

# 내가 쓰고있는 스태틱 경로 (collectstatic 할때 참조)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app', 'static')
]

# 장고가 스태틱 모아줄때 폴더명 지정
STATIC_ROOT = os.path.join(BASE_DIR, 'col_static')

# 요청 받는 이름
STATIC_URL = '/static/'



# media root 추가
# app폴더의 하위폴더로 루트 설정.
# MEDIA_ROOT = os.path.join(BASE_DIR , 'app/uploaded_media')
# MEDIA_URL = '/app/uploaded_media/'

