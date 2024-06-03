from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Turnos(models.Model):
    cedula = models.CharField(max_length=10)
    servicio = models.CharField(max_length=10)
    turno = models.CharField(max_length=4)
    modulo = models.CharField(max_length=10)
    
class Caja (models.Model):
    num_caja = models.IntegerField()
    estado = models.CharField(max_length=10)
    
class Gerencia (models.Model):
    estado = models.CharField(max_length=10)
    
class AtenCliente (models.Model):
    num_modulo = models.IntegerField()
    estado = models.CharField(max_length=10)
    
    