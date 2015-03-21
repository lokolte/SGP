from django.conf.urls import patterns, include, url
from django.contrib import admin
from SGPv1 import views

urlpatterns = patterns('',
  url(r'^login/$', 'django.contrib.auth.views.login'),
url(r'^$', views.index, name='index'),
url(r'^home/', views.home, name='home'),
url(r'^admin/', include(admin.site.urls))
  )

