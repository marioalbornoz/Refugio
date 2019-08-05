from django.db import models
from apps.adopciones.models import Persona

# Create your models here.
class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre

class Mascota(models.Model):
		nombre = models.CharField(max_length=50)
		sexo = models.CharField(max_length=10)
		fecha = models.DateField()
		edad = models.IntegerField()
		persona = models.ForeignKey(Persona, null = True, blank = True, on_delete=models.CASCADE)
		vacuna = models.ManyToManyField(Vacuna, blank = True)

		def __str__(self):
			return self.nombre