from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")
    list_filter = ("is_staff", "is_active", "groups")
    ordering = ("username",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(ModoJuego)
class ModoJuegoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(ModeloNegocio)
class ModeloNegocioAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Desarrolladora)
class DesarrolladoraAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(VideoJuego)
class VideoJuegoAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "modo_juego",
        "modelo_negocio",
        "desarrolladora",
        "fecha_de_lanzamiento",
    )
    search_fields = ("titulo", "descripcion")
    list_filter = ("categoria", "modo_juego", "modelo_negocio", "desarrolladora")
    ordering = ("titulo",)


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "videojuego", "comentario")
    search_fields = ("usuario__username", "videojuego__titulo", "comentario")
    list_filter = ("videojuego", "usuario")
    ordering = ("videojuego",)
