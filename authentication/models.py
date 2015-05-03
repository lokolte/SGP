from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#########    Usuario     ############

class Usuario(models.Model):
    # Un usuario tendra un nombre identificador, contrasenha, estado, tipo de usuario, nombre,
    # apellido, direccion de correo electronico, numeros de telefono, direccion del domicilio.
    ESTADOS_U = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
    TIPOS_U = (
        ('C', 'Cliente'),
        ('E', 'Empleado')
    )
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=75)

    telefono = models.TextField()
    direccion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  #fecha de creacion de usuario
    #El usuario debera tener uno de los siguientes dos estados:
    #A (Activo): El usuario esta habilitado para utilizar el sistema.
    #I (Inactivo): El usuario no esta habilitado para utilizar el sistema
    estado = models.CharField(max_length=1, choices=ESTADOS_U, default='A')
    tipo = models.CharField(max_length=1, choices=TIPOS_U)  #tipo empleado o cliente setteado en el post al crear

##############################    Proyecto    ########################################

class Proyecto(models.Model):
    # Un proyecto tendra un codigo identificador, nombre, estado, clientes, fecha de inicio,
    # fecha estimada de finalizacion, informacion de sincronizacion del versionador y observaciones.
    ESTADOS_P = (
        ('A', 'Activo'),
        ('S', 'Suspendido'),
        ('F', 'Finalizado'),
    )
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, editable=False)  #usuario que lo creo
    cliente = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.SET_NULL)  #usuario que lo creo

    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #El proyecto debera tener uno de los siguientes tres estados:
    # A (Activo): El proyecto se encuentra en desarrollo.
    # S (Suspendido): El proyecto fue suspendido.
    # F (Finalizado): El proyecto fue finalizado exitosamente.
    estado = models.CharField(max_length=1, choices=ESTADOS_P, default='S')
    #El estado por defecto de un proyecto sera'Suspendido' hasta que se cree un flujo,
    # clientes = usuario
    fecha_ini = models.DateTimeField(auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now_add=False)  #fecha entrega estimada
    observaciones = models.TextField()


#######################    Flujo         ########################
class Flujo(models.Model):
    # Un flujo tendra un codigo identificador, nombre, estado, actividades y observaciones.
    ESTADOS_F = (
        ('TD', 'To_Do'),
        ('DG', 'Doing'),
        ('DN', 'Done'),
    )
    id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, editable=False)  #Proyecto al que corresponde el flujo
    owner = models.ForeignKey(Usuario, editable=False)  #usuario que lo creo

    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.TextField(max_length=2, choices=ESTADOS_F, default='TD')
    observaciones = models.TextField()


#######################    Actividades    #######################
class Actividad(models.Model):
    # Una actividad tendra un codigo identificador unico, flujo, estado, conjunto de US.
    #Los estados seran estaticos: To do. Doing. Done.
    ESTADOS_A = (
        ('TD', 'To_Do'),
        ('DG', 'Doing'),
        ('DN', 'Done'),
    )
    id = models.AutoField(primary_key=True)
    flujo = models.ForeignKey(Flujo, editable=False)  #Flujo al que corresponde la actividad
    owner = models.ForeignKey(Usuario, editable=False)  #usuario que lo creo

    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.TextField(max_length=2, choices=ESTADOS_A, default='TD')
    orden = models.DecimalField(max_digits=4, decimal_places=0, default=0)

#######################        UserStorys         #######################

class Sprint(models.Model):
    ESTADOS_S = (
        ('A', 'Activo'),
        ('C', 'Cerrado'),
    )
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Usuario, editable=False)  # usuario que lo creo
    proyecto = models.ForeignKey(Proyecto, editable=False)  # proyecto a quien pertenece
    #El sprint debera tener uno de los siguientes dos estados:
      #A (Activo): El sprint se encuentra activo.
      #C (Cerrado): El sprint se encuentra cerrado.
    estado = models.CharField(max_length=1, choices=ESTADOS_S, default='P')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ini = models.DateTimeField(auto_now_add=False)
    duracionHoras = models.DecimalField(max_digits=6, decimal_places=2)


class UserStory(models.Model):
    # US tendra un codigo identificador, descripcion corta para visualizacion y
    # una larga para detallar el trabajo a realizar, prioridad,
    # tamanho, estado, fecha de creacion, fecha de entrega estimada,
    # archivos adjuntos, usuario asignado, el flujo actual con la actividad y
    # el estado dentro del mismo, un historial de trabajo realizado y un historial
    # de modificaciones realizados sobre la US.
    ESTADOS_US = (
        ('P', 'Pendiente'),
        ('S', 'Suspendido'),
        ('F', 'Finalizado'),
    )
    id = models.AutoField(primary_key=True)
    flujo_actual = models.ForeignKey(Flujo, editable=False)
    sprint = models.ForeignKey(Sprint, editable=False)
    actividad_actual = models.ForeignKey(Actividad, editable=False)
    owner = models.ForeignKey(Usuario, editable=False)  # usuario que lo creo

    descripcionC = models.CharField(max_length=50)
    descripcionL = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    prioridad = models.DecimalField(max_digits=1, decimal_places=0)
    tamanho = models.DecimalField(max_digits=6, decimal_places=2)
    # La US debera tener uno de los siguientes tres estados:
    # P (Pendiente): La US aun tiene trabajo pendiente a realizar y no cumple todavia las expectativas de los clientes.
    # S (Suspendido): La US fue suspendida y ya no se realiza trabajo sobre la misma.
    # F (Finalizado): La US fue finalizada exitosamente y cumple todas las expectativas de los clientes.
    estado = models.CharField(max_length=1, choices=ESTADOS_US, default='P')
    fecha_ini = models.DateTimeField(auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now_add=False)  #fecha entrega estimada


