from rest_framework import serializers
from customers.models import Rent


class FilmRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = [
            'id',
            'rented_at',
            'rented_days',
            'film',
            'user',
        ]

    def create(self, validated_data):
        film = validated_data['film']
        if not film.stock:
            raise serializers.ValidationError(
                {"film": film.availability}
            )

        return super(
            FilmRentSerializer, self).create(validated_data)


class FilmReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = [
            'id',
            'rented_at',
            'returned_at',
            'rented_days',
            'price',
            'extra_day_fee',
            'film',
            'user',
        ]

        read_only_fields = [
            'id',
            'rented_at',
            'rented_days',
            'price',
            'extra_day_fee',
            'film',
            'user',
        ]

    def update(self, instance: Rent, validated_data):
        if instance.rented_at:
            raise serializers.ValidationError(
                {"returned_at": "The film is already returned"}
            )

        if not validated_data['returned_at']:
            raise serializers.ValidationError(
                {"returned_at": "Return date can't be empty"}
            )

        if instance.rented_at > validated_data['returned_at']:
            raise serializers.ValidationError(
                {"returned_at": "Return must occur after rent"}
            )

        return super(
            FilmReturnSerializer, self).update(instance, validated_data)
