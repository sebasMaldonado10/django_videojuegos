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