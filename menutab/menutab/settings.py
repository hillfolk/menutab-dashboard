"""
Django settings for menutab project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from os.path import abspath, basename, dirname, join, normpath
from sys import path


BASE_DIR = dirname(dirname(abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hz^1+g&er(wu9tq7ld#p2p&s%cyf^z7qr4fyj81o5$7!zyy-16'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_PATCH_SETTINGS = False

ADMINS = (
     ('Markmedia', 'markmenutab@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['dashboard.menutab.co.kr','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_sockjs_server',
    'south',
    'gcm',
    'debug_toolbar',
    'orders',
    'pushs',
    'staffcall',
    'dashboard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'menutab.cors.XsSharingMiddleware',

)

GCM_APIKEY = 'AIzaSyAssxwZHH2T03y7lq56KLXA8Lo89b72Am0'
GCM_DEVICE_MODEL = 'pushs.models.MenuTabApp'

ROOT_URLCONF = 'menutab.urls'

WSGI_APPLICATION = 'menutab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wdmdashboard',
        'HOST': 'wdmdashboard.cgvb2gghmvsp.ap-northeast-1.rds.amazonaws.com',
        'PORT': '3306',
        'USER': 'wdmdashboard',
        'PASSWORD': 'mark130620'
    }
}
DATABASE_OPTIONS = {'charset': 'utf8'}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = False

USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
SITE_ROOT = BASE_DIR
#STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',
    '%Y/%m/%d',             # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
)


TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, "templates")
)

DJANGO_SOCKJS_SERVER = {
      'rabbitmq_server_host': '127.0.0.1',
      'rabbitmq_user': 'guest',
      'rabbitmq_password': 'guest',
      'rabbitmq_server_port': 5672,
      'rabbitmq_server_vhost': '/',
      'rabbitmq_exhange_name': 'sockjs',
      'rabbitmq_exchange_type': 'fanout',
      'listen_addr': '0.0.0.0',
      'listen_port': 8083,
      'listen_location': '/ws',
      'secret_key': 'xe4pa7gysp4phe2rhyd',
      'sockjs_url': ['http://dashboard.menutab.co.kr:8083/ws']
  }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
