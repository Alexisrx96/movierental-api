from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins

from casts.api.serializers import CastMemberSerializer, CastRoleSerializer
from casts.models import CastMember, CastRole


class CastMemberListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = CastMemberSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CastMemberDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = CastMember.objects.all()
    serializer_class = CastMemberSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CastRoleListAPIView(
        mixins.CreateModelMixin,
        generics.ListAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = CastRole.objects.all()
    serializer_class = CastRoleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CastRoleDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = CastRole.objects.all()
    serializer_class = CastRoleSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
