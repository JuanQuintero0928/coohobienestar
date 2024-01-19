from django.db import models
from cuentas.models import Cuenta
from asociados.models import Asociado

# Create your models here.

class ServicioFijo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False, null=False)
    tarifa = models.IntegerField(models.IntegerField(blank=False, null=False))
    fkCuenta = models.ForeignKey(Cuenta, on_delete=models.RESTRICT, blank=False, null=False)

    class Meta:
        verbose_name = 'Servicios Fijos'
        verbose_name_plural = 'Servicios Fijos'
        ordering = ['id']

    def __str__(self):
        return self.nombre
    
class ServicioAdicionales(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=30, blank=False, null=False)
    fkCuenta = models.ForeignKey(Cuenta, on_delete=models.RESTRICT, blank=False, null=False)

    class Meta:
        verbose_name = 'Servicios Adicionales'
        verbose_name_plural = 'Servicios Adicionales'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class MesesOP(models.TextChoices):
    enero = 'ENERO', 'Enero'
    febrero = 'FEBRERO', 'Febrero'
    marzo = 'MARZO', 'Marzo'
    abril = 'ABRIL', 'Abril'
    mayo = 'MAYO', 'Mayo'
    junio = 'JUNIO', 'Junio'
    julio = 'JULIO', 'Julio'
    agosto = 'AGOSTO', 'Agosto'
    septiembre = 'SEPTIEMBRE', 'Septiembre'
    octubre = 'OCTUBRE', 'Octubre'
    noviembre = 'NOVIMEBRE', 'Noviembre'
    diciembre = 'DICIEMBRE', 'Diciembre'

class Historico(models.Model):
    id = models.AutoField(primary_key=True)
    pkAsociado = models.ForeignKey(Asociado, on_delete=models.RESTRICT, blank=False, null=False)
    mes = models.CharField('Mes', max_length=40 ,choices=MesesOP.choices, blank=False, null=False)
    valor = models.IntegerField(blank=False, null=False)
    FechaPago = models.DateField('Fecha Pago', blank=True, null=True)
    estado = models.BooleanField('Estado', blank=False, null=False)

    class Meta:
        verbose_name = 'Historico'
        verbose_name_plural = 'Historico'
        ordering = ['id']

    def __str__(self):
        return self.pkAsociado.nombre