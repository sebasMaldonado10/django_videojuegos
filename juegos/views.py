from django.shortcuts import render
from .models import VideoJuego, Resena

def inicio(request):
    return render (request, 'juegos/index.html')

def juegos(request):
    juegos = VideoJuego.objects.all()
    return render (request, 'juegos/juegos.html', {'juegos': juegos})

def resenas(request):
    resenas = Resena.objects.all()
    return render (request, 'juegos/resenas.html', {'resenas': resenas})