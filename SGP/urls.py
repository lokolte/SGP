from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from SGP.views import IndexView
from authentication.views import UsuarioViewSet, LoginView, LogoutView, UsuariosConProyectos
from proyectos import views #ProyectoViewSet, ProyectoOperations, ModificarProyectos, ObtenerProyectos#, ProyectosView, cambiar_estado

from django.views.decorators.csrf import csrf_exempt

#router = routers.SimpleRouter(trailing_slash=False)
router = routers.DefaultRouter()#trailing_slash=False)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'proyectos', views.ProyectoViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/login/', LoginView.as_view(), name='login'),
    url(r'^api/logout/', LogoutView.as_view(), name='logout'),

    # vistas de los metodos de los proyectos

    # Ejemplo de como usar los parametros y los views
    url(r'^api/proyecto/(?P<pk>[0-9]+)/estado/(?P<pk2>[0-9]+)/$', views.ProyectoEstado.as_view(), name='estado'),

    #vistas de los metodos de los usuarios
    url(r'^api/user/(?P<pk>[0-9]+)/proyectos/$', UsuariosConProyectos.as_view(), name='proyectos'),

    #url(r'^api/proyectos/modificar', ModificarProyectos.as_view(), name='modificar'),
    #url(r'^api/proyectos/get', ObtenerProyectos.as_view(), name='get'),

    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url('^.*$', IndexView.as_view(), name='index'),
)