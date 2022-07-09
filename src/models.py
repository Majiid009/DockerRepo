from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False,)
    username = models.CharField(unique=True, blank=False, max_length=30)
    subscribed = models.BooleanField(default=False)
