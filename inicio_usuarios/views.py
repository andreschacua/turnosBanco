from django.shortcuts import render
from django.http import HttpResponse
from inicio_usuarios.models import Clientes

def inicio_usuarios(request):
    return render(request, "index.html")

def comparar(request):
    
    
    mensaje = "cedula usuario: %r" %request.GET["cedula"]
    cedula = request.GET["cedula"]
    
    clientes = Clientes.objects.filter(cedula__icontains = cedula)
    
    return render(request, "resultados_busqueda.html", {"clientes":clientes, "query":cedula})
    
    return HttpResponse(mensaje)