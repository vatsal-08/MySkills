from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myskills.middleware import AdminSuperuserMiddleware

urlpatterns = [
    path('',include('courses.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    path('admin/', AdminSuperuserMiddleware(admin.site.urls)),
] + urlpatterns
