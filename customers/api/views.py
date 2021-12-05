from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins

from customers.api.serializers import RentSerializer, UserSerializer
from customers.models import Rent, User


class RentListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'rented_at',
        'returned_at',
        'film_title',
        'user__username',
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RentDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.filter(is_staff=False).all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'username',
        'email',
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailsAPIView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.filter(is_staff=False).all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
