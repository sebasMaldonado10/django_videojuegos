from django.shortcuts import render, redirect, get_object_or_404
from .models import VideoJuego, Resena, Categoria
from .forms import ResenaForm, VideoJuegoForm, RegistroForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth import login


def inicio(request):
    # 1. Agregados recientemente: Ordenamos por ID de forma descendente y tomamos 5
    recientes = VideoJuego.objects.filter(activo=True).order_by('-id')[:5]
    
    # 2. Juegos destacados: Contamos cuántas reseñas tiene cada juego.
    # CORRECCIÓN: Cambié 'resenas' por 'resena' (o podés usar 'resena_set' si da error)
    destacados = VideoJuego.objects.filter(activo=True).annotate(
        num_resenas=Count('resenas') 
    ).order_by('-num_resenas')[:5]
    
    # 3. Categorías para la barra horizontal
    categorias = Categoria.objects.all()

    # CORRECCIÓN: Saqué el `:` que estaba adentro de 'juegos_destacados:'
    context = {
        'juegos_recientes': recientes,
        'juegos_destacados': destacados, 
        'categorias': categorias
    }
    return render(request, 'juegos/index.html', context)

def detalle_juego(request, id):
    juego = get_object_or_404(VideoJuego, id=id)
    return render(request, 'juegos/detalle_juego.html', {'juego': juego})

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {"form": form})


##### CRUD modelo videojuego #####

# Create
@permission_required('juegos.add_videojuego', raise_exception=True)
def crearJuego(request):
    if request.method == 'POST':
        form = VideoJuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('juegos')
    else:
        form = VideoJuegoForm()
    return render(request, 'juegos/crear_juego.html', {'form': form})

# Read
@login_required
def juegos(request):
    juegos = VideoJuego.objects.all()
    return render(request, 'juegos/juegos.html', {'juegos': juegos})

# Update
@permission_required('juegos.change_videojuego', raise_exception=True)
def editarJuego(request, id):
    juego = get_object_or_404(VideoJuego, id=id)

    if request.method == 'POST':
        form = VideoJuegoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('juegos')
    else:
        form = VideoJuegoForm(instance=juego)
    return render(request, 'juegos/editar_juego.html', {'form': form})

# Delete
@permission_required('juegos.delete_videojuego', raise_exception=True)
def borrarJuego(request, id):
    juego = get_object_or_404(VideoJuego, id=id)

    if request.method == 'POST':
        juego.activo = False
        juego.save()
        return redirect('juegos')
    return render(request, 'juegos/borrar_juego.html', {'juego': juego})


##### CRUD modelo resena #####

# Create
@permission_required('juegos.add_resena', raise_exception=True)
def crearResena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resenas')
    else:
        form = ResenaForm()
    return render(request, 'juegos/crear_resena.html', {'form': form})

# Read
@login_required
def resenas(request):
    resenas = Resena.objects.all()
    return render(request, 'juegos/resenas.html', {'resenas': resenas})

# Update
@permission_required('juegos.change_resena', raise_exception=True)
def editarResena(request, id):
    resena = get_object_or_404(Resena, id=id)

    if request.method == 'POST':
        form = ResenaForm(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            return redirect('resenas')
    else:
        form = ResenaForm(instance=resena)
    return render(request, 'juegos/editar_resena.html', {'form': form})

# Delete
@permission_required('juegos.delete_resena', raise_exception=True)
def borrarResena(request, id):
    resena = get_object_or_404(Resena, id=id)

    if request.method == 'POST':
        resena.activo = False
        resena.save()
        return redirect('resenas')
    return render(request, 'juegos/borrar_resena.html', {'resena': resena})