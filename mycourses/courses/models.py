from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    img = models.ImageField(upload_to="img/")
    description = models.TextField()
    added = models.DateTimeField(auto_now_add=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ['-last_modified']

    def __str__(self):
        return self.name
