from django.shortcuts import render
from django.views.generic.list import ListView, DetailView

from .models import *

def index(request):
    return render(request,'courses/home.html')

class CourseList(ListView):
    model = Course

def about(request):
    return render(request,'courses/about.html')

class CourseDetail(DetailView):
    model = Course