from authentication.models import Usuario
from django.db import models
# Create your models here.

class ProyectoManager(models.Manager):

    def crear_proyecto(self, nombre, **kwargs):

        if not nombre:
            raise ValueError('Debe existir un nombre de Proyecto')

        if not kwargs.get('observacion'):
            raise ValueError('Debe tener una observacion valida')

        proyecto = self.model(
            nombre=nombre,
            observacion=kwargs.get('observacion'),
            estado=Proyecto.SUSPENDIDO,
        )

        proyecto.save()
        return proyecto

    #la variable cliente_id es el id del Usuario cliente
    def agregar_cliente(self, cliente_id, **kwargs):

        cliente = Usuario.objects.get(pk=cliente_id)

        if not cliente:
            raise ValueError('Debe existir un Cliente valido')

        proyecto = self.model(
            cliente=cliente,
        )

        proyecto.save()
        return proyecto

class Proyecto(models.Model):
    ACTIVO = 'A'
    SUSPENDIDO = 'S'
    FINALIZADO = 'F'
    ESTADOS_P = (
        ('A', 'Activo'),
        ('S', 'Suspendido'),
        ('F', 'Finalizado'),
    )
    #id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Usuario, editable=False)  #usuario que lo creo
    cliente = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.SET_NULL)

    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion =  models.DateTimeField(auto_now_add=False)
    estado = models.CharField(max_length=1, choices=ESTADOS_P, default=SUSPENDIDO)
    fecha_ini = models.DateTimeField(auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now_add=False)  #fecha entrega estimada
    observacion = models.TextField()

    objects = ProyectoManager()

    REQUIRED_FIELDS = ['nombre', 'observacion']

    def __unicode__(self):
        return self.nombre

    def get_nombre(self):
        return self.nombre

    def get_observacion(self):
        return self.observacion