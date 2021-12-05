from django.conf.urls import url

from films.api.views import (
    FilmListAPIView,
    FilmDetailsAPIView,
    ChapterListAPIView,
    ChapterDetailsAPIView,
    SeasonListAPIView,
    SeasonDetailsAPIView,
    CategoryListAPIView,
    CategoryDetailsAPIView,
)

app_name = 'film'

urlpatterns = [
    url(r'^films/$', FilmListAPIView.as_view()),
    url(r'^films/(?P<pk>\d+)/$', FilmDetailsAPIView.as_view()),

    url(r'^chapters/$', ChapterListAPIView.as_view()),
    url(r'^chapters/(?P<pk>\d+)/$', ChapterDetailsAPIView.as_view()),

    url(r'^seasons/$', SeasonListAPIView.as_view()),
    url(r'^seasons/(?P<pk>\d+)/$', SeasonDetailsAPIView.as_view()),

    url(r'^categories/$', CategoryListAPIView.as_view()),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetailsAPIView.as_view()),
]
