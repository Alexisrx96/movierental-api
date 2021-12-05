from rest_framework import generics
from rest_framework import mixins

from public.api.serializers import FilmRentSerializer, FilmReturnSerializer
from customers.api.serializers import UserSerializer
from customers.models import Rent, User


class UserListAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = User.objects.filter(is_staff=False).all()
    serializer_class = UserSerializer


class FilmReturnAPIView(
        mixins.UpdateModelMixin,
        generics.RetrieveAPIView
        ):
    permission_classes = []
    authentication_classes = []
    queryset = Rent.objects.all()
    serializer_class = FilmReturnSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class FilmRentAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Rent.objects.all()
    serializer_class = FilmRentSerializer
