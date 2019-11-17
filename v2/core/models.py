from django.db import models

# Create your models here.

class Comuna(models.Model):
    nombreC = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreC

class Usuario(models.Model):
    celular = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=50)
    fecha = models.IntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre