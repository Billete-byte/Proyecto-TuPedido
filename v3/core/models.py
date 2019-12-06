from django.db import models

# Create your models here.

class Tipo_producto(models.Model):
    #id => auto incrementable
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo_prodcuto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE,verbose_name="tipo_producto")
    informacion = models.TextField(null=True, blank=True)
    fecha_entrega = models.DateField()
    descuento = models.CharField(max_length=2)
    imagen = models.ImageField(null=True , blank=True)

    def __str__(self):
        return self.nombre
