from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def primer_view(request):
    plantilla = loader.get_template("PlayApp/T01-view.html")

    documento = plantilla.render()

    return HttpResponse(documento)

def inicio(request):
    plantilla = loader.get_template("PlayApp/T02-inicio.html")

    documento = plantilla.render()
    
    return HttpResponse(documento)

def usuario(request):
    plantilla = loader.get_template("PlayApp/T03-usuario.html")

    documento = plantilla.render()

    return HttpResponse(documento)

def publicaciones(request):
    plantilla = loader.get_template("PlayApp/T04-publicaciones.html")

    documento = plantilla.render()

    return HttpResponse(documento)

def sobre_nosotros(request):
    plantilla = loader.get_template("PlayApp/T05-sobre_nosotros.html")

    documento = plantilla.render()

    return HttpResponse(documento)