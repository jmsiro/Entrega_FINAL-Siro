from datetime import datetime, time
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm




# class UsuarioForm(UserCreationForm):
#     email = forms.EmailField()
#     tipo = forms.CharField()
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    # class Meta:
    #     model = Usuario
    #     fields = ["nombre", "email", "password1", "password2", "tipo"]

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

