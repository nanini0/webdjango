from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    descipcion = models.TextField(max_length=200)
    foto = models.ImageField(upload_to='equipo_trabajo',
                             verbose_name='Imagen')
    create = models.DateField(auto_now_add=True)
    updatea = models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre