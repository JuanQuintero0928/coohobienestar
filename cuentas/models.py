from django.db import models

# Create your models here.

class Cuenta(models.Model):
    id = models.AutoField(primary_key=True)
    nomCuenta = models.CharField('Nombre Cuenta', max_length=30, blank=False, null=False)
    numCuenta = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['pk']
    
    def __str__(self):
        return self.nomCuenta