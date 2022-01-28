from ast import AugStore
from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Manager_Usuario(BaseUserManager):
    def create_user(self, username, nombre, apellido, email, tipo, password=None):
        if not username:
            raise ValueError("Debes tener un nombre de usuario")
        if not nombre:
            raise ValueError("Debes tener un nombre")
        if not apellido:
            raise ValueError("Debes tener un apellido")    
        if not email:
            raise ValueError("Debes tener un email")
        if not tipo:
            raise ValueError("Debes tener un tipo de usuario")
        usuario = self.model(
            username
    =username
    ,
            nombre=nombre,
            apellido=apellido,
            email=self.normalize_email(email),
            tipo=tipo
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self,username, nombre, apellido, email, tipo, password):
        usuario = self.create_user(
            username
    =username
    ,
            nombre=nombre,
            apellido=apellido,
            email=self.normalize_email(email),
            tipo=tipo,
            password=password
        )
        usuario.is_admin = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, verbose_name="email", unique=True)
    # password1 = models.CharField(max_length=12)
    # password2 = models.CharField(max_length=12)
    tipo = models.CharField(max_length=6, default="")
    date_joined = models.DateTimeField(verbose_name="Fecha de Registro", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Ultima Conexión", auto_now=True) 
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = "username" #Buscar si se puede poner que sea nombre de usuario o email, que de la opcion de loguear ocn cualquiera de los dos.
    REQUIRED_FIELDS = ["nombre", "apellido", "email", "tipo"]
    objects = Manager_Usuario()
    

    def __str__(self):
        return f" {self.nombre} - {self.email} - {self.tipo}"
        
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    # ver posibilidad de usar lista para elgir tipo

class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Usuario, default=None, on_delete=models.CASCADE)
    subtitulo = models.CharField(max_length=100)
    noticia = models.TextField(max_length=5000)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=False, max_length=12)
    id_autor = models.CharField(max_length=6)

    def __str__(self):
        return f" {self.titulo} - {self.autor} - {self.fecha}"



class Comentario(models.Model):
    nombre = models.CharField(max_length=40)
    comentario = models.TextField(max_length=300)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=False, max_length=12)
    # publicacion = models.IntegerField() Buscar que se cargue automaticamante el id de publicacion asociada al comentario.

    def __str__(self):
        return f" {self.nombre}  - {self.fecha}" #{self.publicacion}

