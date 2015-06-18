from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from authentication.models import Usuario
from rest_framework.permissions import IsAuthenticated
from utilitarios.models import Utils
from authentication.permisos import EsEmpleado, EsCliente, EsScrumMaster, EsClienteScrumMasterProyecto
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

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Proyecto.objects.crear_proyecto(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'No se pudo crear Proyecto.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Proyecto.objects.modificar_proyecto(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)

        return Response({
            'status': 'Bad request',
            'message': 'No se pudo modificar el Proyecto.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response({
            'status': 'Bad request',
            'message': 'No se pueden eliminar Proyectos.'
        }, status=status.HTTP_400_BAD_REQUEST)

class ProyectoOperations(views.APIView):
    permission_classes = (IsAuthenticated, EsScrumMaster,)
    #/api/proyectos/estado {id:#, estado: 'estado'}
    def post(self, request, format=None):
        data = json.loads(request.body)
        print(request.body)
        print(data)
        print(data.get('id'))

        id = -1

        try:
            print('buscando')
            respuesta = None
            id = data.get('id', None)
            estado = data.get('estado', None)
            print(estado)
            print('buscando')
            result = Proyecto.objects.cambiar_estado(id=id, estado=estado)
            print('buscando')
            result = Utils.objects.definirrespuesta(result=result)
            ser = ProyectoSerializer(result)
            print(ser.data)
            return Response(ser.data, status=status.HTTP_200_OK)
        except:
            print('buscando')
            result = {
                'status': 'Bad request',
                'message': 'Peticion invalida.'
            }
            print('buscando')
            return Response(result, status=status.HTTP_200_OK)

#/api/proyectos/modificar
class ModificarProyectos(views.APIView):
    permission_classes = (IsAuthenticated, EsScrumMaster,)
    #sirve para modificar proyectos {'nombre': "", 'observacion':"", fecha_fin:""}
    def post(self, request, format=None):
        data = json.loads(request.body)
        print(request.body)
        print(data)
        print(data.get('id'))

        try:

            id = data.get('id', None)
            nombre = data.get('nombre', None)
            observacion = data.get('observacion', None)
            fecha_fin = data.get('fecha_fin', None)
            print('buscando.. con datos: '+ id + ' ' + nombre+ ' '+ observacion+' '+ fecha_fin)

            result = Proyecto.objects.modificar_proyecto(id, nombre=nombre, observacion=observacion, fecha_fin=fecha_fin)
            metodo = Utils.objects.definirrespuesta(result=result)

            print('El resultado es: ' + metodo.status)

            if metodo.status == Utils.RESPUESTSA_EXITOSA:
                print(result)
                ser = ProyectoSerializer(result)
                result = ser.data
            else:
                result = {'status': metodo.status, 'message': metodo.message}
                #return Response(result, status=status.HTTP_200_O)

            print(result)

            return Response(result, status=status.HTTP_200_OK)
        except:
            print('buscando')
            result = {
                'status': 'Bad request',
                'message': 'Peticion invalida.'
            }
            print('buscando')
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
#/api/proyectos/get
class ObtenerProyectos(views.APIView):
    permission_classes = (IsAuthenticated, EsClienteScrumMasterProyecto,)
    #recibe {'id': #} //para buscar el proyecto
    def post(self, request, format=None):
        print('llego en en servidor?')
        data = json.loads(request.body)
        print(request.body)
        print(data)
        print(data.get('id'))

        try:
            print('buscando')
            id = data.get('id', None)
            print('buscando')
            result = Proyecto.objects.buscar_proyecto(id=id)
            print('buscando')
            ser = ProyectoSerializer(result)
            return Response(ser.data, status=status.HTTP_200_OK)
        except:
            print('buscando')
            result = {
                'status': 'Bad request',
                'message': 'Peticion de id Invalido.'
            }
            print('buscando')
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        print('llego en en servidor?')
        data = json.loads(request.body)
        print(request.body)
        print(data)
        print(data.get('id'))

        try:
            usuario = request.user
            if usuario.tipo == Usuario.T_CLIENTE:
                result = Proyecto.objects.filter(cliente=usuario)
            elif usuario.tipo == Usuario.T_EMPLEADO and usuario.is_admin:
                result = Proyecto.objects.all()
            elif usuario.tipo == Usuario.T_EMPLEADO:
                result = Proyecto.objects.filter(empleado=usuario)

            print('buscando')
            ser = ProyectoSerializer(result, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)
        except:
            print('buscando')
            result = {
                'status': 'Bad request',
                'message': 'Peticion de id Invalido.'
            }
            print('buscando')
            return Response(result, status=status.HTTP_400_BAD_REQUEST)