from rest_framework import serializers

from films.models import Film, FilmCast, Chapter, Season, Category
from casts.api.serializers import CastMemberSerializer, CastRoleSerializer


def season_is_from_serie(season):
    if season.film.category.name != 'serie':
        raise serializers.ValidationError(
            {"season": "this season don't belong to a serie"}
        )


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
                "validators": [season_is_from_serie],
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
