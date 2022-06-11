from errno import EADDRNOTAVAIL
from django.db import models

# Create your models here.
class ModeloFamilia(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=100, null=False, default='Esta es una descripcion corta de un familiar')
    edad = models.IntegerField(null=False)
    fdn = models.DateField()
    parentesco = models.CharField(max_length=20)
