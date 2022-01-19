from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PlayApp.forms import *
from PlayApp.models import *
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.urls import reverse_lazy
# Create your views here.

def primer_view(request):
    return render(request, "PlayApp/T01-view.html")

def inicio(request):
    
    return render(request, "PlayApp/T02-inicio.html")

def usuario(request):
    return render(request, "PlayApp/T03-usuario.html")

def usuario_form(request):
    if request.method == "POST":

        formulario = UsuarioForm(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            info = formulario.cleaned_data

            user = Usuario (nombre = info ["nombre"], email = info ["email"], clave = info ["clave"], tipo = info ["tipo"] )
        
            user.save()

            return render(request, "PlayApp/T02-inicio.html")

    else:
        formulario = UsuarioForm()
        return render(request, "PlayApp/T03.1-usuario_form.html", {"formulario":formulario})


def publicaciones(request):
    return render(request, "PlayApp/T04-publicaciones.html")

def publicaciones_form(request):
    if request.method == "POST":

        formulario_p = PublicacionesForm(request.POST)
        print(formulario_p)
        
        if formulario_p.is_valid:
            info_p = formulario_p.cleaned_data

            publi = Publicacion (titulo = info_p ["titulo"], nombre = info_p ["nombre"], noticia = info_p ["noticia"], fecha = info_p ["fecha"] )
        
            publi.save()

            return render(request, "PlayApp/T02-inicio.html")

    else:
        formulario_p = PublicacionesForm()
        return render(request, "PlayApp/T04.1-publicaciones_form.html", {"formulario_p":formulario_p})


def publicaciones_busc(request):
    return render(request, "PlayApp/T04.2-publicaciones_busc.html")

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

        formulario_c = PublicacionesForm(request.POST)
        print(formulario_c)
        
        if formulario_c.is_valid:
            info_c = formulario_c.cleaned_data

            coment = Comentario (usuario = info_c ["nombre"], comentario = info_c ["comentario"], fecha = info_c ["fecha"], id_publi = info_c ["publicacion"] )
        
            coment.save()

            return render(request, "PlayApp/T02-inicio.html")

    else:
        formulario_c = ComentariosForm()
        return render(request, "PlayApp/T06-comentarios.html", {"formulario_c":formulario_c})
   

class Crear_Comentario(CreateView):
    model = Comentario
    succes_url = "/PlayApp/comentarios_lista/"
    template_name = "PlayApp/T06-comentarios.html"
    fields = ["nombre", "comentario"]

class Detalle_Comentario(DetailView):
    model = Comentario
    template_name = "PlayApp/T06.3-comentarios_detalle.html"
    
class Listar_Comentario(ListView):
    model = Comentario
    template_name = "PlayApp/T06.1-comentarios_lista.html"
    
class Delete_Comentario(DeleteView):
    model = Comentario
    succes_url = "/PlayApp/comentarios_lista/"
    template_name = "PlayApp/T06.4-comentarios_confirm_delete.html"
    
class Update_Comentario(UpdateView):
    model = Comentario
    succes_url = "/PlayApp/comentarios_lista/"
    fields = ["nombre", "comentario"]
    template_name = "PlayApp/T06.2-comentarios_form.html"

def borrar_comentario(request):
    return render(request, "PlayApp/T06.4-comentarios_confirm_delete.html")


