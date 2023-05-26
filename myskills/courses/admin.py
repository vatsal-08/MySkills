from django.contrib import admin
from .models import Course
class CourseAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Course._meta.fields]
admin.site.register(Course,CourseAdmin)