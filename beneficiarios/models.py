from django.db import models
from asociados.models import Asociado

# Create your models here.

class ParentescoOP(models.TextChoices):
    madre = 'MADRE', 'Madre'
    padre = 'PADRE', 'Padre'
    hermano = 'HERMANO', 'Hermano'
    hermana = 'HERMANA', 'Hermana'
    esposo = 'ESPOSO', 'Esposo'
    hijo = 'HIJO', 'Hijo'
    hija = 'HIJA', 'Hija'
    sobrino = 'SOBRINO', 'Sobrino'
    sobrina = 'SOBRINA', 'Sobrina'

class Beneficiario(models.Model):
    id = models.AutoField(primary_key=True)
    fkAsociado = models.ForeignKey(Asociado, on_delete=models.RESTRICT, blank=False, null=False)
    cedula = models.IntegerField(blank=False, null=False)
    nomBeneficiario = models.CharField('Nombre', max_length=30, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField('Fecha Nacimiento', blank=False, null=False)
    parentesco = models.CharField('Parentesco', max_length=40 ,choices=ParentescoOP.choices, blank=False, null=False)
    ImgCedula = models.FileField(upload_to='cedula', blank=True, null=True)

    class Meta:
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'
        ordering = ['pk']
    
    def __str__(self):
        return self.nomBeneficiario
    
class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    fkAsociado = models.ForeignKey(Asociado, on_delete=models.RESTRICT, blank=False, null=False)
    nomMascota = models.CharField('Nombre Mascota', max_length=30, blank=False, null=False)
    Raza = models.CharField('Raza', max_length=30, blank=False, null=False)
    añoNacimiento = models.DateField('Fecha Nacimiento', blank=False, null=False)
    fotoMascota = models.FileField(upload_to='mascota', blank=True, null=True)
    ImgCarnet = models.FileField(upload_to='carnet', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        ordering = ['pk']
    
    def __str__(self):
        return self.nomMascota