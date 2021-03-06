from django.db import models
from authentication.models import Usuario
from sprints.models import Sprint
from flujos.models import Flujo
from proyectos.models import Proyecto
from flujos.models import Actividad
from utilitarios.models import Utils


class UserStoryManager(models.Manager):
    def crear_us(self, **kwargs):

        if not kwargs.get('nombre'):
            raise ValueError('Debe existir un nombre de US')

        if not kwargs.get('owner_id'):
            raise ValueError('Debe existir un Usuario responsable')
        else:
            owner = Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
            if owner == None:
                print('No existe el usuario')
                return Utils.NO_ENCONTRADO

        if not kwargs.get('proyecto_id'):
            raise ValueError('Debe existir un Proyecto')
        else:
            proyecto = Proyecto.objects.buscar_proyecto(id=kwargs.get('proyecto_id'))
            if proyecto == None:
                print('No existe el proyecto')
                return Utils.NO_ENCONTRADO

        print('testeando la fecha')
        print(kwargs.get('fecha_ini'))
        print('paso la prueba')

        if not kwargs.get('fecha_ini'):
            raise ValueError('Debe existir una Fecha de Inicio')
        else:
            fecha_ini = kwargs.get('fecha_ini')

        if not kwargs.get('fecha_fin'):
            raise ValueError('Debe existir una Fecha de Fin')

        if not kwargs.get('valorNegocio'):
            raise ValueError('Debe existir un valor de negocio')

        if not kwargs.get('valorTecnico'):
            raise ValueError('Debe existir un valor tecnico')

        if not kwargs.get('descripcionL'):
            descriplarga = ''
        else:
            descriplarga = kwargs.get('descripcionL')

        if not kwargs.get('descripcionC'):
            raise ValueError('Debe existir una descripcion corta')

        if not kwargs.get('prioridad'):
            raise ValueError('Debe existir un valor de prioridad')

        if not kwargs.get('tamanho'):
            tamanho = Utils.objects.retornar_fecha(kwargs.get('fecha_fin')) - Utils.objects.retornar_fecha(fecha_ini)
            print(tamanho)
            tamanho = tamanho.days*8 + tamanho.seconds//3600
            print(tamanho)
        else:
            print('El tamanho unicamente se calcula.')
            raise ValueError('El tamanho unicamente se calcula')

        try:
            print('La fecha se cargo exitosamente: ' + fecha_ini)
            print(tamanho)
            #print(tamanho)
            #print(tamanho.hour)
            #print(tamanho.days)
        except:
            print('error!!')

        userstory = self.model(
            nombre=kwargs.get('nombre'),
            owner=owner,
            estado=UserStory.PENDIENTE,
            proyecto=proyecto,
            fecha_ini=Utils.objects.retornar_fecha(fecha_ini),
            fecha_fin=Utils.objects.retornar_fecha(kwargs.get('fecha_fin')),
            valorNegocio=kwargs.get('valorNegocio'),
            valorTecnico=kwargs.get('valorTecnico'),
            descripcionC=kwargs.get('descripcionC'),
            descripcionL=descriplarga,
            prioridad=kwargs.get('prioridad'),
            tamanho=tamanho,
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
            # Y verificar si es el final de un sprint para realizar los cambios
            if kwargs.get('nombre'):
                userstory.nombre = kwargs.get('nombre')

            if kwargs.get('valorNegocio'):
                userstory.valorNegocio = kwargs.get('valorNegocio')

            if kwargs.get('valorTecnico'):
                userstory.valorTecnico = kwargs.get('valorTecnico')

            if kwargs.get('descripcionC'):
                userstory.descripcionC = kwargs.get('descripcionC')

            if kwargs.get('descripcionL'):
                userstory.descripcionL = kwargs.get('descripcionL')

            if kwargs.get('tamanho'):
                userstory.fecha_fin = Utils.objects.retornar_fecha(kwargs.get('fecha_fin'))
                if userstory.fecha_fin > userstory.fecha_ini:
                    userstory.tamanho = userstory.fecha_fin - userstory.fecha_ini
                else:
                    raise ValueError('La fecha de finalizacion no puede ser menor o igual a la fecha de inicio.')

            if kwargs.get('prioridad'):
                userstory.prioridad = kwargs.get('prioridad')

            userstory.save()
        else:
            print('No se permiten modificar US que no tengan estado pendiente')
            return Utils.NO_PERMITIDO

    def asignar_us_sprint(self, id_us, id_sprint, **kwargs):
        sprint = Sprint.objects.buscar_sprint(id_sprint)
        userstory = UserStory.objects.buscar_userstory(id_us)
        if sprint != None and userstory != None:
            userstory.sprint = sprint
            if userstory.tamanho <= sprint.horasRest:
                sprint.horasRest = sprint.horasRest - userstory.tamanho
                userstory.save()
            else:
                print('No permitido; tamanho de US mayor al tiempo restate del sprint')
                return Utils.NO_PERMITIDO
        else:
            print('El US, Sprint o ambos no existe')
            return Utils.NO_ENCONTRADO

    def asignar_us_flujo(self, id_us, id_flujo, **kwargs):
        userstory = UserStory.objects.buscar_userstory(id_us)
        flujo = Flujo.objects.buscar_flujo(id_flujo)
        if flujo != None and userstory != None:
            if userstory.actividad_actual != None:
                actividad = Actividad.objects.filter(flujo=id_flujo, orden=1)
                if actividad != None:
                    userstory.flujo_actual = flujo
                    userstory.actividad_actual = actividad
                    userstory.save()
                else:
                    print('La Actividad no existe')
                    return Utils.NO_ENCONTRADO
            else:
                userstory.flujo_actual = flujo
        else:
            print('El US, Flujo o ambos no existen')
            return Utils.NO_ENCONTRADO

    def cambiar_estado_us(self, id, **kwargs):
        userstory = UserStory.objects.buscar_userstory(id)

        if userstory != None:
            if userstory.estado == UserStory.SUSPENDIDO and kwargs.get('estado') == UserStory.PENDIENTE:
                userstory.estado = kwargs.get('estado')
            elif userstory.estado == UserStory.PENDIENTE and kwargs.get('estado') == UserStory.SUSPENDIDO:
                userstory.estado = kwargs.get('estado')
            elif userstory.estado == UserStory.PENDIENTE and kwargs.get('estado') == UserStory.FINALIZADO:
                userstory.estado = kwargs.get('estado')
            else:
                print('No esta permitido')
                return Utils.NO_PERMITIDO

            userstory.save()
            return userstory
        else:
            print('El US no existe')
            return Utils.NO_ENCONTRADO

    # solo el Scrum llama a esta funcion
    def verificar_us(self, id, **kwargs):
        userstory = UserStory.objects.buscar_userstory(id)

        if userstory != None:
            if userstory.estado == UserStory.FINALIZADO:
                userstory.confirmado = kwargs.get(
                    'confirmado') == 'True'  # es true cuando confirmado = True si es False es False
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
                        if max + 1 == a.orden:
                            id_sigte_act = a.id

                    if userstory.actividad_actual.cantidadUS == 0:
                        if userstory.actividad_actual.orden == 1:
                            Actividad.objects.cambiar_estado_actividad(id=userstory.actividad_actual,
                                                                       estado=Actividad.DONE)
                        else:
                            # conseguir la actividad anterior
                            id_ant_act = -1
                            for a in actividades:
                                if max - 1 == a.orden:
                                    id_ant_act = a.id

                            if id_ant_act != -1:
                                actividadAnterior = Actividad.objects.buscar_actividad(id=id_ant_act)
                                if actividadAnterior != None:
                                    if actividadAnterior.estado == Actividad.DONE:
                                        Actividad.objects.cambiar_estado_actividad(id=userstory.actividad_actual,
                                                                                   estado=Actividad.DONE)
                                else:
                                    print('La Actividad no existe')
                                    return Utils.NO_ENCONTRADO
                            else:
                                print('No existe actividad anterior')

                    if id_sigte_act != -1:
                        userstory.actividad_actual = id_sigte_act

            userstory.save()
        else:
            print('El US no existe')
            return Utils.NO_ENCONTRADO

            # def registrar_actividad(self):
            #    print('se registra')

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
    owner = models.ForeignKey(Usuario, related_name='US_Owner', null=True)  # , editable=False)  # usuario que lo creo
    flujo_actual = models.ForeignKey(Flujo, related_name='US_Flujo', null=True)  # , editable=True)
    sprint = models.ForeignKey(Sprint, related_name='US_Sprint', null=True)  # , editable=True)
    actividad_actual = models.ForeignKey(Actividad, related_name='US_Actividad', null=True)  # , editable=True)
    proyecto = models.ForeignKey(Proyecto, related_name='US_Proyecto')
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADOS_US, default=PENDIENTE)
    # La US debera tener uno de los siguientes tres estados:
    # P (Pendiente): La US aun tiene trabajo pendiente a realizar y no cumple todavia las expectativas de los clientes.
    # S (Suspendido): La US fue suspendida y ya no se realiza trabajo sobre la misma.
    # F (Finalizado): La US fue finalizada exitosamente y cumple todas las expectativas de los clientes.
    valorNegocio = models.IntegerField(default=0)
    valorTecnico = models.IntegerField(default=0)
    descripcionC = models.CharField(max_length=350)
    descripcionL = models.CharField(max_length=750)

    fecha_ini = models.DateTimeField(auto_now_add=False, null=True)
    fecha_fin = models.DateTimeField(auto_now_add=False, null=True)

    # prioridad es un valor que va 1 a 10 y cuanto mayor sea el valor tendra mayor prioridad
    prioridad = models.IntegerField(default=1)
    tamanho = models.DecimalField(max_digits=20, decimal_places=5, default=0.0)#.IntegerField(default=0)
    horasregistradas = models.IntegerField(default=0)
    confirmado = models.BooleanField(default=False)
    revisado = models.BooleanField(default=False)

    objects = UserStoryManager()

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

    def get_fecha_ini(self):
        return self.fecha_ini

    def get_fecha_fin(self):
        return self.fecha_fin

    def get_descripcionL(self):
        return self.descripcionL

