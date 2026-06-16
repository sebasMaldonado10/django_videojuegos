from django.shortcuts import render
from .models import VideoJuego

def inicio(request):
    return render (request, 'juegos/index.html')

def juegos(request):
    juegos = VideoJuego.objects.all()
    return render (request, 'juegos/juegos.html', {'juegos': juegos})
