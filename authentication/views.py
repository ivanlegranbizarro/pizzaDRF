from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
