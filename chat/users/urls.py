from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/', views.ApiUserView.as_view()),
    path('api/reg/', views.register, name='reg'),
    path('api/auth/', views.login, name='auth'),
    path('api/logout/', views.logout, name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
