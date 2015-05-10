from django.db import models
from authentication.models import Usuario
from proyectos.models import Proyecto

class FlujoManager(models.Manager):

    def crear_flujo(self, nombre, **kwargs):

        if not nombre:
            raise ValueError('Debe existir un nombre de Proyecto')

        proyecto= buscar_proyecto(id=kwargs.get('proyecto_id'))
        if not kwargs.get('proyecto'):
            raise ValueError('Debe existir un nombre de Proyecto')

        owner= buscar_usuario(id=kwargs.get('owner_id'))
        if not owner:
            raise ValueError('Debe existir un nombre de Proyecto')

        flujo = self.model(
            nombre=nombre,
            owner= owner,
            proyecto= proyecto,
            observacion=kwargs.get('observacion'),
            estado=Flujo.TODO,
        )

        flujo.save()
        return flujo

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
    estado = models.TextField(max_length=2, choices=ESTADOS_F, default=TODO)
    observaciones = models.TextField()

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