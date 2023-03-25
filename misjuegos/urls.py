from django.urls import path,include
from .views import inicio,usuario,juego,reseña,comentario,juegoformulario,buscarjuego,login_request,register,mostrar_todos
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',inicio,name='inicio'),
    path('usuario/',usuario,name='usuario'),
    path('juego/',mostrar_todos,name='juego'),
    path('reseña/',reseña,name='reseña'),
    path('comentario/',comentario,name='comentario'),
    path('juegoformulario/',juegoformulario,name='Agregar Juego'),
    path('buscarjuego/<titulo>',buscarjuego,name="Buscar Juego"),
    path('login/',login_request,name='login'),
    path('register/',register,name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    
]

