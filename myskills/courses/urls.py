from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',index,name='home'),
    path('courses/',CourseList.as_view(),name='courses'),
    path('courses/create/',create_view,name='create-view'),
    path('courses/<int:pk>/',CourseDetail.as_view(),name='detail'),
    path('courses/<int:pk>/update/',views.update_course,name='update'),
    path('courses/<int:pk>/delete/',views.delete_course,name='delete'),
    path('about-me/',views.about,name='about-me'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)