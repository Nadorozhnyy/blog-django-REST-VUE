from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("email"), blank=False, null=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
