from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
  """Custom User Model"""
  username = None
  email = models.EmailField(_("email address"), unique=True)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email
