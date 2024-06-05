from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio_usuarios.models import Clientes
from django.urls import reverse

def inicio_usuarios(request):
    return render(request, "index.html")

def comparar(request):
    cedula = request.GET.get("cedula", "")
    
    if cedula:
        clientes = Clientes.objects.filter(cedula__exact=cedula)
        if clientes.exists():
            # Redirigir a la página para asignar turno
            return redirect(reverse('asignar_turno'))
        else:
            # Redirigir a la página para registrar nombre y teléfono
            return redirect(reverse('registro_cliente', kwargs={'cedula': cedula}))
    
    return render(request, "resultados_busqueda.html", {"clientes": [], "query": cedula})

def asignar_turno(request):
    return render(request, 'asignar_turno.html')

def registro_cliente(request, cedula):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        if nombre and telefono:
            nuevo_cliente = Clientes(nombre=nombre, cedula=cedula, telefono=telefono)
            nuevo_cliente.save()
            return redirect(reverse('asignar_turno'))
    return render(request, 'registro_cliente.html', {'cedula': cedula})

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        if nombre and cedula and telefono:
            nuevo_cliente = Clientes(nombre=nombre, cedula=cedula, telefono=telefono)
            nuevo_cliente.save()
            return redirect('ver_clientes')
    return render(request, 'agregar_cliente.html')