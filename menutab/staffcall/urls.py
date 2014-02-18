from django.conf.urls import patterns, include, url
from staffcall.views import *

urlpatterns = patterns('',

url(r'$^',staffcall_list_view),
url(r'staffcall/new$',new_staffcall_view),
url(r'(?P<method>create)/$',staffcall_create_view),
url(r'(?P<num>\w+)/(?P<method>update)/$',staffcall_update_view),
url(r'(?P<num>\w+)/$',staffcall_view),
)
