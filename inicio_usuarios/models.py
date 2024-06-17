from django.db import models
from django.core.validators import RegexValidator

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, validators=[RegexValidator(regex='^\\d{1,10}$', message='Cedula must be 1 to 10 digits long')])
    telefono = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Turnos(models.Model):
    cedula = models.CharField(max_length=20)
    turno = models.CharField(max_length=5)
    
    def __str__(self):
        return f'{self.cedula} - {self.turno}'

class TurnosPasados(models.Model):
    cedula = models.CharField(max_length=20)
    turno = models.CharField(max_length=5)
    caja = models.CharField(max_length=20)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.turno} - {self.caja} - {self.fecha_hora}'
    
