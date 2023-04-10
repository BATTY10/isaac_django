from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('read_post/<str:pk>/', views.read_post, name='read_post'),
]
