from django.shortcuts import render , redirect
from misjuegos.models import *
from misjuegos.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
# Create your views here.
#usuario,juego,reseña,comentario
def inicio(request):
    return render(request,"misjuegos/inicio.html")

def usuario(request):
    return render(request,"misjuegos/usuario.html")

def juego(request):
    return render(request,"misjuegos/juego.html")
def juegoformulario(request):
    return render(request,"misjuegos/juegoformulario.html")
def reseña(request):
    return render(request,"misjuegos/reseña.html")

def comentario(request):
    return render(request,"misjuegos/comentario.html")


#def juegoformulario(request):
#    if request.method == 'POST':
#        formulario=Juegoformulario(request.POST)
#        #juego=Juegoformulario(titulo=request.POST['titulo'],tematica=request.POST['tematica'],estudio=request.POST['estudio'],fecha=request.POST['fecha'])
##       juego.save()
#        diccionario=formulario.cleaned_data['titulo']
#
#        return render(request,'misjuegos/inicio.html')
#    else:
#        formulario=Juegoformulario()
#    return render(request,'misjuegos/juegoformulario.html',{'Formulario':formulario})

#Desde urls tenes que vincular cada view, y eso vinculado con un form que esta vinculado a un model
#class ProductForm(ModelForm):
#    class Meta:
#        model = Product
#        fields = '__all__'
@login_required
def juegoformulario(request):
    if request.method=='POST':
        formulario=Juegoformulario(request.POST)
        if formulario.is_valid():
            titulo=formulario.cleaned_data
            print(titulo)
            juego=Juego(titulo=formulario.cleaned_data['titulo'],
                        tematica=formulario.cleaned_data['tematica'],
                        estudio=formulario.cleaned_data['estudio'],
                        fecha=formulario.cleaned_data['fecha'])
            juego.save()
            #formulario.cleaned_data.save()
            #info=formulario.cleaned_data()
            #juego=Juegoformulario(nombre=info['titulo'],tema=info['tematica'],est=info['estudio'],fech=info['fecha'])
            #juego.save()
            return render(request,'misjuegos/inicio.html')
    else:
        formulario=Juegoformulario()
    return render(request,'misjuegos/juegoformulario.html',{'Formulario':formulario})

def buscarjuego(request,titulo):
    if titulo:
        titulo = request.GET['titulo']
        estudio = Juego.objects.filter(estudio__icontains=estudio)
        return render(request, "AppCoder/resultadoBusqueda.html", {"titulo":titulo, "estudio":estudio})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos" 
    return HttpResponse (respuesta)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:
                login(request,user)
                return redirect('inicio')

            else:
                form = AuthenticationForm()
                return render(request,"misjuegos/login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 1", 'form':form} )

        else:
            form = AuthenticationForm()
            return render(request,"misjuegos/login_request.html", {'mensaje': "Usuario o contrasenia incorrectos 2", 'form': form} )

    else:
        form = AuthenticationForm()
        return render(request, 'misjuegos/login_request.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            form.save()
            form2 = AuthenticationForm()
            return render(request,"misjuegos/login_request.html", {'mensaje2': "Usuario creado correctamente", 'form': form2 })
        else:
            form = UserRegisterForm()
            mensaje = "Los datos ingresados no son validos"

    else:
        form = UserRegisterForm()
        mensaje = "La contraseña debe incluir mayusculas y caracteres especiales"

    return render(request, 'misjuegos/register.html', {'form':form, 'mensaje':mensaje})

def mostrar_todos(request):
    juegos=Juego.objects.all()
    context={'juegos':juegos}
    return render(request,'misjuegos/juegos.html',context)