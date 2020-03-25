from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import User, Book
from .serializers import UserSerializer, BookSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']
