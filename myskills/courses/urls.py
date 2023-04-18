from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',index,name='home'),
    path('courses/',CourseList.as_view(),name='courses'),
    path('courses/<int:pk>/',CourseDetail.as_view(),name='course'),
    path('about-me/',views.about,name='about-me'),
]