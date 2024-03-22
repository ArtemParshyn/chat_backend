from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace='api')),
    path("users/", include('users.urls', namespace='users')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
