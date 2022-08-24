from webbrowser import get
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from courses.models import *


def index(request):
    return redirect('courses')


class CourseList(ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'


class CourseDetail(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'


def about(request):
    return render(request, 'courses/about-me.html')
