from django.db import models
from authentication.models import Usuario
from sprints.models import Sprint
from flujos.models import Flujo
from proyectos.models import Proyecto
from flujos.models import Actividad

class USManager(models.Manager):

    def crear_us(self, **kwargs):

        if not kwargs.get('nombre'):
            raise ValueError('Debe existir un nombre de US')

        owner = Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
        if not owner:
            raise ValueError('Debe existir un Usuario responsable')

        if not kwargs.get('fecha_ini'):
            raise ValueError('Debe existir una Fecha de Inicio')

        if not kwargs.get('fecha_fin'):
            raise ValueError('Debe existir una Fecha de Fin')

        if not kwargs.get('valorNegocio'):
            raise ValueError('Debe existir un valor de negocio')

        if not kwargs.get('valorTecnico'):
            raise ValueError('Debe existir un valor tecnico')

        descriplarga=''
        if kwargs.get('descripcionL'):
            descriplarga= kwargs.get('descripcionL')

        if not kwargs.get('descripcionC'):
            raise ValueError('Debe existir una descripcion corta')

        if not kwargs.get('prioridad'):
            raise ValueError('Debe existir un valor de prioridad')

        if not kwargs.get('tamanho'):
            raise ValueError('Debe existir un tamanho en horas')


        userstory = self.model(
            nombre=kwargs.get('nombre'),
            owner=owner,
            estado=UserStory.PENDIENTE,
            fecha_ini=kwargs.get('fecha_ini'),
            fecha_fin=kwargs.get('fecha_fin'),
            valorNegocio=kwargs.get('valorNegocio'),
            valorTecnico=kwargs.get('valorTecnico'),
            descripcionC=kwargs.get('descripcionC'),
            descripcionL=descriplarga,
            prioridad=kwargs.get('prioridad'),
            tamanho=kwargs.get('tamanho'),
        )

        userstory.save()
        return userstory

    def buscar_userstory(self, id):
        try:
            return UserStory.objects.get(pk=id)
        except UserStory.DoesNotExist:
            return None

    def modificar_us(self, id, **kwargs):
        userstory = UserStory.objects.buscar_userstory(id)
        if userstory.estado == UserStory.PENDIENTE:
            #Y verificar si es el final de un sprint para realizar los cambios
            userstory.nombre = kwargs.get('nombre')
            userstory.valorNegocio = kwargs.get('valorNegocio')
            userstory.valorTecnico = kwargs.get('valorTecnico')
            userstory.descripcionC = kwargs.get('descripcionC')
            userstory.descripcionL = kwargs.get('descripcionL')
            userstory.tamanho = kwargs.get('tamanho')
            userstory.fecha_fin = kwargs.get('fecha_fin')
            userstory.prioridad = kwargs.get('prioridad')
        userstory.save()

    def cambiar_estado_us(self, id, **kwargs):
        userstory = UserStory.objects.buscar_userstory(id)#.get(id)
        if userstory.estado == UserStory.SUSPENDIDO and kwargs.get('estado') == UserStory.PENDIENTE:
            userstory.estado = kwargs.get('estado')
        elif userstory.estado == UserStory.PENDIENTE and kwargs.get('estado') == UserStory.SUSPENDIDO:
            userstory.estado = kwargs.get('estado')
        elif userstory.estado == UserStory.PENDIENTE and kwargs.get('estado') == UserStory.FINALIZADO:
            userstory.estado = kwargs.get('estado')
        else:
            print('No esta permitido')
        userstory.save()

    # solo el Scrum llama a esta funcion
    def verificar_us(self,id, **kwargs):
        userstory = UserStory.objects.buscar_userstory(id)
        if userstory.estado == UserStory.FINALIZADO:
            userstory.confirmado = kwargs.get('confirmado')
            userstory.revisado = True
            if userstory.confirmado == False:
                userstory.estado = UserStory.PENDIENTE
            elif userstory.confirmado == True:
                # un US pendiente menos
                userstory.actividad_actual.cantidadUS = userstory.actividad_actual.cantidadUS - 1
                actividades = Actividad.objects.all().filter(flujo=userstory.flujo_actual)
                # conseguir la sigte actividad
                max = userstory.actividad_actual.orden
                id_sigte_act = -1
                for a in actividades:
                    if max+1 == a.orden:
                        id_sigte_act = a.id
                if id_sigte_act != -1:
                    userstory.actividad_actual = id_sigte_act

                if userstory.actividad_actual.cantidadUS == 0:
                    if userstory.actividad_actual.orden == 1:
                        Actividad.objects.cambiar_estado_actividad(id=userstory.actividad_actual, estado=Actividad.DONE)
                    else:
                        # conseguir la actividad anterior
                        id_ant_act = -1
                        for a in actividades:
                            if max-1 == a.orden:
                                id_ant_act = a.id
                        actividadAnterior = Actividad.objects.buscar_actividad(id=id_ant_act)
                        if actividadAnterior != None:
                            if actividadAnterior.estado == Actividad.DONE:
                                Actividad.objects.cambiar_estado_actividad(id=userstory.actividad_actual, estado=Actividad.DONE)
        userstory.save()

    #def asignar_flujo()

