from django.db import models
from django.core.validators import RegexValidator

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, validators=[RegexValidator(regex='^\\d{1,10}$', message='Cedula must be 1 to 10 digits long')])
    telefono = models.CharField(max_length=20, validators=[RegexValidator(regex='^\\d{1,10}$', message='Cedula must be 1 to 10 digits long')])
    
    def __str__(self):
        return self.nombre
