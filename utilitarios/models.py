from django.db import models
from datetime import datetime

# Create your models here.
class UtilsManager(models.Manager):

    def retornar_fecha(self, fecha=None):
        if fecha!=None:
            return datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        else:
            return Utils.NO_ENCONTRADO


class Utils(models.Model):
    NO_ENCONTRADO = 'NE'
    ERROR = 'EE'
    SIN_EFECTOS = 'SE'
    NO_PERMITIDO = 'NP'
    RTA_MET = (
        ('NE', 'NO_ENCONTRADO'),
        ('SE', 'SIN_EFECTOS'),
        ('EE', 'ERROR'),
        ('NP', 'NO_PERMITIDO'),
    )

    objects = UtilsManager()
