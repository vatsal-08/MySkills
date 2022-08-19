from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# class CustomUser(User):
#     email
#     username
#     date_joined
#     last_login
