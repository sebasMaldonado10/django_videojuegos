from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Aqui iran los modelos y el user personalizado

class UsuarioPersonalizado(AbstractUser):
    # Cada campo debe permitir nulos o valores por defecto
    telefono = models.IntegerField(null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil', null=True, blank=True)

    def __str__(self):
        return f"custom {self.telefono}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"categoria {self.nombre}"

class ModoJuego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"modo de juego {self.nombre}"
    
class ModeloNegocio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"modelo de negocio {self.nombre}"
    
class Desarrolladora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"desarrolladora {self.nombre}"

class VideoJuego(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='videojuegos/', null=True, blank=True)
    fecha_de_lanzamiento = models.DateField(null=True, blank=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='videojuegos'
    )
    modo_juego = models.ForeignKey(
        ModoJuego,
        on_delete=models.CASCADE,
        related_name='videojuegos'
    )
    modelo_negocio = models.ForeignKey(
        ModeloNegocio,
        on_delete=models.CASCADE,
        related_name='videojuegos'
    )
    desarrolladora = models.ForeignKey(
        Desarrolladora,
        on_delete=models.CASCADE,
        related_name='videojuegos'
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"videojuego {self.titulo}"


class Resena(models.Model):
    usuario = models.ForeignKey(
        UsuarioPersonalizado,
        on_delete= models.CASCADE,
        related_name= 'resenas'
    )
    videojuego = models.ForeignKey(
        VideoJuego,
        on_delete=models.CASCADE,
        related_name='resenas'
    )
    fecha = models.DateField(auto_now_add=True)
    comentario = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"resena {self.usuario.username}"

