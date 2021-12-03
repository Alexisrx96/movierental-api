from rest_framework import serializers

from films.models import Film, Chapter, Season, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'id',
            'title',
            'description',
            'number',
            'season',
        ]


class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = [
            'id',
            'title',
            'description',
            'film',
            'prequel',
            'sequel',
        ]


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = [
            'id',
            'title',
            'description',
            'stock',
            'price',
            'category',
            'release_date',
        ]
