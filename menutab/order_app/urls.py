from django.conf.urls import patterns, include, url
from order_app.views import *


urlpatterns = patterns('',

url(r'orders/$',order_list_view),
url(r'neworders/$',new_order_view),
url(r'orders/(?P<method>create)/$',order_create_view),
url(r'orders/(?P<num>\w+)/(?P<method>update)/$',order_update_view),
url(r'orders/(?P<num>\w+)/(?P<method>cookstart)/$',order_update_view),
url(r'orders/(?P<num>\w+)/(?P<method>cookdone)/$',order_update_view),
url(r'orders/(?P<num>\w+)/$',order_view),
url(r'home/(?P<page>\w+).html$', serve_html),
url(r'login/$', login_view),

)