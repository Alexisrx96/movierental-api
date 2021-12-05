from rest_framework import generics
from rest_framework import mixins

from casts.api.serializers import CastMemberSerializer, CastRoleSerializer
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

class CastRoleListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = CastRoleSerializer

    def get_queryset(self):
        qs = CastRole.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

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
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
