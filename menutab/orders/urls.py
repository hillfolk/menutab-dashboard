from django.conf.urls import patterns, include, url
from orders.views import *


urlpatterns = patterns('',

url(r'$^',order_list_view),
url(r'neworders/$',new_order_view),
url(r'(?P<method>create)/$',order_create_view),
url(r'(?P<num>\w+)/(?P<method>update)/$',order_update_view),
url(r'(?P<num>\w+)/(?P<method>cookstart)/$',order_update_view),
url(r'(?P<num>\w+)/(?P<method>cookdone)/$',order_update_view),
url(r'(?P<num>\w+)/$',order_view),
)