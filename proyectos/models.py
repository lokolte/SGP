from authentication.models import Usuario
from django.db import models
# Create your models here.

class ProyectoManager(models.Manager):
    #recibe nombre, owner_id, cliente_id, estado,
    def crear_proyecto(self, **kwargs):

        if not kwargs.get('nombre'):
            raise ValueError('Debe existir un nombre de Proyecto')

        owner= buscar_usuario(id=kwargs.get('owner_id'))
        if not kwargs.get('owner'):
            raise ValueError('Debe existir un Usuario responsable')

        cliente= buscar_usuario(id=kwargs.get('cliente_id'))
        if not cliente:
            raise ValueError('Debe existir un cliente de Proyecto')

        if not kwargs.get('fecha_ini'):
            raise ValueError('Debe existir una Fecha de Inicio')

        if not kwargs.get('fecha_fin'):
            raise ValueError('Debe existir una Fecha de Fin Estimado')

        if not kwargs.get('estado'):
            estadoaux=Proyecto.SUSPENDIDO,
        else:
            if kwarg.get('estado') == 'S':
                estadoaux=Proyecto.SUSPENDIDO#kwargs.get('estado'),
            elif kwargs.get('estado') == 'A':
                estadoaux=Proyecto.ACTIVO

        proyecto = self.model(
            nombre=nombre,
            owner=owner,
            estado=estadoaux,
            cliente=cliente,
            fecha_ini=fecha_ini,
            fecha_fin=fecha_fin,
            observacion=kwargs.get('observacion'),
        )
        proyecto.save()
        return proyecto

    def buscar_proyecto(self, id):
        try:
            return Proyecto.objects.get(pk=id)
        except Proyecto.DoesNotExist:
            return

class Proyecto(models.Model):
    ACTIVO = 'A'
    SUSPENDIDO = 'S'
    FINALIZADO = 'F'
    ESTADOS_P = (
        ('A', 'Activo'),
        ('S', 'Suspendido'),
        ('F', 'Finalizado'),
    )
    owner = models.ForeignKey(Usuario, related_name='Usuario_Proyecto', editable=False)  #usuario que lo creo
    cliente = models.ForeignKey(Usuario, related_name='Cliente_Proyecto', blank=True, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion =  models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=1, choices=ESTADOS_P, default=SUSPENDIDO)
    fecha_ini = models.DateTimeField(auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now_add=False)  #fecha entrega estimada
    observacion = models.TextField()

    objects = ProyectoManager()

    REQUIRED_FIELDS = ['nombre', 'owner', 'cliente', 'fecha_ini', 'fecha_fin']

    def __unicode__(self):
        return self.nombre

    def get_nombre(self):
        return self.nombre

    def get_observacion(self):
        return self.observacion

    def get_owner(self):
        return self.owner

    def get_cliente(self):
        return self.cliente