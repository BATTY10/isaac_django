from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('read_post/<str:pk>/', views.read_post, name='read_post'),
    path('update_post/<str:pk>/', views.update_post, name='update_post'),
    path('create_post', views.create_post, name='create_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post')
]
