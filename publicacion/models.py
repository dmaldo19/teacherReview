from django.db import models
from usuario.models import Usuario
from profesor.models import Profesor
from materia.models import Materia

# Create your models here.
class Publicacion(models.Model):
    #Llave foranea
    #Si el usuario se elimina, se elimina la publicacion
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    comentario = models.CharField(max_length=500)
    dominio = models.IntegerField()
    puntualidad = models.IntegerField()
    asistencia = models.IntegerField()
    dificultad = models.IntegerField()
    seguimiento = models.IntegerField()

    def __str__(self) -> str:
        return self.titulo