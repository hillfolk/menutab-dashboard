from django.conf.urls import patterns, include, url
from .views import *




urlpatterns = patterns('',
	url(r'send_push/(?P<id>\w+)/(?P<msg>\w+)/$', send_messge),
	url(r'(?P<method>\w+)/$', DeviceBinding),
    


)