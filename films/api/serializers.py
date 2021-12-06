from rest_framework import serializers

from casts.api.serializers import CastMemberSerializer, CastRoleSerializer
from films.api.validators import (allow_only_films_from_serie_category,
                                  allow_only_season_from_serie_category)
from films.models.films import Category, Film, FilmCast
from films.models.seasons import Chapter, Season


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
        extra_kwargs = {
            "season": {
                "validators": [allow_only_season_from_serie_category],
            },
        }


class SeasonSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = [
            'id',
            'title',
            'description',
            'film',
            'prequel',
            'sequel',
            'chapters',
        ]
        extra_kwargs = {
            "film": {
                "validators": [allow_only_films_from_serie_category],
            },
        }


class FilmCastSerializer(serializers.ModelSerializer):
    member = CastMemberSerializer(read_only=True)
    role = CastRoleSerializer(read_only=True)

    class Meta:
        model = FilmCast
        fields = ['member', 'role']


class FilmSerializer(serializers.ModelSerializer):
    cast = FilmCastSerializer(
        source='filmcast_set',
        many=True,
        read_only=True,
    )
    seasons = SeasonSerializer(many=True, read_only=True,)

    class Meta:
        model = Film
        fields = [
            'id',
            'title',
            'description',
            'stock',
            'price',
            'availability',
            'category',
            'release_date',
            'cast',
            'seasons',
        ]

    def update(self, instance, validated_data):
        validated_data.pop('category', None)
        return super(FilmSerializer, self).update(instance, validated_data)


class AddCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmCast
        fields = ['film', 'member', 'role']
