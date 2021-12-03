from rest_framework import generics
from rest_framework import mixins

from .serializers import CastMemberSerializer, CastRoleSerializer
from casts.models import CastMember, CastRole


class CastMemberListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = CastMemberSerializer

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
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
