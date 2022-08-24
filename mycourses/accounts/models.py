from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.TextField(null=False, blank=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, blank=True)
    last_logout = models.DateTimeField(null=True,blank=True)

    USERNAME_FIELD=['email']


    # def authenticate(self,username=None,password=None):
    #     if '@' in username:
    #         kwargs={'email':username}
    #     else:
    #         kwargs={'username':username}
    #     try:
    #         user = 