from django.conf.urls import url

from .views import (
    CastMemberListAPIView,
    CastMemberDetailsAPIView,
    CastRoleDetailsAPIView,
    CastRoleListAPIView
)

app_name = 'cast'

urlpatterns = [
    url(r'^members/$', CastMemberListAPIView.as_view()),
    url(
        r'^members/(?P<id>\d+)/$',
        CastMemberDetailsAPIView.as_view(),
        name='member-detail'
    ),
    url(r'^roles/$', CastRoleListAPIView.as_view()),
    url(
        r'^roles/(?P<id>\d+)/$',
        CastRoleDetailsAPIView.as_view(),
        name='role-detail'
    ),
]
