from django.db import models

# Create your models here.
class User(models.Model):
    # id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=50)
    rol = models.CharField(max_length=100)
    descripccion = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre
