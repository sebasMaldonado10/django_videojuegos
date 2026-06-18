from django.shortcuts import render, redirect
from .models import VideoJuego, Resena
from .forms import ResenaForm

def inicio(request):
    return render (request, 'juegos/index.html')

###CRUD modelo videojuego
def juegos(request):
    juegos = VideoJuego.objects.all()
    return render (request, 'juegos/juegos.html', {'juegos': juegos})

###CRUD modelo resena

#Create
"""
def CrearResena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resena')
    return render (request, 'template', {'': })
"""

#Read
def resenas(request):
    resenas = Resena.objects.all()
    return render (request, 'juegos/resenas.html', {'resenas': resenas})