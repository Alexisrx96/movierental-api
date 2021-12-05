from django.conf.urls import url

from films.api.views.films import (CategoryDetailsAPIView, CategoryListAPIView,
                                   FilmDetailsAPIView, FilmListAPIView)
from films.api.views.seasons import (ChapterDetailsAPIView, ChapterListAPIView,
                                     SeasonDetailsAPIView, SeasonListAPIView)

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
