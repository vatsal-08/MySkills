from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Course


class User(AbstractUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=40, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date joined")
    last_login = models.DateTimeField(verbose_name="Date joined")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    courses_taken = models.ManyToManyField(Course)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self) -> str:
        return self.email
