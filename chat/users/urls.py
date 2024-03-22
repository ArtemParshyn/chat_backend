from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("register/", views.register, name="register"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
