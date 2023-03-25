from django.contrib import admin
from .models import Juego,Comentario,Reseña,Usuario
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Juego)
admin.site.register(Reseña)
admin.site.register(Comentario)