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
admin.site.register(Categoria)
admin.site.register(ModoJuego)
admin.site.register(ModeloNegocio)
admin.site.register(Desarrolladora)

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin (admin.ModelAdmin):
    list_display = (
        "id",
        "password",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "telefono",
        "foto_perfil",
    )

@admin.register(VideoJuego)
class VideoJuegoAdmin (admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "descripcion",
        "imagen",
        "fecha_de_lanzamiento",
        "categoria",
        "modo_juego",
        "modelo_negocio",
        "desarrolladora",
        "activo",
    )
    list_filter = ("titulo","categoria",)
    search_fields = ("titulo",)

@admin.register(Resena)
class ResenaAdmin (admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "videojuego",
        "fecha",
        "comentario",
        "activo",
    )
    list_filter = ("videojuego",)
    search_fields = ("videojuego",)