from django.db import models
from userstories.models import UserStory
from utilitarios.models import Utils

# Create your models here.
class HistorialUSManager(models.Manager):

    #recibe {'userstory_id': #, 'horas_trabajadas': #, 'descripcion_trabajo': #}
    def registrarTrabajo(self, **kwargs):

        if not kwargs.get('userstory_id'):
            raise ValueError('Debe existir un Usuario responsable')
        else:
            us = UserStory.objects.buscar_userstory(id=kwargs.get('userstory_id'))
            if us==None:
                print('No existe el User Story')
                return Utils.NO_ENCONTRADO

        if not kwargs.get('horas_trabajadas'):
            raise ValueError('Debe registrar una cantidad de horas de trabajo')
        else:
            horas = kwargs.get('horas_trabajadas')

        if not kwargs.get('descripcion_trabajo'):
            descripcion = ''
        else:
            descripcion = kwargs.get('descripcion_trabajo')

        if us.tamanho >= (us.horasregistradas + horas):
            us.horasregistradas = us.horasregistradas + horas
        else:
            print('Atencion el registro tiene un tamanho mayor al del US!.')
            us.horasregistradas = us.horasregistradas + horas

        hus = self.model(
            userstory=us,
            horas_trabajas=horas,
            descripcion_trabajo=descripcion
        )

        hus.save()
        return hus

class HistorialUS(models.Model):
    userstory = models.ForeignKey(UserStory, related_name='HistorialUS_US', null=True)
    horas_trabajadas = models.IntegerField(default=0)
    descripcion_trabajo = models.CharField(max_length=350)
    fecha_creacion = models.DateTimeField(auto_now=True)

    objects = HistorialUSManager()