class UserStory(models.Model):
    # US tendra un codigo identificador, descripcion corta para visualizacion y
    # una larga para detallar el trabajo a realizar, prioridad,
    # tamanho, estado, fecha de creacion, fecha de entrega estimada,
    # archivos adjuntos, usuario asignado, el flujo actual con la actividad y
    # el estado dentro del mismo, un historial de trabajo realizado y un historial
    # de modificaciones realizados sobre la US.
    PENDIENTE = 'P'
    SUSPENDIDO = 'S'
    FINALIZADO = 'F'
    ESTADOS_US = (
        ('P', 'Pendiente'),
        ('S', 'Suspendido'),
        ('F', 'Finalizado'),
    )
    nombre = models.CharField(max_length=100)
    owner = models.ForeignKey(Usuario,related_name='US_Owner', null=True)#, editable=False)  # usuario que lo creo
    flujo_actual = models.ForeignKey(Flujo, related_name='US_Flujo', null=True)#, editable=True)
    sprint = models.ForeignKey(Sprint, related_name='US_Sprint', null=True)#, editable=True)
    actividad_actual = models.ForeignKey(Actividad, related_name='US_Actividad', null=True)#, editable=True)
    proyecto = models.ForeignKey(Proyecto, related_name='US_Proyecto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=1, choices=ESTADOS_US, default=PENDIENTE)
    # La US debera tener uno de los siguientes tres estados:
    # P (Pendiente): La US aun tiene trabajo pendiente a realizar y no cumple todavia las expectativas de los clientes.
    # S (Suspendido): La US fue suspendida y ya no se realiza trabajo sobre la misma.
    # F (Finalizado): La US fue finalizada exitosamente y cumple todas las expectativas de los clientes.
    fecha_ini = models.DateTimeField(auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now_add=False)  #fecha entrega estimada
    valorNegocio = models.IntegerField(default=10)
    valorTecnico = models.IntegerField(default=10)
    descripcionC = models.CharField(max_length=50)
    descripcionL = models.CharField(max_length=150)
    prioridad = models.IntegerField(default=1)
    tamanho = models.IntegerField(default=50)
    confirmado = models.BooleanField(default=False)
    revisado = models.BooleanField(default=False)

    objects = USManager()

    REQUIRED_FIELDS = ['nombre', 'owner', 'fecha_ini', 'fecha_fin', 'tamanho', 'descripcionC']

    def __unicode__(self):
        return self.nombre

    def get_nombre(self):
        return self.nombre

    def get_descripcionC(self):
        return self.descripcionC

    def get_owner(self):
        return self.owner

    def get_estado(self):
        return self.estado

    def get_tamanho(self):
        return self.tamanho

    def fecha_ini(self):
        return self.fecha_ini

    def get_fecha_fin(self):
        return self.fecha_fin

    def get_descripcionL(self):
        return self.descripcionL

