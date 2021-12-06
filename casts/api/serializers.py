from rest_framework import serializers

from casts.models import CastMember, CastRole


class CastMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastMember
        fields = ['id', 'name', 'birth_date']


class CastRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastRole
        fields = ['id', 'name']
