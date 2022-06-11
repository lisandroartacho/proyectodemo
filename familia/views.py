from django.shortcuts import render
from django.http import HttpResponse
from .models import ModeloFamilia
# Create your views here.

#familiares = [
#    {'id': 1, 'nombre': 'Juan', 'apellido': 'Flores', 'descripcion': 'Casado y sin hijos. Fanatico de D&D.', 'edad': 35, 'fdn': '1986-06-15', 'parentesco': 'hermano'},
#    {'id': 2, 'nombre': 'Carla', 'apellido': 'Flores', 'descripcion': 'Soltera. Busca marido urgentemente. Buena estudiante.', 'edad': 30, 'fdn': '1992-07-20', 'parentesco': 'hermana'},
#    {'id': 3, 'nombre': 'Lisandro', 'apellido': 'Artacho', 'descripcion': 'Soltera. Busca marido urgentemente. Buena estudiante.', 'edad': 30, 'fdn': '1992-07-20', 'parentesco': 'hermana'}
#]

def inicio(request):
    familiares = ModeloFamilia.objects.all()
    contexto = {'familiares': familiares}
    return render(request, 'familia/inicio.html', contexto)

def miembro_de_familia(request, pk):

    pariente = ModeloFamilia.objects.get(id = int(pk))
    
    contexto = {'pariente': pariente}
    return render(request, 'familia/familiar.html', contexto)

