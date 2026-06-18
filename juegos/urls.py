from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juegos/', views.juegos, name='juegos'),
    path('resenas/', views.resenas, name='resenas'),
    path('nuevaResena/', views.crearResena, name='crearResena'),
    path('editarResena/<int:id>/', views.editarResena, name='editarResena'),
    path('borrarResena/<int:id>/', views.borrarResena, name='borrarResena'),
    path('nuevoJuego/', views.crearJuego, name='crearJuego'),
    path('editarJuego/<int:id>/', views.editarJuego, name='editarJuego'),
    path('borrarJuego/<int:id>/', views.borrarJuego, name='borrarJuego'),
]