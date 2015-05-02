from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#########    Usuario     ############
class EUoo(models.Model):
    ESTADOS_U = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )
class TUoo():
    TIPOS_U = (
        ('C', 'Cliente'),
        ('E', 'Empleado')
    )

class Usuario(models.Model):
    #Un usuario tendrá un nombre identificador, contraseña, estado, tipo de usuario, nombre,
    # apellido, dirección de correo electrónico, números de teléfono, dirección del domicilio.
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=75)

    telefono = models.TextField
    direccion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True) #fecha de creacion de usuario
    #El usuario deberá tener uno de los siguientes dos estados:
        #A (Activo): El usuario está habilitado para utilizar el sistema.
        #I (Inactivo): El usuario no está habilitado para utilizar el sistema
    estado = models.CharField(max_length=1, choices=EUoo.ESTADOS_U, default= 'A')
    tipo = models.CharField(max_length=1, choices=TUoo.TIPOS_U) #tipo empleado o cliente setteado en el post al crear

##############################    Proyecto    ########################################
class EPoo(models.Model):
    ESTADOS_P = (
        ('A', 'Activo'),
        ('S', 'Suspendido'),
        ('F', 'Finalizado'),
    )

class Proyecto(models.Model):
    #Un proyecto tendrá un código identificador, nombre, estado, clientes, fecha de inicio,
    # fecha estimada de finalización, información de sincronización del versionador y observaciones.
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Usuario, editable=False)#usuario que lo creo
    cliente = models.ForeignKey(Usuario, editable=False)#usuario que lo creo

    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #El proyecto deberá tener uno de los siguientes tres estados:
     # A (Activo): El proyecto se encuentra en desarrollo.
     # S (Suspendido): El proyecto fue suspendido.
     # F (Finalizado): El proyecto fue finalizado exitosamente.
    estado = models.CharField(max_length=1, choices=EPoo.ESTADOS_P, default='S')
    #El estado por defecto de un proyecto será “Suspendido” hasta que se cree un flujo,
    # clientes = usuario
    fecha_ini = models.DateTimeField(auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now_add=False) #fecha entrega estimada
    observaciones = models.TextField()

#######################    Actividades    #######################
class EFoo(models.Model):
    ESTADOS_F = (
        ('TD', 'To_Do'),
        ('DG', 'Doing'),
        ('DN', 'Done'),
    )

#######################    Flujo         ########################
class Flujo(models.Model):
    #Un flujo tendrá un código identificador, nombre, estado, actividades y observaciones.
    id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, editable=False)#Proyecto al que corresponde el flujo
    owner = models.ForeignKey(Usuario, editable=False)#usuario que lo creo

    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=2, choices=EFoo.ESTADOS_F, default='TD')
    observaciones = models.TextField()


class Actividad(models.Model):
    #Una actividad tendrá un código identificador único, flujo, estado, conjunto de US.
    #Los estados serán estáticos: To do. Doing. Done.
    id = models.AutoField(primary_key=True)
    flujo = models.ForeignKey(Flujo, editable=False)#Flujo al que corresponde la actividad
    owner = models.ForeignKey(Usuario, editable=False)#usuario que lo creo

    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=2, choices=EFoo.ESTADOS_F, default='TD')

#######################        UserStorys         #######################
class EUSoo(models.Model):
    ESTADOS_US = (
        ('P', 'Pendiente'),
        ('S', 'Suspendido'),
        ('F', 'Finalizado'),
    )

class UserStory(models.Model):
    # US tendrá un código identificador, descripción corta para visualizacion y
    # una larga para detallar el trabajo a realizar, prioridad,
    # tamaño, estado, fecha de creación, fecha de entrega estimada,
    # archivos adjuntos, usuario asignado, el flujo actual con la actividad y
    # el estado dentro del mismo, un historial de trabajo realizado y un historial
    # de modificaciones realizados sobre la US.
    id = models.AutoField(primary_key=True)
    flujo_actual = models.ForeignKey(Flujo, editable=False)
    sprint = models.ForeignKey(Sprint, editable=False)
    actividad_actual = models.ForeignKey(Actividad, editable=False)
    owner = models.ForeignKey(Usuario, editable=False)#usuario que lo creo

    descripcionC = models.CharField(max_length=50)
    descripcionL = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    prioridad = models.DecimalField(max_digits=1)
    tamanho = models.DecimalField(max_digits=4)
    #La US deberá tener uno de los siguientes tres estados:
      # P (Pendiente): La US aún tiene trabajo pendiente a realizar y no cumple todavía las expectativas de los clientes.
      # S (Suspendido): La US fue suspendida y ya no se realiza trabajo sobre la misma.
      # F (Finalizado): La US fue finalizada exitosamente y cumple todas las expectativas de los clientes.
    estado = models.CharField(max_length=1, choices=EUSoo.ESTADOS_US, default='P')
    fecha_ini = models.DateTimeField(auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now_add=False) #fecha entrega estimada

class Sprint(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Usuario, editable=False)#usuario que lo creo
    proyecto = models.ForeignKey(Proyecto, editable=False)#proyecto a quien pertenece

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_ini = models.DateTimeField(auto_now_add=False)
    duracionHoras = models.DecimalField(max_digits=4)
