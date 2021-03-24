import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# DEBUG = False
ALLOWED_HOSTS = ['*']

DEBUG = True
SECRET_KEY = 'hao@_p9(=+6x#z)(8%6q2c!ew0xm2h4@o-7o)m@4_5zscrl$j#'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'applications.apps.ApplicationsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware' #一番下に追加しないとエラー？
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# dj_database_url.config()では、環境変数の一つであるDATABASE_URLを元に接続情報のディクショナリーが入ります。HerokuではディフォルトでDATABASE_URLにPostgresのパスが設定されているため、これ以上の設定は必要ありません。
# https://qiita.com/terappy/items/803ff638d63b3dc09ada
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://qiita.com/shonansurvivors/items/ff2dc23ed0962c2a6f12
# ここの方法→HTML、adminページのcss表示OK
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = 'staticfiles'

# akiyokoさんの方法→HTML、adminページのcss表示OK
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# PROJECT_NAME = os.path.basename(BASE_DIR)
# STATIC_ROOT = 'var/www/{}/static'.format(PROJECT_NAME)

# https://devcenter.heroku.com/ja/articles/django-assets
# Herokuの方法→HTML、adminページのcss表示OK
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# この処理を追加することで settings.py の DEBUG が False でも local_settings があればデバッグ環境だと判断されて runserver が可能になる→DEBUGを切り替える必要もなくなる
try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']

##################
# Authentication #
##################
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/work_apps/ya_src_tool/v3/'
LOGOUT_REDIRECT_URL = '/work_apps/accounts/login/'