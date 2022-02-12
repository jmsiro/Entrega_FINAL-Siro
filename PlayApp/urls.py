
from django.urls import path
from PlayApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.inicio, name = "Inicio"),
    
    path("usuario/", views.login_usuario, name = "Usuario"),
    path("usuario_form/", views.usuario_form, name = "Usuario Form"),
    path("logout/", views.logout_usuario, name = "Usuario Logout"),
    path("usuario_update/", views.update_usuario, name = "Usuario Update" ),
    
    # Reseteo contraseña - (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_cambiar/ok/', auth_views.PasswordChangeDoneView.as_view(template_name='Password/password_cambiar_ok.html'), name='password_change_done'),
    
    path('password_cambiar/', auth_views.PasswordChangeView.as_view(template_name='Password/password_cambiar.html'), 
        name='password_change'),

    path('password_reseteo/listo/', auth_views.PasswordResetCompleteView.as_view(template_name='Password/password_reseteo_listo.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reseteo/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reseteo/ok/', auth_views.PasswordResetCompleteView.as_view(template_name='Password/password_reseteo_ok.html'),name='password_reset_complete'),
    
    #Publicaciones
    path("publicaciones_detalle/<int:pk>/comentarios_form/", views.comentarios_form, name = "Crear Comentarios" ),
    path("publicaciones_detalle/<int:pk>/comentarios_lista/", views.comentarios_lista, name = "Lista Comentarios" ),
    path("comentarios_delete/<pk>/", views.Delete_Comentario.as_view(), name = "Delete Comentarios" ),
    path("comentarios_update/<pk>/", views.Update_Comentario.as_view(), name = "Update Comentarios" ),

    path("about/", views.sobre_nosotros, name = "Sobre Nosotros"),

    path("publicaciones/", views.publicaciones, name = "Publicaciones"),
    path("publicaciones_form/", views.publicaciones_form, name = "Publicaciones Form"),
    path("busqueda_publicacion/", views.busqueda_publicacion, name = "Busqueda Publicacion"),
    path("publicaciones_busc/", views.publicaciones_busc, name = "Publicaciones Busc"),
    path("publicaciones_detalle/<int:pk>/", views.detalle_publicacion, name = "Detalle Publicaciones"),
    path("<int:pk>/publicaciones_update/", views.update_publicacion, name = "Update Publicaciones"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)