
from rest_framework import permissions
from authentication.models import Usuario

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False

class EsCliente(permissions.BasePermission):
    def has_permission(self, request, view):
        usuario = request.user
        if not usuario.tipo:
            return False
        return usuario.tipo==Usuario.T_CLIENTE

class EsEmpleado(permissions.BasePermission):
    def has_permission(self, request, view):
        usuario = request.user
        if not usuario.tipo:
            return False
        return usuario.tipo==Usuario.T_CLIENTE

