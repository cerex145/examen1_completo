from django.db import models
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Peliculas(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    estreno = models.DateField()
    genero = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='peliculas')

    def __str__(self):
        return self.titulo

