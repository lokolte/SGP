from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  url(r'^login/$', 'django.contrib.auth.views.login'),
url(r'^$', include('SGPv1.urls')),
url(r'^admin/', include(admin.site.urls))
)

