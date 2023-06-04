from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_verified = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
