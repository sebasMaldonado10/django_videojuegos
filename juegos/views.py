from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoJuego, Resena
from .forms import ResenaForm, VideoJuegoForm

def inicio(request):
    return render (request, 'juegos/index.html')

##### CRUD modelo videojuego #####

#Create
def crearJuego(request):
    if request.method == 'POST':
        form = VideoJuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('juegos')
    else:
        form = VideoJuegoForm()
    return render (request, 'juegos/crear_juego.html', {'form': form})

#Read
def juegos(request):
    juegos = VideoJuego.objects.all()
    return render (request, 'juegos/juegos.html', {'juegos': juegos})

#Update
def editarJuego(request, id):
    juego = get_object_or_404(VideoJuego, id=id)

    if request.method == 'POST':
        form = VideoJuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('juegos')
    else:
        form = VideoJuegoForm(instance=juego)
    return render (request, 'juegos/editar_juego.html', {'form': form})

#Delete
def borrarJuego(request, id):
    juego = get_object_or_404(VideoJuego, id=id)

    if request.method == 'POST':
        juego.activo = False
        juego.save()
        return redirect('juegos')
    return render (request, 'juegos/borrar_juego.html', {'juego': juego})

##### CRUD modelo resena #####

#Create
def crearResena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resenas')
    else:
        form = ResenaForm()
    return render (request, 'juegos/crear_resena.html', {'form': form})

#Read
def resenas(request):
    resenas = Resena.objects.all()
    return render (request, 'juegos/resenas.html', {'resenas': resenas})

#Update
def editarResena(request, id):
    resena = get_object_or_404(Resena, id=id)

    if request.method == 'POST':
        form = ResenaForm(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            return redirect('resenas')
    else:
        form = ResenaForm(instance=resena)
    return render (request, 'juegos/editar_resena.html', {'form': form})

#Delete
def borrarResena(request, id):
    resena = get_object_or_404(Resena, id=id)

    if request.method == 'POST':
        resena.activo = False
        resena.save()
        return redirect('resenas')
    return render (request, 'juegos/borrar_resena.html', {'resena': resena})