from django.conf.urls import url

from casts.api.views import (CastMemberDetailsAPIView, CastMemberListAPIView,
                             CastRoleDetailsAPIView, CastRoleListAPIView)

app_name = 'casts'

urlpatterns = [
    url(r'^members/$',
        CastMemberListAPIView.as_view(),
        name='members'),
    url(r'^members/(?P<pk>\d+)/$',
        CastMemberDetailsAPIView.as_view(),
        name='member-detail'),
    url(r'^roles/$', CastRoleListAPIView.as_view(), name='roles'),
    url(r'^roles/(?P<pk>\d+)/$',
        CastRoleDetailsAPIView.as_view(),
        name='role-detail'),
]
