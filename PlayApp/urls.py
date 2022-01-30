from django.urls import path
from PlayApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.inicio, name = "Inicio"),
    
    
    path("usuario/", views.login_usuario, name = "Usuario"),
    path("usuario_form/", views.usuario_form, name = "Usuario Form"),
    path("logout/", views.logout_usuario, name = "Usuario Logout"),
    path("usuario_update/", views.update_usuario, name = "Usuario Update" ),

    path("publicaciones/", views.publicaciones, name = "Publicaciones"),
    path("publicaciones_form/", views.publicaciones_form, name = "Publicaciones Form"),
    path("busqueda_publicacion/", views.busqueda_publicacion, name = "Busqueda Publicacion"),
    path("publicaciones_busc/", views.publicaciones_busc, name = "Publicaciones Busc"),
    path("<slug>/", views.detalle_publicacion, name = "Detalle Publicaciones"),
    path("<slug>/publicaciones_update/", views.update_publicacion, name = "Update Publicaciones"),
    path("about/", views.sobre_nosotros, name = "Sobre Nosotros"),
    
    path("comentarios/", views.comentarios, name = "Comentarios"),
    path("comentarios_lista/", views.Listar_Comentario.as_view(), name = "Lista Comentarios" ),
    path("comentarios_form/", views.Crear_Comentario.as_view(), name = "Crear Comentarios" ),
    path("comentarios_detalle/<pk>/", views.Detalle_Comentario.as_view(), name = "Detalle Comentarios" ),
    path("comentarios_delete/<pk>/", views.Delete_Comentario.as_view(), name = "Delete Comentarios" ),
    path("comentarios_update/<pk>/", views.Update_Comentario.as_view(), name = "Update Comentarios" ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)