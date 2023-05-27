from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creo la clase: Articulo, con campos titulo, subtitulo, cuerpo, autor, fecha (imagen optativa)


#Creo la clase articulo
class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=1500)
    autor = models.CharField(max_length=256)
    fecha_publicacion = models.DateField(null=True)
    #agrego el modo creador para que registre quien fue el creador
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


  #le agrego el método mágico str para visualizarlo bien en el panel admin
    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.fecha_publicacion}"
