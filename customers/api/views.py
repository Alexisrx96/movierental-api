from rest_framework import generics
from rest_framework import mixins

from customers.api.serializers import RentSerializer, UserSerializer
from customers.models import Rent, User


class RentListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

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
    lookup_field = 'id'

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
