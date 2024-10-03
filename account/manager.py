from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
  """Set up email as the unique identifier"""
  def create_user(self, email, password, **extra_fields):
    """Create and save user with email and pass"""
    if not email:
      raise ValueError(_("Email must be set"))
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user
  
  def create_superuser(self, email, password, **extra_fields):
    """Create super user with the said fields"""
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)
    extra_fields.setdefault("is_active", True)

    return self.create_user(email, password, **extra_fields)
