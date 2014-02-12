from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'menutab.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
		       url(r'', include('gcm.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^push_app/', include('push_app.urls')),
                       url(r'^order_app/', include('order_app.urls')),
                       )
