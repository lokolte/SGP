from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from authentication.views import UsuarioViewSet, IndexView, LoginView, LogoutView
from proyectos.views import ProyectoViewSet

from django.views.decorators.csrf import csrf_exempt

router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'proyectos', ProyectoViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/login/', csrf_exempt(LoginView.as_view()), name='login'),
    url(r'^api/logout/', LogoutView.as_view(), name='logout'),
    url(r'^/api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)
