# Importaciones
from django.shortcuts import render, redirect, get_object_or_404
from PlayApp.forms import *
from PlayApp.models import *
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import os

# padre
def primer_view(request):
    return render(request, "PlayApp/T01-view.html")

# inicio
def inicio(request):
    publis = Publicacion.objects.all().order_by('-fecha_publi') [0:3]           
    return render(request, "PlayApp/T02-inicio.html", {"publis": publis})
    
# Usuario
def usuario(request):
    return render(request, "PlayApp/T03-usuario.html")

def usuario_form(request):
    contexto = {}
    
    if request.POST:
        formulario = UsuarioForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            nombre_usuario = formulario.cleaned_data.get("username")
            clave = formulario.cleaned_data.get("password1")

            usuario = authenticate(username = nombre_usuario, password=clave)
            login(request, usuario)
            return render(request,"PlayApp/T02-inicio.html", {"mensaje":f"Hola {usuario.get_username()}, creaste exitosamente tu usuario!"})
        else:
            contexto["usuario_formulario"] = formulario
            
    else:
        formulario = UsuarioForm()
        contexto ["usuario_formulario"] = formulario

    return render(request, "PlayApp/T03.1-usuario_form.html", contexto)


def login_usuario(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = authenticate(username=data["username"], password=data["password"])

            if usuario is not None:
                login(request, usuario)
                return render(request, "PlayApp/T02-inicio.html", {"mensaje":f"Hola {usuario.get_username()}"})
            else:
                return render(request, "PlayApp/T02-inicio.html", {"mensaje":"el usuario y/o la contraseña son incorrectos"})
        else:
            return render(request, "PlayApp/T02-inicio.html", {"mensaje":"Error de autenticación, intente nuevamente."})
    else:
        formulario = AuthenticationForm()
        return render(request, "PlayApp/T03-usuario.html", {"formulario": formulario})

@login_required
def logout_usuario(request):
    logout(request)
    return render(request,"PlayApp/T02-inicio.html", {"mensaje":f"Adios, cerraste sesión exitosamente!"})

@login_required
def update_usuario(request):
    contexto = {}
    
    if request.POST:
        # if  request.user.avatar:
        #     os.remove(request.user.avatar.path)

        formulario = UsuarioUpdateForm(request.POST, request.FILES, instance=request.user)  
        
        if formulario.is_valid():
            
            formulario.save()
            usuario = request.user
            return render(request, "PlayApp/T02-inicio.html", {"mensaje":f"Modificaste exitosamente tu usuario: {usuario.get_username()}"})
    else:
        formulario = UsuarioUpdateForm(
            initial= {
                "username": request.user.username,
                "nombre": request.user.nombre,
                "apellido": request.user.apellido,
                "email": request.user.email,
                "avatar": request.user.avatar,
                "tipo": request.user.tipo        
            }
        )  
    contexto ["usuario_detalle"] = formulario
    return render(request, "PlayApp/T03.2-usuario_detalle.html", contexto)


def actividad_usuario(request):
    usuario = Usuario.objects.filter(username=request.user.username).first()
    publis = Publicacion.objects.filter(autor=usuario).order_by('-fecha_publi')
    coments = Comentario.objects.filter(nombre=usuario).order_by('-fecha')

    contexto = {"publis":publis, "coments":coments}

    return render(request, "PlayApp/T03.3-usuario_actividad.html", contexto)





# Publicaciones
def publicaciones(request):
    publis = Publicacion.objects.all().order_by('-fecha_publi') [0:3]           
    return render(request, "PlayApp/T04-publicaciones.html", {"publis": publis})


@login_required
def publicaciones_form(request):
    contexto = {}
    usuario = request.user
    if usuario.tipo == "LECTOR":
        return render(request, "PlayApp/T02-inicio.html", {"mensaje":f"Su usuario: {usuario.get_username()}, no tiene permisos para publicar."})

    if request.method == "POST":
        formulario_p = PublicacionesForm(request.POST, request.FILES) 

        if formulario_p.is_valid():
            instancia = formulario_p.save(commit=False)

            autor = Usuario.objects.filter(username=usuario.username).first()

            instancia.autor = autor
            instancia.save()

            contexto["formulario_p"] = formulario_p
            
            return redirect("Inicio")

    else:
        formulario_p = PublicacionesForm()
        contexto["formulario_p"] = formulario_p
    return render(request, "PlayApp/T04.1-publicaciones_form.html", contexto)
    
@login_required
def update_publicacion(request, pk):
    contexto = {}
    usuario = request.user
    publicacion = get_object_or_404(Publicacion, pk=pk)

    if publicacion.autor != usuario or usuario.tipo != "AUTOR":
        contexto['mensaje_error'] = "¡Usted no posee autorización para editar esta publicación!"
        return render(request, "PlayApp/T02-inicio.html", contexto)

    if request.POST:
        formulario_p = UpdatePublicacionForm(request.POST , request.FILES, instance=publicacion) #ver si hace falta un "or None" en .post y .files
        if formulario_p.is_valid():
            instancia = formulario_p.save(commit=False)
            instancia.save()
            contexto['mensaje_de_confirmacion'] = "¡Noticia modificada exitosamente!"
            publicacion = instancia

    formulario_p = UpdatePublicacionForm(
            initial = {
                    "titulo": publicacion.titulo,
                    "subtitulo": publicacion.subtitulo,
                    "noticia": publicacion.noticia,
                    "imagen": publicacion.imagen,
            }
        )

    contexto['formulario_p'] = formulario_p
    return render(request, 'PlayApp/T04.4-publicaciones_update.html', contexto)


@login_required
def publicaciones_busc(request):
    return render(request, "PlayApp/T04.2-publicaciones_busc.html")

@login_required
def busqueda_publicacion(request):
    contexto={}
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        public = Publicacion.objects.filter(titulo__icontains=titulo).order_by("-fecha_publi")

        return render(request, "PlayApp/T04.2-publicaciones_busc.html" , {"public":public})
    else:
        contexto['mensaje'] = "¡No enviaste datos!"

        return render(request, "PlayApp/T04-publicaciones.html", contexto)

@login_required
def detalle_publicacion(request, pk):

    contexto = {}

    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    comentarios = publicacion.comentarios.all().order_by("-fecha")[0:3]
    
    contexto['publicacion'] = publicacion
    contexto['comentarios'] = comentarios

    
    return render(request, 'PlayApp/T04.3-publicaciones_detalle.html', contexto)




# Sobre Nosotros
def sobre_nosotros(request):
    return render(request, "PlayApp/T05-sobre_nosotros.html")






# Comentarios
def comentarios_form(request, pk):
    contexto = {}
    usuario = request.user
    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    if request.method == "POST":
        formulario_c =ComentariosForm(request.POST) 

        if formulario_c.is_valid():
            instancia = formulario_c.save(commit=False)

            autor = Usuario.objects.filter(username=usuario.username).first()
            
            instancia.publicacion = publicacion
            instancia.nombre = autor
            instancia.save()

            contexto["formulario_c"] = formulario_c

            return redirect("Inicio")

    else:
        formulario_c = ComentariosForm()
        contexto["formulario_c"] = formulario_c
    return render(request, "PlayApp/T06.2-comentarios_form.html", contexto)


def comentarios_lista(request, pk):
    contexto = {}
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = publicacion.comentarios.all().order_by("-fecha")
    
    contexto['publicacion'] = publicacion
    contexto['comentarios'] = comentarios
    
    return render(request, 'PlayApp/T06.1-comentarios_lista.html', contexto)


class Delete_Comentario(DeleteView):
    model = Comentario
    success_url = "/PlayApp/publicaciones/"
    template_name = "PlayApp/T06.3-comentarios_confirm_delete.html"


class Update_Comentario(UpdateView):
    model = Comentario
    form_class = ComentariosForm
    success_url = "/PlayApp/publicaciones/"
    template_name = "PlayApp/T06.2-comentarios_form.html"

