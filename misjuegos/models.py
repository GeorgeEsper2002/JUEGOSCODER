from django.db import models
# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    #email=models.CharField(max_length=30)
    #fecha_nac=models.DateField()
#class Juego(models.Model):
#    titulo=models.CharField(max_length=50)
#    tematica=models.CharField(max_length=10)
#    estudio=models.CharField(max_length=50,blank=True) #El estudio que creo el juego
#    fecha=models.CharField(max_length=10)
#    #imagen=models.ImageField()
#    def __str__(self):
#        return self.titulo
class Juego(models.Model):
    titulo = models.CharField(max_length=150, null = True)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to="uploads/", null=True)
    tematica = models.CharField(max_length=50, null=True)
    estudio = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    juego=models.ForeignKey(Juego,on_delete=models.CASCADE)
    puntuacion=models.FloatField()
    user=models.ForeignKey(Usuario,on_delete=models.CASCADE)    
    texto=models.TextField()
    fecha=models.DateField()
    
    
class Comentario(models.Model):
    resena=models.ForeignKey(Reseña,on_delete=models.CASCADE)
    user=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    texto=models.TextField()
    fecha_pub=models.DateField()
    
    