from django.urls import path, include
from accounts.views import * 
urlpatterns = [
    path('signup/', SignUpView.as_view(template_name='accounts/signup.html'), name='signup'),
    path('login/', LoggingView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
]
