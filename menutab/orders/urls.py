from django.conf.urls import patterns, include, url
from orders.views import *


urlpatterns = patterns('',
url(r'$^',order_list_view),
url(r'(?P<method>create)/$',order_create_view),
url(r'(?P<method>createlist)/$',order_list_create_view),
url(r'(?P<method>allcompleted)/$',order_list_completed_view),
url(r'(?P<method>allcancle)/$',order_list_cancle_view),
url(r'(?P<num>\w+)/(?P<method>update)/$',order_update_view),
url(r'(?P<num>\w+)/$',order_view),
)
