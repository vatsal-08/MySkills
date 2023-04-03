from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *

def index(request):
    return render(request,'courses/home.html')

class CourseList(ListView):
    model = Course

def about(request):
    pass