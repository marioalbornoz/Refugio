from django.contrib import admin
from apps.adopciones.models import Persona, Solicitud

# Register your models here.
admin.site.register(Persona)
admin.site.register(Solicitud)