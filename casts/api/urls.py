from django.conf.urls import url

from casts.api.views import (
    CastMemberListAPIView,
    CastMemberDetailsAPIView,
    CastRoleDetailsAPIView,
    CastRoleListAPIView
)

app_name = 'cast'

urlpatterns = [
    url(r'^members/$', CastMemberListAPIView.as_view()),
    url(
        r'^members/(?P<pk>\d+)/$',
        CastMemberDetailsAPIView.as_view(),
        name='member-detail'
    ),
    url(r'^roles/$', CastRoleListAPIView.as_view()),
    url(
        r'^roles/(?P<pk>\d+)/$',
        CastRoleDetailsAPIView.as_view(),
        name='role-detail'
    ),
]
