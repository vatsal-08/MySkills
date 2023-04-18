from django.shortcuts import render
from django.views.generic import  ListView,DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

def index(request):
    return render(request,'courses/home.html')

def about(request):
    return render(request,'courses/about-me.html')

class CourseList(ListView):
    model = Course
    template_name="courses/home.html"
    context_object_name='courses'

class CourseDetail(LoginRequiredMixin,DetailView):
    model = Course
    template_name="courses/detail.html"
    context_object_name='course'

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "course/update.html"
