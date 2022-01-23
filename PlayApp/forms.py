from datetime import datetime, time
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=40, label="Nombre")
    last_name = forms.CharField(max_length=40, label="Apellido")
    email = forms.EmailField()
    tipo = forms.CharField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2", "tipo"]

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

