from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',index,name='home'),
    path('courses/',views.list_view,name='courses'),
    path('courses/create/',views.create_view,name='create-view'),
    path('courses/search/',views.search_view,name='search'),
    path('courses/search_results/',views.search_results,name='search_result'),
    path('courses/<int:pk>/',views.course_detail,name='detail'),
    path('courses/<int:pk>/update/',views.update_course,name='update'),
    path('courses/<int:pk>/delete/',views.delete_course,name='delete'),
    path('about-me/',views.about,name='about-me'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)