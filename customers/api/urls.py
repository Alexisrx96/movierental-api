from django.conf.urls import url

from customers.api.views import (RentDetailsAPIView, RentListAPIView,
                                 UserDetailsAPIView, UserListAPIView)

app_name = 'rents'

urlpatterns = [
    url(r'^rents/$', RentListAPIView.as_view()),
    url(
        r'^rents/(?P<pk>\d+)/$',
        RentDetailsAPIView.as_view(),
    ),
    url(r'^users/$', UserListAPIView.as_view()),
    url(
        r'^users/(?P<username>.*)/$',
        UserDetailsAPIView.as_view(),
    ),
]
