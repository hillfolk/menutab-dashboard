# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
url(r'^$', main_html),
url(r'(?P<page>\w+).html$', serve_html),
url(r'login/$', login_view),
url(r'orderboard/',orderboard_view),
url(r'finishboard/',finishboard_view),
url(r'cancleboard/',cancleboard_view),
url(r'getsearchboard/',history_order_view),
url(r'getcancleboard/',history_cancle_view),
)
