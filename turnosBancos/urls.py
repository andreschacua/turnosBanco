"""turnosBancos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio_usuarios, name='inicio'),
    path('comparar/', views.comparar, name='comparar'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('asignar-turno/', views.asignar_turno, name='asignar_turno'),
    path('registro-cliente/<str:cedula>/', views.registro_cliente, name='registro_cliente'),
    path('cajero/', views.cajero_view, name='cajero_view'),
    path('gerencia/', views.gerencia_view, name='gerencia_view'),
    path('atencion-usuario/', views.atencion_usuario_view, name='atencion_usuario_view'),
]

