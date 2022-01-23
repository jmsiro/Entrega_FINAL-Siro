from datetime import datetime, time
from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    clave = forms.CharField()
    tipo = forms.CharField()

class PublicacionesForm(forms.Form):
    titulo = forms.CharField()
    nombre = forms.CharField()
    noticia = forms.CharField(widget=forms.Textarea())
    fecha = forms.DateField(initial=datetime.now(), show_hidden_initial=True)

class ComentariosForm(forms.Form):
    nombre = forms.CharField()
    comentario = forms.CharField(widget=forms.Textarea())
    fecha = forms.DateField(initial=datetime.now(), show_hidden_initial=True)
    # publicacion = forms.IntegerField()

