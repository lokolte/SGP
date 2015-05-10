from django.shortcuts import render
import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from authentication.models import Usuario
from authentication.permisos import IsAccountOwner, EsEmpleado
from authentication.serializers import UsuarioSerializer

from proyectos.models import Proyecto
from proyectos.serializers import ProyectoSerializer

# Create your views here.

class ProyectoViewSet(viewsets.ModelViewSet):
    lookup_field = 'nombre'
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    def get_permissions(self):
        return (permissions.AllowAny(), )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Proyecto.crear_proyecto(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'No se pudo crear Proyecto.'
        }, status=status.HTTP_400_BAD_REQUEST)

