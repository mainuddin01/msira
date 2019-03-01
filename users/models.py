from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username