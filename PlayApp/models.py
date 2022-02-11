from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.dispatch import receiver

from ckeditor.fields import RichTextField


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
            username=username,
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
            username=username,
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

    TIPO_USUARIO = [
        ("ADMIN","Admin"),
        ("LECTOR","Lector"),
        ("AUTOR","Autor"),
    ]
    username = models.CharField(max_length=40, unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=254, verbose_name="email", unique=True)
    # password1 = models.CharField(max_length=12)
    # password2 = models.CharField(max_length=12)
    tipo = models.CharField(max_length=6, choices=TIPO_USUARIO, default="LECTOR")
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
        return f"{self.username}  ({self.nombre}  {self.apellido} - {self.tipo})"
        
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    # ver posibilidad de usar lista para elgir tipo




def upload_location(instance, archivo):
    path_archivo= 'PlayApp/{id_autor}/{titulo}-{archivo}'.format(
        id_autor=str(instance.autor.id), titulo=str(instance.titulo), archivo=archivo
    )
    return path_archivo
class Publicacion(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subtitulo = models.CharField(max_length=100, null=False, blank=False)
    noticia = RichTextField(max_length=5000)
    imagen = models.ImageField(upload_to=upload_location, null=False, blank=False)
    fecha_publi= models.DateTimeField(auto_now_add=True, verbose_name="fecha publicación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="fecha actualización")
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return f" {self.titulo} - {self.autor}"

@receiver(post_delete, sender=Publicacion)
def submission_delete(sender, instance, **kargs):
    instance.imagen.delete(False)


def pre_save_publicacion_reciver(sender, instance, *arg, **kargs):
    if not instance.slug:
        instance.slug= slugify(instance.autor.username + "-" + instance.titulo)

pre_save.connect(pre_save_publicacion_reciver, sender=Publicacion)





class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name="comentarios", on_delete=models.CASCADE, default="")
    nombre = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.publicacion} - {self.nombre} - {self.fecha} "
