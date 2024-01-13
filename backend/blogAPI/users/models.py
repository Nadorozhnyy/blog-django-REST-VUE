from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("email"), blank=False, null=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="users"
    )
    name = models.CharField(max_length=30, verbose_name=_('name'))
    surname = models.CharField(max_length=30, blank=True, verbose_name=_('surname'))
