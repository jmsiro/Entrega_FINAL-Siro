from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PlayApp.forms import *
from PlayApp.models import *
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

