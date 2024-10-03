from django.db import models

# Create your models here.
class Author(models.Model):
  """Author Model"""
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return(f"{self.first_name} {self.last_name}")


class Genre(models.Model):
  """Genre Model"""
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Book(models.Model):
  """Book Model"""
  title = models.CharField(max_length=50)
  description = models.TextField(blank=True, null=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
