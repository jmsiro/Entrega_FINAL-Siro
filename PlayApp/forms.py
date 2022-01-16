from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    clave = forms.CharField()
    tipo = forms.CharField()