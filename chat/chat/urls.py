from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace='api')),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/auth/', AuthorApiView.as_view()),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/message/', include('djoser.urls')),
    path("users/", include('users.urls', namespace='users')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
]
