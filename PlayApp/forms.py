from datetime import datetime, time
from django import forms
from django.contrib.auth.forms import UserCreationForm
from PlayApp.models import Usuario





class UsuarioForm(UserCreationForm):
    # nombre = forms.CharField(max_length=40, label="Nombre")
    # apellido = forms.CharField(max_length=40, label="Apellido")
    email = forms.EmailField(max_length=50, help_text="Agregar una dirección de Email válida")
    # tipo = forms.CharField()
    # password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    # password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ["username", "nombre", "apellido", "email", "tipo", "password1", "password2"]

class PublicacionesForm(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField(widget=forms.HiddenInput())
    subtitulo = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":20}))
    noticia = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":40}))
    fecha = forms.DateField(initial=datetime.now(), show_hidden_initial=True, widget=forms.HiddenInput())
    id_autor = forms.CharField(widget=forms.HiddenInput())

class ComentariosForm(forms.Form):
    nombre = forms.CharField()
    comentario = forms.CharField(widget=forms.Textarea())
    fecha = forms.DateField(initial=datetime.now(), show_hidden_initial=True)
    # publicacion = forms.IntegerField()

