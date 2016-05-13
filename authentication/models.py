from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from utilitarios.models import Utils
#from roles.models import Miembro

# Create your models here.

class UsuarioManager(BaseUserManager):
    '''
       @cvar UsuarioManager: controlador de la clase B{Usuario}
       @param nombre de usuario
    '''

    def create_user(self, username, password=None, **kwargs):
        '''
        :param username: nombre del usuario del sistema
        @type username: string de 40 caracteres
        :param password: contrasenha del usuario
        @type password: string heredado del framework
        :param kwargs: otros datos
        :return: usuario
        '''
        if not username:
            print('Debe existir un nombre de usuario')
            return Utils.ERROR

        if not kwargs.get('email'):
            print('Debe tener una direccion de correo valida')
            return Utils.ERROR

        if not kwargs.get('nombre'):
            print('El usuario debe tener un nombre')
            return Utils.ERROR

        if not kwargs.get('apellido'):
            print('El usuario debe tener un apellido')
            return Utils.ERROR

        if not kwargs.get('telefono'):
            telefono = ''
        else:
            telefono = kwargs.get('telefono')

        if not kwargs.get('direccion'):
            direccion = ''
        else:
            direccion = kwargs.get('direccion')

        usuario = self.model(
            username=username,
            email=self.normalize_email(kwargs.get('email')),
            nombre=kwargs.get('nombre'),
            apellido=kwargs.get('apellido'),
            telefono=telefono,
            direccion=direccion
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, password=None, **kwargs):
        '''
        funcion B{crear superusuario} funcion para crear un superusuario
        @param username:: nombre del usuario del sistema
        @type username: string de 40 caracteres
        @param password: contrasenha del usuario
        @type password: string agregado por el framework
        @param kwargs: otros datos
        '''
        usuario = self.create_user(username, password, **kwargs)
        #usuario.tipo = Usuario.T_EMPLEADO

        usuario.is_admin = True
        usuario.save()
        return usuario

    def buscar_usuario(self, id):
        try:
            return Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            return None


class Usuario(AbstractBaseUser):
    '''
    @cvar Usuario: con I{nombre}, I{apellido}, I{email}, I{telefono}, I{direccion} y I{estado}
    I{email}, I{nombre} y I{apellido}
    I{nombre},I{apellido}: para I{get_nombre_completo}
    '''

    username = models.CharField(max_length=40, unique=True)

    nombre = models.CharField(max_length=40, blank=True)
    apellido = models.CharField(max_length=40, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=50, blank=True)

    ## el atributo activo representa el estado, si es activo o inactivo
    activo = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def __unicode__(self):
        return self.username

    def get_nombre_completo(self):
        return ''.join([self.nombre, self.apellido])

    def get_nombre(self):
        return self.nombre
