from django.urls import path
from PlayApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name = "Inicio"),
    # path("view/", views.primer_view),
    
    path("usuario/", views.login_usuario, name = "Usuario"),
    path("usuario_form/", views.register_usuario, name = "Usuario Form"),
    path("logout/", LogoutView.as_view(template_name="PlayApp/T03.2-usuario_logout.html"), name = "Usuario Logout"),


    path("publicaciones/", views.publicaciones, name = "Publicaciones"),
    path("publicaciones_form/", views.publicaciones_form, name = "Publicaciones Form"),
    path("busqueda_publicacion/", views.busqueda_publicacion, name = "Busqueda Publicacion"),
    path("publicaciones_busc/", views.publicaciones_busc, name = "Publicaciones Busc"),
    path("publicaciones_detalle/<pk>/", views.Detalle_Publicacion.as_view(), name = "Detalle Publicaciones"),

    path("about/", views.sobre_nosotros, name = "Sobre Nosotros"),
    
    path("comentarios/", views.comentarios, name = "Comentarios"),
    path("comentarios_lista/", views.Listar_Comentario.as_view(), name = "Lista Comentarios" ),
    path("comentarios_form/", views.Crear_Comentario.as_view(), name = "Crear Comentarios" ),
    path("comentarios_detalle/<pk>/", views.Detalle_Comentario.as_view(), name = "Detalle Comentarios" ),
    path("comentarios_delete/<pk>/", views.Delete_Comentario.as_view(), name = "Delete Comentarios" ),
    path("comentarios_update/<pk>/", views.Update_Comentario.as_view(), name = "Update Comentarios" ),
]
