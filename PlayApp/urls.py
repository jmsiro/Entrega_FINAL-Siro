from django.urls import path
from PlayApp import views

urlpatterns = [
    path("", views.inicio, name = "Inicio"),
    # path("view/", views.primer_view),
    path("usuario/", views.usuario, name = "Usuario"),
    path("usuario_form/", views.usuario_form, name = "Usuario Form"),
    path("publicaciones/", views.publicaciones, name = "Publicaciones"),
    path("publicaciones_form/", views.publicaciones_form, name = "Publicaciones Form"),
    path("about/", views.sobre_nosotros, name = "Sobre Nosotros"),

]
