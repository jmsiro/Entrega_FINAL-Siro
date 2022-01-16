from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from PlayApp.forms import UsuarioForm
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

def sobre_nosotros(request):
    return render(request, "PlayApp/T05-sobre_nosotros.html")

