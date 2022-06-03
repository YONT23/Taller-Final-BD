from django.db import models
from django.contrib.auth.models import User
from apps.libro.models import Libro

# Create your models here.

class Ejemplares(models.Model):
    localizacion = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro,  blank=False, null=False, on_delete=models.CASCADE,)

class Prestar(models.Model):
    ejemplares = models.ForeignKey(Ejemplares, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fecha_dev = models.DateField()
    fecha_pres = models.DateField()