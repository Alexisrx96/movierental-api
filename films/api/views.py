from rest_framework import generics
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

from films.api.serializers import (
    CategorySerializer,
    ChapterSerializer,
    FilmSerializer,
    SeasonSerializer
)
from films.models import Film, Chapter, Season, Category


class FilmListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'title',
        'category__name',
        'release_date',
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FilmDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ChapterListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'title',
        'season__film__title',
        'season__title',
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ChapterDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SeasonListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'title',
        'film__title',
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SeasonDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'name',
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
