from os import name
from django.conf.urls import url

from customers.api.views import (RentDetailsAPIView, RentListAPIView,
                                 UserDetailsAPIView, UserListAPIView)

app_name = 'customers'

urlpatterns = [
    url(r'^rents/$',
        RentListAPIView.as_view(),
        name='rents'),
    url(r'^rents/(?P<pk>\d+)/$',
        RentDetailsAPIView.as_view(),
        name='rent-detail'),
    url(r'^users/$',
        UserListAPIView.as_view(),
        name='users'),
    url(r'^users/(?P<username>.*)/$',
        UserDetailsAPIView.as_view(),
        name='user-detail'),
]
