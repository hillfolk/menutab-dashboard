from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
                       url(r'auth/$',auth_login,name='auth'),
                       url(r'login/$',login_page,name='login'),
                       url('logout/$',auth_logout,name="logout"),
                       

)
