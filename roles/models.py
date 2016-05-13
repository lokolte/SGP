from django.db import models
from proyectos.models import Proyecto
from utilitarios.models import Utils
from authentication.models import Usuario

# Create your models here.
# cada usuario es miembro de un proyecto una sola vez con un rol en particular
# Existen N miembros como N proyectos en los que participa el usuario
class MiembroManager(models.Manager):

    def crear_miembro(self, **kwargs):

        if not kwargs.get('owner_id'):
            print('Debe existir un Usuario responsable')
            return Utils.ERROR
        else:
            owner = Usuario.objects.buscar_usuario(id=kwargs.get('owner_id'))
            if owner == None:
                print('No existe el owner')
                return Utils.NO_ENCONTRADO

        if not kwargs.get('usuario_id'):
            print('Debe existir un usuario miembro de Proyecto')
            return Utils.ERROR
        else:
            usuario = Usuario.objects.buscar_usuario(id=kwargs.get('usuario_id'))
            if usuario == None:
                print('No existe el usuario')
                return Utils.NO_ENCONTRADO


        if not kwargs.get('proyecto_id'):
            print('Debe existir un Proyecto')
            return Utils.ERROR
        else:
            proyecto = Proyecto.objects.buscar_proyecto(id=kwargs.get('proyecto_id'))
            if proyecto == None:
                print('No existe el proyecto')
                return Utils.NO_ENCONTRADO
            else:
                lista_miembros_usuario = Miembro.objects.buscar_miembro_por_up(usuario_id=usuario.id, proyecto_id=proyecto.id)
                for miembro in lista_miembros_usuario:
                    usuario_miembro = miembro.usuario
                    if usuario_miembro.id == usuario.id:
                        print('El usuario ya es miembro de este proyecto.. Nombre y Apellido: ' + usuario_miembro.nombre + ' ' + usuario_miembro.apellido)
                        return Utils.SIN_EFECTOS

        if not kwargs.get('rol'):
            tipo = Miembro.SIN_PERMISOS
        else:
            if kwargs.get('rol') == Miembro.EMPLEADO:
                tipo = Miembro.EMPLEADO
            elif kwargs.get('rol') == Miembro.SCRUM_MASTER:
                tipo = Miembro.SCRUM_MASTER
            elif kwargs.get('rol') == Miembro.CLIENTE:
                tipo = Miembro.CLIENTE
            else:
                return Utils.ERROR

        miembro = self.model(
            owner=owner,
            proyecto=proyecto,
            usuario=usuario,
            rol=tipo,
        )

        miembro.save()
        return miembro

    def crear_miembro_empleado(self, **kwargs):
        miembro = self.crear_miembro(**kwargs)
        try:
            miembro.rol = Miembro.EMPLEADO
            miembro.save()
            return miembro
        except:
            return miembro

    def crear_miembro_cliente(self, **kwargs):
        miembro = self.crear_miembro(**kwargs)
        try:
            miembro.rol = Miembro.CLIENTE
            miembro.save()
            return miembro
        except:
            return miembro

    def crear_miembro_scrum(self, **kwargs):
        miembro = self.crear_miembro(**kwargs)
        try:
            miembro.rol = Miembro.SCRUM_MASTER
            miembro.save()
            return miembro
        except:
            return miembro

    def buscar_miembro(self, id):
        try:
            return Miembro.objects.get(pk=id)
        except Miembro.DoesNotExist:
            return None

    def buscar_por_usuario(self, usuario_id):
        try:
            usuario = Usuario.objects.buscar_usuario(id=usuario_id)
            if usuario != None:
                return Miembro.objects.filter(usuario=usuario)
        except Usuario.DoesNotExist:
            return None

    def buscar_por_proyecto(self, proyecto_id):
        try:
            proyecto = Proyecto.objects.buscar_proyecto(id=proyecto_id)
            if proyecto != None:
                return Miembro.objects.filter(proyecto=proyecto)
        except Proyecto.DoesNotExist:
            return None

    def buscar_miembro_por_up(self, usuario_id, proyecto_id):
        try:
            usuario = Usuario.objects.buscar_usuario(id=usuario_id)
            proyecto = Proyecto.objects.buscar_proyecto(id=proyecto_id)
            if usuario != None and proyecto != None:
                return Miembro.objects.filter(usuario=usuario, proyecto=proyecto)
        except Miembro.DoesNotExist:
            return None

    def retornar_lista_proyectos_de_usuario(self, usuario_id):
        try:
            miembros = Miembro.objects.buscar_por_usuario(usuario_id=usuario_id)
            proyectos = []

            if miembros != None:
                for miembro in miembros:
                    proyectos.append(miembro.proyecto)

                return proyectos
            else:
                return None

        except Miembro.DoesNotExist:
            return None

    def existe_miembro(self, usuario_id, proyecto_id):
        try:
            usuario = Usuario.objects.buscar_usuario(id=usuario_id)
            proyecto = Proyecto.objects.buscar_proyecto(id=proyecto_id)
            if usuario != None and proyecto != None:
                return len(Miembro.objects.filter(usuario=usuario, proyecto=proyecto)) != 0
        except Miembro.DoesNotExist:
            return None

class Miembro(models.Model):
    CLIENTE = 'CL'
    SCRUM_MASTER = 'SM'
    EMPLEADO = 'EM'
    SIN_PERMISOS = 'SP'
    ROLES_PROYECTO = (
        ('CL', 'Cliente'),
        ('SM', 'Scrum_Master'),
        ('EM', 'Empleado'),
        ('SP', 'Sin_Permisos'),
    )
    owner = models.ForeignKey(Usuario, related_name='Usuario_Miembro', editable=False)  #usuario que lo creo
    proyecto = models.ForeignKey(Proyecto, related_name='Miembro_Proyecto', blank=True, null=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(Usuario, related_name='Miembro_Usuario', blank=True, null=True, on_delete=models.SET_NULL)

    rol = models.CharField(max_length=2, choices=ROLES_PROYECTO, default=EMPLEADO)

    objects = MiembroManager()

    REQUIRED_FIELDS = ['rol', 'owner', 'proyecto', 'usuario']

    def __unicode__(self):
        return self.rol

    def get_owner(self):
        return self.owner

    def get_usuario(self):
        return self.usuario

    def get_proyecto(self):
        return self.proyecto

    def get_rol(self):
        return self.rol