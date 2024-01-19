from django.db import models

# Create your models here.

class ServicioFijo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False, null=False)
    tarifa = models.IntegerField(models.IntegerField(blank=False, null=False))

    class Meta:
        verbose_name = 'Servicios Fijos'
        verbose_name_plural = 'Servicios Fijos'
        ordering = ['id']

    def __str__(self):
        return self.nombre
    