from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from authentication.views import UserListCreateAPIView, UserDetailAPIView

urlpatterns = patterns(
    '',

    url(r'^api/v1/auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/v1/users/', UserListCreateAPIView.as_view()),
    url(r'^api/v1/users/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view()),

    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
)
