from django.db import models
from datetime import datetime

# Create your models here.
class UtilsManager(models.Manager):
    def retornar_fecha(self, fecha=None):
        if fecha != None:
            print('La fecha recibida es: ' + fecha)
            return datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        else:
            return Utils.NO_ENCONTRADO

    def definirrespuesta(self, result=None):
        if result == Utils.NO_ENCONTRADO:
            Resultados.status = Utils.NO_ENCONTRADO
            Resultados.message = 'Proyecto no encontrado.'
            return Resultados
        elif result == Utils.NO_PERMITIDO:
            Resultados.status = Utils.NO_PERMITIDO
            Resultados.message = 'La operacion no esta permitida.'
            return Resultados
        elif result == Utils.ERROR:
            Resultados.status = Utils.ERROR
            Resultados.message = 'Ocurrio algun error.'
            return Resultados
        elif result == Utils.SIN_EFECTOS:
            Resultados.status = Utils.SIN_EFECTOS
            Resultados.message = 'La operacion no tuvo efectos.'
            return Resultados
        else:
            print('Respuesta exitosa!..')
            Resultados.status = Utils.RESPUESTSA_EXITOSA
            Resultados.message = 'Respuesta exitosa!..'
            return Resultados

class Utils(models.Model):
    NO_ENCONTRADO = 'NE'
    ERROR = 'EE'
    SIN_EFECTOS = 'SE'
    NO_PERMITIDO = 'NP'
    RESPUESTSA_EXITOSA = 'RE'
    RTA_MET = (
        ('NE', 'NO_ENCONTRADO'),
        ('SE', 'SIN_EFECTOS'),
        ('EE', 'ERROR'),
        ('NP', 'NO_PERMITIDO'),
        ('RE', 'RESPUESTSA_EXITOSA'),
    )

    objects = UtilsManager()

class Resultados:
    status = ''
    message = ''