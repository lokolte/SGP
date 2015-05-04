from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from authentication.views import UserListCreateAPIView, UserDetailAPIView, ProyectoList, ProyectoDetail, \
    FlujoList, FlujoDetail, ActividadList, ActividadDetail, UserStoryList, UserStoryDetail, SprintList, SprintDetail

urlpatterns = patterns(
    '',

    url(r'^api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/v1/users/', UserListCreateAPIView.as_view()),
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view()),
    url(r'^api/v1/proyectos/', ProyectoList.as_view()),
    url(r'^api/v1/proyectos/(?P<pk>[0-9]+)/$', ProyectoDetail.as_view()),
    url(r'^api/v1/sprints/', SprintList.as_view()),
    url(r'^api/v1/sprints/(?P<pk>[0-9]+)/$', SprintDetail.as_view()),
    url(r'^api/v1/flujos/', FlujoList.as_view()),
    url(r'^api/v1/flujos/(?P<pk>[0-9]+)/$', FlujoDetail.as_view()),
    url(r'^api/v1/actividades/', ActividadList.as_view()),
    url(r'^api/v1/actividades/(?P<pk>[0-9]+)/$', ActividadDetail.as_view()),
    url(r'^api/v1/userstories/', UserStoryList.as_view()),
    url(r'^api/v1/userstories/(?P<pk>[0-9]+)/$', UserStoryDetail.as_view()),

    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
)
