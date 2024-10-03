from rest_framework import serializers
from .models import (Book, Author, Genre)


class BookSerializer(serializers.ModelSerializer):
  """"""
  class Meta:
    model = Book
    fields = ['id', 'title', 'description', 'author', 'genre']


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id', 'first_name', 'last_name']


class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = ['id', 'name']