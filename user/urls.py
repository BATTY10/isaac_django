from django.urls import path
from . import views
from django.contrib.auth import views as user_auth_views


urlpatterns = [
    path('', views.register, name='register'),
    path('login/', user_auth_views.LoginView.as_view(template_name='user/login.html'), name='login')
]
