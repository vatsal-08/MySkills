from django.shortcuts import render
from django.views.generic import  ListView,DetailView

from .models import *

def index(request):
    # return redirect()
    return render(request,'courses/home.html')

def about(request):
    return render(request,'courses/about-me.html')

class CourseList(ListView):
    model = Course
    template_name="courses/home.html"

class CourseDetail(DetailView):
    model = Course
    template_name="courses/"