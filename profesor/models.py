from django.db import models
from django.db.models import Avg

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    usuarios = models.ManyToManyField('usuario.Usuario', through='publicacion.Publicacion')
    materias = models.ManyToManyField('materia.Materia', through='publicacion.Publicacion')

    def __str__(self) -> str:
        return self.nombre
    
    def get_general_rating(self):
        return self.publicacion_set.aggregate(
            general=Avg((models.F('dominio') + models.F('puntualidad') + models.F('asistencia') + models.F('dificultad') + models.F('seguimiento')) / 5)
        )['general']

    def get_rubric_averages(self):
        return self.publicacion_set.aggregate(
            Dominio=Avg('dominio'),
            Puntualidad=Avg('puntualidad'),
            Asistencia=Avg('asistencia'),
            Dificultad=Avg('dificultad'),
            Seguimiento=Avg('seguimiento')
        )