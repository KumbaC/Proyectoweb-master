from django.db import models
from django.contrib.auth.models import User

# Crea tus modelos aquí.
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    created =  models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta: 
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categorias de tienda'
def __str__(self):
    return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ManyToManyField(CategoriaProd)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    created =  models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta: 
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos de tienda'
def __str__(self):
    return self.nombre
  