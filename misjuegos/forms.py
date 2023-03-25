from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.core.validators import RegexValidator
class Juegoformulario(forms.Form):
    titulo=forms.CharField(max_length=50) # use esto para que por ej: un juego se llame "age of empires 2"
    tematica=forms.CharField(max_length=50)
    estudio=forms.CharField(max_length=50)
    fecha=forms.CharField(max_length=50)
    #imagen=forms.ImageField(null=True)

class UsuarioForm(UserCreationForm):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()

class Reseña(forms.Form):
    usuario=UsuarioForm()
    texto=forms.CharField()
    opinion=forms.BooleanField()

class Comentario(forms.Form):
    usuario=UsuarioForm()
    juego=forms.CharField()
    texto=forms.CharField()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}