from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',index,name='home'),
    path('courses/',CourseList.as_view(),name='courses'),
    path('courses/<int:pk>/',CourseList.as_view(),name='courses'),
    path('about-me/',views.about,name='courses'),
]