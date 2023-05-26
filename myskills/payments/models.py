from django.db import models
from accounts.models import *
from courses.models import *

class Transactions(models.Model):
    amount=models.IntegerField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)