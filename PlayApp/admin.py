from django.contrib import admin
from PlayApp.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(Usuario)

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("autor", "titulo", "subtitulo","imagen", "fecha_publi", "fecha_actualizacion")
    search_fields = ("autor", "titulo", "fecha_publi")
    readonly_fields = ("autor", "fecha_publi", "fecha_actualizacion") #No se pueden cambiar manualmente

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Publicacion, PublicacionAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "publicacion", "comentario","fecha")
    search_fields = ("nombre", "publicacion")
    readonly_fields = ("publicacion", "fecha") #No se pueden cambiar manualmente

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Comentario, ComentarioAdmin)

class UsuarioAdmin(UserAdmin): #Modelo de administrador de usuarios customizado
    list_display = ("username", "nombre", "apellido", "email","tipo", "date_joined", "last_login", "is_admin", "is_active")
    search_fields = ("username", "email")
    readonly_fields = ("date_joined", "last_login") #No se pueden cambiar manualmente

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Usuario, UsuarioAdmin)
