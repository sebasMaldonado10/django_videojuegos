from django import forms
from .models import Resena, VideoJuego

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class ResenaForm (forms.ModelForm):
    class Meta:
        model = Resena
        fields = [
            "usuario",
            "videojuego",
            "comentario",
        ]

class VideoJuegoForm (forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = [
            "titulo",
            "descripcion",
            "imagen",
            "fecha_de_lanzamiento",
            "categoria",
            "modo_juego",
            "modelo_negocio",
            "desarrolladora",
        ]

Usuario = get_user_model()

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]