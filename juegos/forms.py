from django import forms
from .models import Resena, VideoJuego

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