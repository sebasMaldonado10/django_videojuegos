from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juegos/', views.juegos, name='juegos'),
    path('resenas/', views.resenas, name='resenas'),
]