from django.conf import settings
from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static

# app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='detail'),
    path('about-me/', views.about, name='about-me'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
