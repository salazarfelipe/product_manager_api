from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=200, verbose_name="Nombre")
    price = models.FloatField(verbose_name="Precio", null=True, blank=True)
    date = models.DateField(verbose_name="Fecha de caducidad", null=True, blank=True)
    latitud = models.CharField(max_length=100, verbose_name="Latitud", null=True, blank=True)
    longitud = models.CharField(max_length=100, verbose_name="Longitud", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.name
