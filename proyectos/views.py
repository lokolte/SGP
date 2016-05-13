from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from authentication.models import Usuario
from rest_framework.permissions import IsAuthenticated
from utilitarios.models import Utils, Resultados
from authentication.permisos import EsEmpleado, EsCliente, EsScrumMaster, EsClienteScrumMasterProyecto
from rest_framework.decorators import detail_route, list_route, api_view
from authentication.serializers import UsuarioSerializer

from proyectos.models import Proyecto
from proyectos.serializers import ProyectoSerializer

# Create your views here.


class ProyectoViewSet(viewsets.ModelViewSet): # view para los objetos
    lookup_field = 'id'
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    # def get_permissions(self):
    #    return (permissions.AllowAny(), )

    def create(self, request, *args, **kwargs): #oficialmente es el post para crear
        print('Intentando crear objecto')
        serializer = self.serializer_class(data=request.data)
        print('serializer estado?')
        print(serializer)
        print('0')
        print(request.data)
        print('1')
        data = json.loads(request.data)

        #print(request.body)
        print('2')
        print(data)
        print('3')
        print(data.get('estado'))
        print('4')
        print(serializer.is_valid())
        print('serializer valido?')

        print(serializer.data)

        if serializer.is_valid():
            Proyecto.objects.crear_proyecto(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(Utils.objects.definir_respuesta(result=Utils.BAD_REQUEST).to_json(), status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs): #oficialmente este es el get
        print('llega? nose nada de este retrieve')
        #print(request.body)
        return Response(Utils.objects.definir_respuesta(Utils.RESPUESTSA_EXITOSA).to_json(), status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs): #oficialmente este es el put
        print('aca? 2')
        print(self.get_object())
        print('Entremedio..')
        print(request.body)
        print(request.data)
        print('hasta aquiii')
        proyecto = self.get_object()
        print(proyecto)

        print(ProyectoSerializer(proyecto).data)
        print('Comprobando..')
        serializer = ProyectoSerializer(self.get_object(), data=request.data)
        print('holaaa')
        print(serializer.is_valid())
        if serializer.is_valid():
            print('ENtro??')
            Proyecto.objects.modificar_proyecto(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)

        return Response(Utils.objects.definir_respuesta(result=Utils.BAD_REQUEST).to_json(), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):

        try:

            proyecto = self.get_object()

            print('Se suspende el proyecto ' + proyecto.nombre + ' por el usuario') #  + request.user + '.')

            print('Se notifica a los implicados...')

            resultado = Proyecto.objects.cambiar_estado(id=proyecto.id, estado=Proyecto.SUSPENDIDO)
            return Response(Utils.objects.definir_respuesta(result=resultado).to_json(), status=status.HTTP_202_ACCEPTED)

        except:
            print('No existe el proyecto.')
            return Response(Utils.objects.definir_respuesta(result=Utils.NO_ENCONTRADO).to_json(), status=status.HTTP_200_OK)


class ProyectoEstado(views.APIView): # oficialmente este es la forma de hacer los views personalizados

    def get_permissions(self):
        return (permissions.IsAuthenticated(), EsEmpleado(),)

    # /api/proyecto/:id/estado {estado: 'estado'}
    def post(self, request, pk, pk2, format=None):
        print('llega la peticion?')
        print('EL valor de pk es: ' + pk + ' el valor de pk2 es: ' + pk2)
        data = json.loads(request.body)
        print(request.body)
        print(data)
        print(data.get('estado'))

        try:
            print('intentando')
            return Response(Utils.objects.definir_respuesta(Utils.RESPUESTSA_EXITOSA).to_json(), status=status.HTTP_200_OK)
        except:

            return Response(Utils.objects.definir_respuesta(Utils.RESPUESTSA_EXITOSA).to_json(), status=status.HTTP_200_OK)


class cualquiera(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):

        print('entro en la peticion?? de cualquiera..')

        return Response({'message': 'peticion success'}, status=status.HTTP_204_NO_CONTENT)