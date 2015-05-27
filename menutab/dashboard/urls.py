from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
                       url(r'^$',orderboard_page),
                       #url(r'(?P<page>\w+).html$', serve_html , name = 'index'),
                       #url(r'login/$', login_view ),
                       url(r'orderboard/',orderboard_page),
                       url(r'finishboard/',finishboard_page),
                       url(r'cancleboard/',cancleboard_page),
                       url(r'finishhistory/',orderboard_page),
                       url(r'orderitems/',orderboard_view),
                       url(r'finishitems/',finishboard_view),
                       url(r'cancleitems/',cancleboard_view),
                       url(r'orderhistory/',history_order_view),
                       url(r'canclehistory/',history_cancle_view),
)
