import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from PlayApp.forms import *
from PlayApp.models import *
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# from django.urls import reverse_lazy
# Create your views here.

def primer_view(request):
    return render(request, "PlayApp/T01-view.html")

def inicio(request):
    publis = Publicacion.objects.all().order_by('-fecha') [0:3]           
    return render(request, "PlayApp/T02-inicio.html", {"publis": publis})
    

def usuario(request):
    return render(request, "PlayApp/T03-usuario.html")

def usuario_form(request):
    contexto = {}
    
    if request.POST:
        formulario = UsuarioForm(request.POST)
        
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
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            # usuario = form.cleaned_data.get('username')
            # contra = form.cleaned_data.get('password')

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return render(request, "PlayApp/T02-inicio.html", {"mensaje":f"Hola {user.get_username()}"})
            else:
                return render(request, "PlayApp/T02-inicio.html", {"mensaje":"el usuario y/o la contraseña son incorrectos"})
        else:
            return render(request, "PlayApp/T02-inicio.html", {"mensaje":"Error de autenticación, intente nuevamente."})
    else:
        form = AuthenticationForm()
        return render(request, "PlayApp/T03-usuario.html", {"form": form})



# def register_usuario(request):
#     if request.method == 'POST':
#         form = UsuarioForm(request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data["username"]
#             form.save()
#             return render(request,"PlayApp/T02-inicio.html", {"mensaje":f"Usuario {usuario} creado exitosamente."})
#         # else:
#         #     return render(request, "PlayApp/T02-inicio.html", {"mensaje":"Error de registro, intente nuevamente."})
#     else:
#         form = UsuarioForm()
#         return render(request,"PlayApp/T03.1-usuario_form.html", {"form":form})




def publicaciones(request):
    publis = Publicacion.objects.all().order_by('-fecha') [0:3]           
    return render(request, "PlayApp/T04-publicaciones.html", {"publis": publis})


@login_required
def publicaciones_form(request):
    if request.method == "POST":

        formulario_p = PublicacionesForm(request.POST)
        print(formulario_p)
        
        if formulario_p.is_valid:
            info_p = formulario_p.cleaned_data

            publi = Publicacion (titulo = info_p ["titulo"], subtitulo = info_p ["subtitulo"], noticia = info_p ["noticia"], fecha = info_p ["fecha"] )
        
            instancia = publi.save(commit=False)
            instancia.autor = request.Usuario
            instancia.save()
           

            return render(request, "PlayApp/T02-inicio.html")

    else:
        formulario_p = PublicacionesForm()
        return render(request, "PlayApp/T04.1-publicaciones_form.html", {"formulario_p":formulario_p})

@login_required
def publicaciones_busc(request):
    return render(request, "PlayApp/T04.2-publicaciones_busc.html")

@login_required
def busqueda_publicacion(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        public = Publicacion.objects.filter(titulo__icontains=titulo)

        return render(request, "PlayApp/T04.2-publicaciones_busc.html" , {"public":public})
    else:
        public = "No enviaste datos"

    return HttpResponse(public)

def sobre_nosotros(request):
    return render(request, "PlayApp/T05-sobre_nosotros.html")


def comentarios(request):
    if request.method == "POST":

        formulario_c = ComentariosForm(request.POST)
        print(formulario_c)

        if formulario_c.is_valid:
            info_c = formulario_c.cleaned_data

            coment = Comentario (nombre = info_c ["nombre"], comentario = info_c ["comentario"], fecha = info_c ["fecha"], publicacion = info_c ["publicacion"] )

            coment.save()

            return render(request, "PlayApp/T02-inicio.html")

    else:
        formulario_c = ComentariosForm()

        return render(request, "PlayApp/T06-comentarios.html", {"formulario_c":formulario_c})

class Detalle_Publicacion(DetailView):
    model = Publicacion
    template_name = "PlayApp/T04.3-publicaciones_detalle.html"





class Crear_Comentario(LoginRequiredMixin, CreateView):
    login_url = "/PlayApp/usuario/"
    model = Comentario
    success_url = "/PlayApp/comentarios_lista/"
    template_name = "PlayApp/T06.2-comentarios_form.html"
    fields = ["nombre", "comentario"]

class Detalle_Comentario(DetailView):
    model = Comentario
    template_name = "PlayApp/T06.3-comentarios_detalle.html"
    
class Listar_Comentario(ListView):
    model = Comentario
    template_name = "PlayApp/T06.1-comentarios_lista.html"
    
class Delete_Comentario(DeleteView):
    model = Comentario
    success_url = "/PlayApp/comentarios_lista/"
    template_name = "PlayApp/T06.4-comentarios_confirm_delete.html"
    
class Update_Comentario(UpdateView):
    model = Comentario
    success_url = "/PlayApp/comentarios_lista/"
    template_name = "PlayApp/T06.2-comentarios_form.html"
    fields = ["nombre", "comentario"]


