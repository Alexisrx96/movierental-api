from rest_framework import serializers

from customers.models import Rent, User


class RentSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if data['returned_at'] and data['rented_at'] > data['returned_at']:
            raise serializers.ValidationError(
                {"returned_at": "return must occur after rent"}
            )
        return data

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
            'total',
        ]
        read_only_fields = ('total', 'price', 'extra_day_fee')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]
