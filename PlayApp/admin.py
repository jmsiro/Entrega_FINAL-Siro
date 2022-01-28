from django.contrib import admin
from PlayApp.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(Usuario)

admin.site.register(Publicacion)

admin.site.register(Comentario)



class UsuarioAdmin(UserAdmin):
    list_display = ("username", "nombre", "apellido", "email","tipo", "date_joined", "last_login", "is_admin", "is_active", "is_staff")
    search_fields = ("username", "email")
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Usuario, UsuarioAdmin)
