"""
Django settings for demo3 project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i6e#*me+q4blb4n!*oh8j0rxq%k65@#w#1h95+xj+q)xc*oj0v'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False为调试模式，可以调出404和500错误模板，上线时应关闭改为True
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

# 应用注册配置
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'comments',
    # 注册tinymce应用可以找到应用下方文件夹
    'tinymce',
    # 注册haystack应用用于索引
    'haystack',
]
# 中间件，
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # csrf：跨站请求伪造，关闭时安全性大大降低
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由
ROOT_URLCONF = 'demo3.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 配置模板相对路径
        'DIRS': [os.path.join(BASE_DIR, 'template')],
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

WSGI_APPLICATION = 'demo3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# 配置语言，大小写无所谓
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# 配置时区，大小写无所谓
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# 配置样式相对路径
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# 配置媒体相对路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')


# 配置富文本，这里是针对admin来设置的
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}


# 配置redis缓存
CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "localhost:6379",
        'TIMEOUT': 300,
    },
}


# 配置搜索信息
HAYSTACK_CONNECTIONS = {
'default': {
'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
}
}

# 配置搜索结果分页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
# 配置搜索进程
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'



