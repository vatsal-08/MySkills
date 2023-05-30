from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return super().user.username