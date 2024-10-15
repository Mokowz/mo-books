from django.shortcuts import render
from rest_framework import generics
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

  @method_decorator(cache_page(settings.CACHE_TTL))
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

  @method_decorator(cache_page(settings.CACHE_TTL))
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)


# Author
class AuthorList(generics.ListCreateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

  @method_decorator(cache_page(settings.CACHE_TTL))
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

  @method_decorator(cache_page(settings.CACHE_TTL))
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)


# Genre
class GenreList(generics.ListCreateAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer

  @method_decorator(cache_page(settings.CACHE_TTL))
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer

  @method_decorator(cache_page(settings.CACHE_TTL))
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)
