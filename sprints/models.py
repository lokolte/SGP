from django.db import models
from authentication.models import Usuario
from proyectos.models import Proyecto
from datetime import timedelta
from utilitarios.models import Utils
#import time

class SprintManager(models.Manager):

    def hallarFechaFin(self, fecha_ini=None, duracion=None):

        if fecha_ini != None and duracion != None:
            duracion = duracion / 8
            fecha_ini = Utils.objects.retornar_fecha(fecha_ini)
            fecha_fin = fecha_ini + timedelta(days=duracion)
            return fecha_fin
        else:
            print('Imposible efectuar operacion sin datos')
            return Utils.NO_PERMITIDO

    def crear_sprint(self, **kwargs):

        if not kwargs.get('owner_id'):
            raise ValueError('Debe existir un Usuario responsable')
        else:
            owner = Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
            if owner == None:
                print('No existe el owner')
                return Utils.NO_ENCONTRADO

        if not kwargs.get('proyecto_id'):
            raise ValueError('Debe existir un Proyecto propietario')
        else:
            proyecto = Proyecto.objects.buscar_proyecto(id=kwargs.get('proyecto_id'))
            if proyecto == None:
                print('No existe el proyecto')
                return Utils.NO_ENCONTRADO

        if not kwargs.get('fecha_ini'):
            raise ValueError('Debe existir una Fecha de Inicio')

        if not kwargs.get('duracionHoras'):
            raise ValueError('Debe existir una duracion estimada')

        if not kwargs.get('fecha_fin'):
            print('La fecha de finalizacion fue calculada...')
            fecha_fin = Sprint.objects.hallarFechaFin(fecha_ini=kwargs.get('fecha_ini'),
                                                      duracion=kwargs.get('duracionHoras'))
        else:
            fecha_fin = kwargs.get('fecha_fin')

        sprint = self.model(
            owner=owner,
            proyecto=proyecto,
            estado=Sprint.ACTIVO,
            fecha_ini=kwargs.get('fecha_ini'),
            duracionHoras=kwargs.get('duracionHoras'),
            horasRest=kwargs.get('duracionHoras'),
            fecha_fin=fecha_fin,
        )
        sprint.save()
        return sprint

    def buscar_sprint(self, id):
        try:
            return Sprint.objects.get(pk=id)
        except Sprint.DoesNotExist:
            return None

    # dominio de estados: A = Activo, C = Cerrado. Utilizar las abreviaturas
    def cambiar_estado(self, id, **kwargs):
        sprint = Sprint.objects.buscar_sprint(id)

        if sprint != None:
            if sprint.estado == Sprint.ACTIVO and kwargs.get('estado') == Sprint.CERRADO:
                sprint.estado = kwargs.get('estado')
                sprint.save()
                return sprint
            else:
                print('No esta permitido cambiar el estado de un Sprint Cerrado')
                return Utils.NO_PERMITIDO
        else:
            print('No existe el sprint')
            return Utils.NO_ENCONTRADO

class Sprint(models.Model):
    ACTIVO = 'A'
    CERRADO = 'C'
    ESTADOS_S = (
        ('A', 'Activo'),
        ('C', 'Cerrado'),
    )

    owner = models.ForeignKey(Usuario, null=True)  # , editable=False)  # usuario que lo creo
    proyecto = models.ForeignKey(Proyecto, null=True)  # , editable=False)  # proyecto a quien pertenece
    # El sprint debera tener uno de los siguientes dos estados:
    #A (Activo): El sprint se encuentra activo.
    #C (Cerrado): El sprint se encuentra cerrado.
    estado = models.CharField(max_length=1, choices=ESTADOS_S, default=ACTIVO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_ini = models.DateTimeField(auto_now_add=False)
    duracionHoras = models.DecimalField(max_digits=6, decimal_places=2, default=300)
    fecha_fin = models.DateTimeField(auto_now_add=False)
    horasRest = models.DecimalField(max_digits=6, decimal_places=2, default=300)

    objects = SprintManager()

    REQUIRED_FIELDS = ['owner', 'proyecto', 'fecha_ini', 'duracionHoras']


    def get_owner(self):
        return self.owner

    def get_proyecto(self):
        return self.proyecto

    def get_duracionHoras(self):
        return self.duracionHoras

    def get_fecha_ini(self):
        return self.fecha_ini

    def get_fecha_fin(self):
        return self.fecha_fin

    def get_estado(self):
        return self.estado
