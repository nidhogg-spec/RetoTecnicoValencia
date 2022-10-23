from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=50)
    rol = models.CharField(max_length=100)
    descripccion = models.CharField(max_length=1000)
    def __str__(self):
        return self.nombre
