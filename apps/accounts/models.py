from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True, blank=True, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='profilepics', null=True, blank=True, verbose_name="Profile Picture")