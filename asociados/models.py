from django.db import models
from departamento.models import Departamento, Municipio

class Asociado(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(blank=False, null=False)
    nombre = models.CharField('Nombre', max_length=30, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField('Fecha Nacimiento', blank=False, null=False)
    direccion = models.CharField('Direccion', max_length=60, blank=False, null=False)    
    numTelefono = models.CharField('Numero Telefono', max_length=10, blank=False, null=False)
    email = models.EmailField('Email', blank=False, null=False)
    fkDepartamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT, blank=False, null=False)
    fkMunicipio = models.ForeignKey(Municipio, on_delete=models.RESTRICT, blank=False, null=False)
    estrato = models.IntegerField('Estrato', blank=False, null=False)

    class Meta:
        verbose_name = 'Asociados'
        verbose_name_plural = 'Asociados'
        ordering = ['pk']
    
    def __str__(self):
        return self.nombre