from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class CustomUser(User):
    email = models.EmailField(max_length=255, unique=True)
    username = models.TextField(null=False, blank=True)
    date_joined = models.DateTimeField(auto_now=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, blank=True)
