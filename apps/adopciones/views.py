from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

from apps.adopciones.models import Persona, Solicitud



def index_adopcion(request):
	return HttpResponse("soy la pagina principal de la app adopcion")


class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopciones/solicitud_list.html'
