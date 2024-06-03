from django.shortcuts import render
from django.http import HttpResponse
from inicio_usuarios.models import Clientes

def inicio_usuarios(request):
    return render(request, "index.html")

def comparar(request):
    cedula = request.GET.get("cedula", "")
    
    if cedula:
        clientes = Clientes.objects.filter(cedula__icontains=cedula)
    else:
        clientes = []
    
    return render(request, "resultados_busqueda.html", {"clientes": clientes, "query": cedula})
