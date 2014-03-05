import base

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dashboard',
        'HOST': 'menutab-dashboard.cxfa44dybjaj.ap-northeast-1.rds.amazonaws.com',
        'PORT': '3306',
        'USER': 'dashboard',
        'PASSWORD': 'mark130620'
    }
}