from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('', admin.site.urls),
]

urlpatterns = [
    path('', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', include(admin_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
