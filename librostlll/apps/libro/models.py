from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    numeropagina = models.CharField(max_length=20)
    edictorial = models.CharField(max_length=15)
    isbn = models.CharField(max_length=10)
    autor = models.ForeignKey(Autor, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo