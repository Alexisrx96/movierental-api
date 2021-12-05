from rest_framework import serializers


def allow_only_season_from_serie_category(season):
    if season.film.category.name != 'serie':
        raise serializers.ValidationError(
            {"season": "this season don't belong to a serie"}
        )


def allow_only_films_from_serie_category(film):
    if film.category.name != 'serie':
        raise serializers.ValidationError(
            {"film": "this film is not a serie"}
        )
