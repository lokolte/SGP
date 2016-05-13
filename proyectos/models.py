from authentication.models import Usuario
from django.db import models
from utilitarios.models import Utils
# Create your models here.

class ProyectoManager(models.Manager):
    #recibe nombre, owner_id, cliente_id, fecha_ini, fecha_fin,
    #/api/proyectos/new {proyecto}
    def crear_proyecto(self, **kwargs):

        if not kwargs.get('nombre'):
            print('Debe existir un nombre de Proyecto')
            return Utils.ERROR

        if not kwargs.get('owner_id'):
            print('Debe existir un Usuario responsable')
            return Utils.ERROR
        else:
            owner = Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
            if owner == None:
                print('No existe el owner')
                return Utils.NO_ENCONTRADO

        if not kwargs.get('cliente_id'):
            print('Debe existir un cliente de Proyecto')
            return Utils.ERROR
        else:
            cliente = Usuario.objects.buscar_usuario(id=kwargs.get('cliente_id'))
            if cliente == None:
                print('No existe el cliente')
                return Utils.NO_ENCONTRADO

        if not kwargs.get('fecha_ini'):
            print('Debe existir una Fecha de Inicio')
            return Utils.ERROR

        if not kwargs.get('fecha_fin'):
            print('Debe existir una Fecha de Fin Estimado')
            return Utils.ERROR

        if not kwargs.get('estado'):
            estado = Proyecto.SUSPENDIDO
        else:
            if kwargs.get('estado') == Proyecto.ACTIVO:
                estado = Proyecto.ACTIVO
            else:
                estado = Proyecto.SUSPENDIDO

        if not kwargs.get('observacion'):
            print('Debe existir una observacion')
            return Utils.ERROR

        proyecto = self.model(
            nombre=kwargs.get('nombre'),
            owner=owner,
            estado=estado,
            cliente=cliente,
            fecha_ini=Utils.objects.retornar_fecha(kwargs.get('fecha_ini')),
            fecha_fin=Utils.objects.retornar_fecha(kwargs.get('fecha_fin')),
            observacion=kwargs.get('observacion'),
        )
        proyecto.save()
        return proyecto

    #/api/proyectos/get {id:#}
    def buscar_proyecto(self, id):
        try:
            return Proyecto.objects.get(pk=id)
        except Proyecto.DoesNotExist:
            return None

    #/api/proyectos/mod {id:#,{proyecto}}
    def modificar_proyecto(self, id=None, **kwargs):

        proyecto = Proyecto.objects.buscar_proyecto(id)
        print ('Modificando datos del proyecto: ' + proyecto.nombre)
        if proyecto != None:
            if proyecto.estado == Proyecto.ACTIVO:
                #solo se cambian los campos que no es estado y solo si el proyecto esta activo
                proyecto.nombre = kwargs.get('nombre')
                proyecto.observacion = kwargs.get('observacion')
                proyecto.fecha_fin = Utils.objects.retornar_fecha(kwargs.get('fecha_fin'))
                proyecto.save()
                print(proyecto)
                return proyecto
            else:
                return Utils.NO_PERMITIDO
        else:
            print('No existe el proyecto')
            return Utils.NO_ENCONTRADO

    #/api/proyectos/estado {id:#, estado: "estado"}
    #solo ejecuta el metodo si es el SCRUM MASTER
    def cambiar_estado(self, id, **kwargs):
        #cambiar el estado solo si no esta finalizado
        proyecto = Proyecto.objects.buscar_proyecto(id)

        print(proyecto.estado)

        if proyecto != None:

            if proyecto.estado == kwargs.get('estado'):
                print('Sin cambios')
                return Utils.SIN_EFECTOS

            elif proyecto.estado == Proyecto.ACTIVO:

                if kwargs.get('estado') == Proyecto.SUSPENDIDO or kwargs.get('estado') == Proyecto.FINALIZADO:
                    proyecto.estado = kwargs.get('estado')
                    proyecto.save()
                    return proyecto

            elif proyecto.estado == Proyecto.SUSPENDIDO:

                if kwargs.get('estado') == Proyecto.ACTIVO:
                    proyecto.estado = kwargs.get('estado')
                    proyecto.save()
                    return proyecto

                elif kwargs.get('estado') == Proyecto.FINALIZADO:
                    print('No esta permitido')
                    return Utils.NO_PERMITIDO

            else:
                print('No esta permitido')
                return Utils.NO_PERMITIDO

        else:
            print('No existe el proyecto')
            return Utils.NO_ENCONTRADO

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
    #cliente = models.ForeignKey(Usuario, related_name='Cliente_Proyecto', blank=True, null=True, on_delete=models.SET_NULL)
    #miembros = models.ManyToManyField(Usuario, related_name='Empleado_Proyecto', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
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

    def get_fecha_ini(self):
        return self.fecha_ini

    def get_fecha_fin(self):
        return self.fecha_fin

    def get_estado(self):
        return self.estado