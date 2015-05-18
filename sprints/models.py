from django.db import models
from authentication.models import Usuario
from proyectos.models import Proyecto
from datetime import datetime, timedelta


class SprintManager(models.Manager):
    def hallarFechaFin(self, fecha_ini, duracion):
            duracion = duracion/8
            fecha_fin = fecha_ini+timedelta(days=duracion)
            return fecha_fin

    def crear_sprint(self, **kwargs):

        owner = Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
        if not owner:
            raise ValueError('Debe existir un Usuario responsable')

        proyecto = Proyecto.objects.buscar_proyecto(id=kwargs.get('proyecto_id'))
        if not kwargs.get('proyecto'):
            raise ValueError('Debe existir un Proyecto propietario')

        if not kwargs.get('fecha_ini'):
            raise ValueError('Debe existir una Fecha de Inicio')

        if not kwargs.get('duracionHoras'):
            raise ValueError('Debe existir una duracion estimada')

        fecha_fin = Sprint.objects.hallarFechaFin(fecha_ini=kwargs.get('fecha_ini'),duracion=kwargs.get('duracionHoras'))
        if not fecha_fin:
            raise ValueError('No se pudo calcular la fecha final')

        sprint = self.model(
            owner= owner,
            proyecto= proyecto,
            estado=Sprint.ACTIVO,
            fecha_ini=kwargs.get('fecha_ini'),
            duracionHoras=kwargs.get('duracionHoras'),
            fecha_fin=fecha_fin,
        )
        sprint.save()
        return sprint

    def buscar_sprint(self, id):
        try:
            return Sprint.objects.get(pk=id)
        except Sprint.DoesNotExist:
            return None

    def cambiar_estado(self, id, **kwargs):
        #cambiar el estado solo si
        sprint = Sprint.objects.buscar_sprint(id)
        if sprint.estado == Sprint.ACTIVO and kwargs.get('estado') == Sprint.CERRADO:
            sprint.estado = kwargs.get('estado')
        else:
            print('No esta permitido cambiar el estado de un Sprint Cerrado')
        sprint.save()


class Sprint(models.Model):
    ACTIVO= 'A'
    CERRADO= 'C'
    ESTADOS_S = (
        ('A', 'Activo'),
        ('C', 'Cerrado'),
    )

    owner = models.ForeignKey(Usuario, null=True)#, editable=False)  # usuario que lo creo
    proyecto = models.ForeignKey(Proyecto, null=True)#, editable=False)  # proyecto a quien pertenece
    #El sprint debera tener uno de los siguientes dos estados:
      #A (Activo): El sprint se encuentra activo.
      #C (Cerrado): El sprint se encuentra cerrado.
    estado = models.CharField(max_length=1, choices=ESTADOS_S, default=ACTIVO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_ini = models.DateTimeField(auto_now_add=False)
    duracionHoras = models.DecimalField(max_digits=6, decimal_places=2, default=300)
    fecha_fin = models.DateTimeField(auto_now_add=False)

    objects = SprintManager()

    REQUIRED_FIELDS = ['owner', 'proyecto', 'fecha_ini', 'duracionhoras']


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
