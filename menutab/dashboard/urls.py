from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
url(r'^$', main_html),
url(r'(?P<page>\w+).html$', serve_html),
url(r'login/$', login_view),
url(r'getdashboard/',dashboard_list_view),
url(r'getsearchboard/',dashboard_search_view),
)
