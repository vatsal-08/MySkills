from django.db import models
from accounts.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    img = models.ImageField(upload_to="img/")
    description = models.TextField(max_length=150)
    added = models.DateTimeField(auto_now_add=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    pdf_file = models.FileField(
        storage=FileSystemStorage(location=settings.MEDIA_ROOT),
        upload_to="pdf/",
        default=None)

    class Meta:
        ordering = ['-last_modified']

    def __str__(self):
        return self.name
    
    def short_description(self):
        if len(self.description) > 50:
            return self.description[:50] + '...'
        return self.description