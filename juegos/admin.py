from django.contrib import admin
# Register your models here.

from .models import (
    UsuarioPersonalizado,
    Categoria,
    ModoJuego,
    ModeloNegocio,
    Desarrolladora,
    VideoJuego,
    Resena
)

admin.site.register(UsuarioPersonalizado)
admin.site.register(Categoria)
admin.site.register(ModoJuego)
admin.site.register(ModeloNegocio)
admin.site.register(Desarrolladora)
admin.site.register(VideoJuego)
admin.site.register(Resena)


