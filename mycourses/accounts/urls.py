from django.conf import settings
from django.urls import path
from .views import SignupView, LoginView
from . import views
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views


# app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', SignupView.as_view(template_name='accounts/signup.html'), name='signup'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
