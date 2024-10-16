from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings

from .models import (Book, Author, Genre)
from .serializers import (
  BookSerializer,
  AuthorSerializer,
  GenreSerializer,
)


# Create your views here.
class BookList(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]


# Author
class AuthorList(generics.ListCreateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  permission_classes = [IsAuthenticated]


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  permission_classes = [IsAuthenticated]


# Genre
class GenreList(generics.ListCreateAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer
  permission_classes = [IsAuthenticated]


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer
  permission_classes = [IsAuthenticated]
