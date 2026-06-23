from .models import Categoria

def datos_globales(request):
    categorias = Categoria.objects.all()

    return {
        'categorias': categorias,
        'nombre_sitio': 'The Goat Games',
        'anio_actual': 2026,
    }