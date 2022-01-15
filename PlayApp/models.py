from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    clave = models.CharField(min_length=8 ,max_length=12)
    