from django.db import models

# Create your models here.

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    cod =models.CharField('Codigo', max_length=4)
    nombre = models.CharField('Nombre', max_length=20)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['pk']

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    fkDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=False, null=False)
    cod = models.CharField('Codigo', max_length=6)
    nombre = models.CharField('Nombre', max_length=20)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['pk']

    def __str__(self):
        return self.nombre