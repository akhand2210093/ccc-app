# registration/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission # Import Group model

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)

    def __str__(self):
        return self.username

