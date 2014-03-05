import os

from os.path import abspath, basename, dirname, join, normpath
from sys import path


BASE_DIR = dirname(dirname(abspath(__file__)))

SECRET_KEY = 'hz^1+g&er(wu9tq7ld#p2p&s%cyf^z7qr4fyj81o5$7!zyy-16'

# SECURITY WARNING: don't run with debug turned on in production!



ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['dashboard.menutab.co.kr','localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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


SITE_ROOT = BASE_DIR
# STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
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
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, "templates")
)

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
