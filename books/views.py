from django.shortcuts import render
from rest_framework import generics

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


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer


# Author
class AuthorList(generics.ListCreateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer


# Genre
class GenreList(generics.ListCreateAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer
