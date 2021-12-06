from django.conf.urls import url

from films.api.views.films import (CategoryDetailsAPIView, CategoryListAPIView,
                                   FilmDetailsAPIView, FilmListAPIView,
                                   FilmCastListAPIView, FilmCastDetailsAPIView)
from films.api.views.seasons import (ChapterDetailsAPIView, ChapterListAPIView,
                                     SeasonDetailsAPIView, SeasonListAPIView)

app_name = 'films'

urlpatterns = [
    url(r'^films/$',
        FilmListAPIView.as_view(),
        name='films'),
    url(r'^films/(?P<pk>\d+)/$',
        FilmDetailsAPIView.as_view(),
        name='film-detail'),

    url(r'^filmcasts/$',
        FilmCastListAPIView.as_view(),
        name='filmcasts'),
    url(r'^filmcasts/(?P<pk>\d+)/$',
        FilmCastDetailsAPIView.as_view(),
        name='filmcasts-detail'),

    url(r'^chapters/$',
        ChapterListAPIView.as_view(),
        name='chapters'),
    url(r'^chapters/(?P<pk>\d+)/$',
        ChapterDetailsAPIView.as_view(),
        name='chapter-detail'),

    url(r'^seasons/$',
        SeasonListAPIView.as_view(),
        name='seasons'),
    url(r'^seasons/(?P<pk>\d+)/$', SeasonDetailsAPIView.as_view(),
        name='season-detail'),

    url(r'^categories/$', CategoryListAPIView.as_view(),
        name='categories'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetailsAPIView.as_view(),
        name='category-detail'),
]
