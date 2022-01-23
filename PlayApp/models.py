from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Usuario(models.Model):
#     nombre = models.CharField(max_length=40)
#     email = models.EmailField(max_length=254)
#     password1 = models.CharField(max_length=12)
#     password2 = models.CharField(max_length=12)
#     tipo = models.CharField(max_length=6, default="") 
#     USERNAME_FIELD = "nombre"
    

#     def __str__(self):
#         return f" {self.nombre} - {self.email} - {self.tipo}"
    # ver posibilidad de usar lista para elgir tipo

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=40)
    noticia = models.TextField(max_length=5000)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=False, max_length=12)

    def __str__(self):
        return f" {self.titulo} - {self.nombre} - {self.fecha}"
class Comentario(models.Model):
    nombre = models.CharField(max_length=40)
    comentario = models.TextField(max_length=300)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=False, max_length=12)
    # publicacion = models.IntegerField() Buscar que se cargue automaticamante el id de publicacion asociada al comentario.

    def __str__(self):
        return f" {self.nombre}  - {self.fecha}" #{self.publicacion}

