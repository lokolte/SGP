from django.db import models
from datetime import datetime
import json

# Create your models here.
class UtilsManager(models.Manager):

    def retornar_fecha(self, fecha=None):
        if fecha != None:
            print('La fecha recibida es: ' + fecha)
            return datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        else:
            return Utils.NO_ENCONTRADO

    def definir_respuesta(self, result=None):
        resultado = Resultados()

        try:
            print(result)

            if result == Utils.NO_ENCONTRADO or result == None:
                resultado.status = Utils.NO_ENCONTRADO
                resultado.message = 'Proyecto no encontrado.'
                return resultado

            elif result == Utils.NO_PERMITIDO:
                resultado.status = Utils.NO_PERMITIDO
                resultado.message = 'Operacion invalida.'
                return resultado

            elif result == Utils.ERROR:
                resultado.status = Utils.ERROR
                resultado.message = 'Ocurrio algun error.'
                return resultado

            elif result == Utils.SIN_EFECTOS:
                resultado.status = Utils.SIN_EFECTOS
                resultado.message = 'La operacion no tuvo efectos.'
                return resultado

            elif result == Utils.BAD_REQUEST:
                resultado.status = Utils.BAD_REQUEST
                resultado.message = 'Bad Request.'

            elif result != None:
                print('Respuesta exitosa!..')
                resultado.status = Utils.RESPUESTSA_EXITOSA
                resultado.message = 'Respuesta exitosa!..'
                return resultado

            return resultado

        except:
            print('Es una instancia.')
            print(result)
            print('Respuesta exitosa!..')
            resultado.status = Utils.RESPUESTSA_EXITOSA
            resultado.message = 'Respuesta exitosa!..'
            return resultado


class Utils(models.Model):
    NO_ENCONTRADO = 'NE'
    ERROR = 'EE'
    SIN_EFECTOS = 'SE'
    NO_PERMITIDO = 'NP'
    RESPUESTSA_EXITOSA = 'RE'
    BAD_REQUEST = 'BD'

    RTA_MET = (
        ('NE', 'NO_ENCONTRADO'),
        ('SE', 'SIN_EFECTOS'),
        ('EE', 'ERROR'),
        ('NP', 'NO_PERMITIDO'),
        ('RE', 'RESPUESTSA_EXITOSA'),
        ('BD', 'BAD_REQUEST'),
    )

    objects = UtilsManager()

class Resultados:
    status = ''
    message = ''

    def __init__(self, status=None, message=None):
        self.status = status
        self.message = message

    def to_json(self):
        return json.dumps(self.__dict__)