from django.db import models

# Create your models here.


class TipoMascota(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.nombre

class Refugio(models.Model):

    ciudades = [('Concepcion','concepcion'),
                ('San Pedro','san pedro'),
                ('Hualpen','hualpen')]
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(choices=ciudades, default='Concepcion')
    telefono = models.IntegerField(max_length=50)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField(max_length=10)
    tipo = models.ForeignKey(TipoMascota,on_delete=models.CASCADE)
    refugio = models.ForeignKey(Refugio,on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=200)
    foto = models.ImageField(upload_to='mascota_centro_adopcion',
                             verbose_name='Imagen')
    
    def __str__(self):
        return self.nombre


class ConfiguracionSitio(models.Model):
    nombre_sitio = models.CharField(
        max_length=100, 
        default='Centro de Adopción ❤️',
        verbose_name='Nombre del sitio'
    )
    mensaje_bienvenida = models.CharField(
        max_length=200, 
        default='Dale un hogar a un nuevo amigo hoy ❤️',
        verbose_name='Mensaje de bienvenida'
    )
    activo = models.BooleanField(default=True, verbose_name='Configuración activa')

    class Meta:
        verbose_name = 'Configuración del sitio'
        verbose_name_plural = 'Configuraciones del sitio'

    def __str__(self):  
        return f"Configuración: {self.nombre_sitio}"

    def save(self, *args, **kwargs):  
        # Solo permite una configuración activa
        if self.activo:
            ConfiguracionSitio.objects.exclude(pk=self.pk).update(activo=False)
        super().save(*args, **kwargs)  