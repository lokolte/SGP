from rest_framework import permissions
from authentication.models import Usuario
import json
from proyectos.models import Proyecto
from proyectos.serializers import ProyectoSerializer
from roles.models import Miembro


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        if request.user:
            return user == request.user
        return False


class EsCliente(permissions.BasePermission):
    def has_object_permission(self, request, view, proyecto):
        miembro_proy = Miembro.objects.buscar_por_usuario(usuario_id=request.user.id).filter(proyecto_id=proyecto.id)
        print(miembro_proy.get_rol())
        return True

#class EsCliente(permissions.BasePermission):
#    def has_permission(self, request, view):
#        usuario = request.user
#        if not usuario.tipo:
#            return False
#        return usuario.tipo == Usuario.T_CLIENTE


class EsEmpleado(permissions.BasePermission):
    def has_permission(self, request, view):
        print('imprimio el primer permiso')
        return True

    #def has_permission(self, request, view):

        #print('entro?? reconoce permisos')
        #return True
        #usuario = request.user
        #if not usuario.tipo:
        #    return False
        #return usuario.tipo == Usuario.T_EMPLEADO


class EsScrumMaster(permissions.BasePermission):
    def has_permission(self, request, view):
        usuario = request.user
        if not usuario.tipo:
            return False
        return (usuario.tipo == Usuario.T_EMPLEADO) and usuario.is_admin

class EsClienteProyecto(permissions.BasePermission): # a cambiar con los roles y miembros
    def has_permission(self, request, view):
        data = json.loads(request.body)
        print(data)
        id = data.get('id', None)
        proyecto = Proyecto.objects.buscar_proyecto(id=id)
        ser = ProyectoSerializer(proyecto)
        print(ser.data)
        usuario = request.user
        if proyecto != None:
            if not usuario.tipo:
                    return False
            elif usuario.tipo == Usuario.T_CLIENTE:
                return proyecto.cliente.id == usuario.id
        else:
            return False

class EsClienteScrumMasterProyecto(permissions.BasePermission): # a cambiar
    def has_permission(self, request, view):
        data = json.loads(request.body)
        print(data)
        id = data.get('id', None)
        proyecto = Proyecto.objects.buscar_proyecto(id=id)
        usuario = request.user
        #ser = ProyectoSerializer(proyecto)
        #print(ser.data)

        #print(proyecto.cliente.id)
        print(usuario.id)

        if not usuario.tipo:
            print('Entro 1')
            return False
        else:
            #para saber si es Scrum Master
            if usuario.tipo == Usuario.T_EMPLEADO:
                return usuario.is_admin

            #para saber si es Cliente del proyecto
            if proyecto != None:
                if usuario.tipo == Usuario.T_CLIENTE:
                    print('Entro 2')
                    return proyecto.cliente.id == usuario.id
            else:
                print('Entro 4')
                return True