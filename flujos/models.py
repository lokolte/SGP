from django.db import models
from authentication.models import Usuario
from proyectos.models import Proyecto
#from django.utils import timezone

class FlujoManager(models.Manager):

    def crear_flujo(self, **kwargs):

        if not kwargs.get('nombre'):
            raise ValueError('Debe existir un nombre de Proyecto')

        proyecto=Proyecto.objects.buscar_proyecto(id=kwargs.get('proyecto_id'))
        if not kwargs.get('proyecto'):
            raise ValueError('Debe existir un Proyecto porpietario')

        owner=Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
        if not owner:
            raise ValueError('Debe existir un Usuario responsable')

        flujo=self.model(
            nombre=kwargs.get('nombre'),
            owner=owner,
            proyecto=proyecto,
            observacion=kwargs.get('observacion'),
            estado=Flujo.TODO,
        )

        flujo.save()
        return flujo

    def buscar_flujo(self, id):
        try:
            return Flujo.objects.get(pk=id)
        except Flujo.DoesNotExist:
            return None

    def modificar_flujo(self, id, **kwargs):
        flujo = Flujo.objects.buscar_flujo(id)
        flujo.nombre = kwargs.get('nombre')
        flujo.observaciones = kwargs.get('observaciones')
        flujo.save()

    def cambiar_estado(self, id, **kwargs):
        flujo = Flujo.objects.buscar_flujo(id)
        if flujo.estado == Flujo.DOING and kwargs.get('estado') == Flujo.DONE: #si es el SCRUM
            #confirmar actividades en DONE
            flujo.estado = kwargs.get('estado')
        elif flujo.estado == Flujo.DONE and kwargs.get('estado') == Flujo.DOING: #si es el SCRUM
            flujo.estado = kwargs.get('estado')
        elif flujo.estado == Flujo.TODO and kwargs.get('estado') == Flujo.DOING:
            flujo.estado = kwargs.get('estado')
            flujo.iniciado = True
        flujo.save()


class Flujo(models.Model):
    # Un flujo tendra un codigo identificador, nombre, estado, actividades y observaciones.
    TODO = 'TD'
    DOING = 'DG'
    DONE = 'DN'
    ESTADOS_F = (
        ('TD', 'To_Do'),
        ('DG', 'Doing'),
        ('DN', 'Done'),
    )
    proyecto = models.ForeignKey(Proyecto, related_name='Proyecto_Flujo')#, editable=False)  #Proyecto al que corresponde el flujo
    owner = models.ForeignKey(Usuario, related_name='Usuario_Flujo', null=True)#, editable=False)  #usuario que lo creo
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    estado = models.TextField(max_length=2, choices=ESTADOS_F, default=TODO)
    observaciones = models.TextField()
    iniciado = models.BooleanField(default=False)

    objects = FlujoManager()

    REQUIRED_FIELDS = ['nombre', 'proyecto', 'owner']

    def __unicode__(self):
        return self.nombre

    def get_nombre(self):
        return self.nombre

    def get_observaciones(self):
        return self.observaciones

    def get_owner(self):
        return self.owner

    def get_estado(self):
        return self.estado

class ActividadManager(models.Manager):
    #def confirmarActividades:
    #
    def crear_actividad(self, **kwargs):
        if not kwargs.get('nombre'):
            raise ValueError('Debe existir un nombre de Actividad')

        flujo = Flujo.objects.buscar_flujo(id=kwargs.get('flujo_id'))
        if not kwargs.get('flujo'):
            raise ValueError('Debe existir un Flujo propietario')

        owner = Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
        if not owner:
            raise ValueError('Debe existir un Usuario responsable')

        if not kwargs.get('orden'):
            raise ValueError('Debe existir un numero de Orden de Actividad')

        actividad = self.model(
            nombre=kwargs.get('nombre'),
            owner=owner,
            flujo=flujo,
            estado=Actividad.TODO,
            orden=kwargs.get('orden'),
        )

        actividad.save()
        return actividad

    def buscar_actividad(self, id):
        try:
            return Actividad.objects.get(pk=id)
        except Actividad.DoesNotExist:
            return None

    #
    def cambiar_estado_actividad(self, id, **kwargs):
        actividad = Actividad.objects.buscar_actividad(id)#.get(id)
        if(actividad is not None):
            if actividad.estado == Actividad.DOING and kwargs.get('estado') == Actividad.DONE:
                #confirmar que se hallan finalizado los US correspondientes
                if actividad.cantidadUS == 0: #cantidad de US pendientes
                    actividad.estado = kwargs.get('estado')
            elif actividad.estado == Actividad.DOING and kwargs.get('estado') == Actividad.TODO:
                actividad.estado = kwargs.get('estado')
            elif actividad.estado == Actividad.TODO and kwargs.get('estado') == Actividad.DOING:
                actividad.estado = kwargs.get('estado')
            elif actividad.estado == Actividad.DONE and kwargs.get('estado') == Actividad.DOING: #solo el SCRUM
                actividad.estado = kwargs.get('estado')
            else:
                print('No esta permitido')
        actividad.save()

    # no utilizar x el momento
    def modificar_actividad(self, id, **kwargs):
        actividad = Actividad.objects.buscar_actividad(id)
        actividad.cantidadUS = kwargs.get('cantidadUS')#cantidad de US pendientes
        actividad.save()


class Actividad(models.Model):
    # Una actividad tendra un codigo identificador unico, flujo, estado, conjunto de US.
    #Los estados seran estaticos: To do. Doing. Done.
    TODO = 'TD'
    DOING = 'DG'
    DONE = 'DN'
    ESTADOS_A = (
        ('TD', 'ToDo'),
        ('DG', 'Doing'),
        ('DN', 'Done'),
    )
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    owner = models.ForeignKey(Usuario, related_name='Actividad_Owner', null=True)#, editable=False)  #usuario que lo creo
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    flujo = models.ForeignKey(Flujo, related_name='Actividad_Flujo')#, editable=False)  #Flujo al que corresponde la actividad
    estado = models.TextField(max_length=2, choices=ESTADOS_A, default=TODO)
    orden = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    cantidadUS = models.DecimalField(max_digits=4, decimal_places=0, default=0)#cantidad de US pendientes

    objects = ActividadManager()

    REQUIRED_FIELDS = ['nombre', 'owner', 'flujo', 'orden']

    def __unicode__(self):
        return self.nombre

    def get_nombre(self):
        return self.nombre

    def get_orden(self):
        return self.orden

    def get_owner(self):
        return self.owner

    def get_flujo(self):
        return self.flujo

    def get_estado(self):
        return self.estado