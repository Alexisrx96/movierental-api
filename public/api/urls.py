from django.conf.urls import url

from public.api.views import (
    UserListAPIView,
    FilmReturnAPIView,
    FilmRentAPIView
)

app_name = 'public'

urlpatterns = [
    url(r'^create_user/$', UserListAPIView.as_view(), name='create'),
    url(
        r'^return_film/(?P<pk>\d+)/$',
        FilmReturnAPIView.as_view(),
        name='return'
    ),
    url(r'^rent_film/$', FilmRentAPIView.as_view(), name='rent'),
]
