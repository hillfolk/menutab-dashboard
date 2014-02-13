from django.conf.urls import patterns, include, url
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                      
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$',include('dashboard.urls')),
		       		   url(r'',include('gcm.urls')),
		       		   url(r'',include('dashboard.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^pushs/', include('pushs.urls')),
                       url(r'^orders/', include('orders.urls')),
                       )
