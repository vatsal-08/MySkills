from django.shortcuts import render
from django.views.generic.list import ListView, DetailView

from .models import *

def index(request):
    # return redirect()
    return render(request,'courses/home.html')

def about(request):
    return render(request,'courses/about.html')

class CourseList(ListView):
    model = Course


class CourseDetail(DetailView):
    model = Course