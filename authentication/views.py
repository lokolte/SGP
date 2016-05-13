# coding=utf-8
import json
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from authentication.models import Usuario
from authentication.permisos import IsAccountOwner
from authentication.serializers import UsuarioSerializer
from utilitarios.models import Utils
from proyectos.models import Proyecto
from proyectos.serializers import ProyectoSerializer
from roles.models import Miembro

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    '''
    Conjunto de vistas que maneja el ABM de usuarios.
    '''
    #lookup_field = 'username'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        #Todos tienen permiso de crear su propia cuenta
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        #Solo el dueño de una cuenta puede hacer update() o delete()
        if self.request.method == 'DELETE':
            print('Checkeando permisos para eliminacion de cuentas')
            return  (permissions.IsAuthenticated(), IsAccountOwner())

        return (permissions.IsAuthenticated(), IsAccountOwner(),)


    def create(self, request, *args, **kwargs):
    #def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print('entroo')
            print(request.data)
            Usuario.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        print('no entro :(')
        result = Utils.objects.definir_respuesta(result=Utils.ERROR)
        return Response(result.to_json(), status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print('entroo')
            print(request.data)
            Usuario.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        print('no entro :(')
        result = Utils.objects.definir_respuesta(result=Utils.ERROR)
        return Response(result.to_json(), status=status.HTTP_400_BAD_REQUEST)
        #return Response()

    def destroy(self, request, *args, **kwargs):
        print('Usted ha intentado eliminar la cuenta de alguien')
        result = Utils.objects.definir_respuesta(result=Utils.NO_PERMITIDO)
        print(result.status + ' ' + result.message)
        return Response(
            result.to_json(),
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

class LoginView(views.APIView):

    def post(self, request, format=None):
        print('Llegada de solicitud..')
        data = json.loads(request.body)
        print(request.body)
        username = data.get('username', None)
        password = data.get('password', None)
        print('Procesando..')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:

            print(usuario.nombre)

            if usuario.activo: #.is_active:
                login(request, usuario)
                serialized = UsuarioSerializer(usuario)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'Esta cuenta de usuario ha sido deshabilitada'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Nombre de usuario o contraseña inválidos.'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):

        print('hizo logout kore')

        logout(request)

        return Response({'message': 'logout success'}, status=status.HTTP_204_NO_CONTENT)


class UsuariosConProyectos(views.APIView):

    def get_permissions(self):
        return (permissions.IsAuthenticated(),)

    #/api/user/:id/proyectos
    def post(self, request, pk, format=None):

        usuario = Usuario.objects.buscar_usuario(id=pk)

        try:
            if usuario != None:
                proyectos = Miembro.objects.retornar_lista_proyectos_de_usuario(usuario_id=usuario.id)
                print(proyectos)
                if proyectos != None and proyectos != []:

                    return Response(ProyectoSerializer(proyectos, many=True).data, status=status.HTTP_200_OK)
                else:
                    return Response(Utils.objects.definir_respuesta(Utils.NO_ENCONTRADO).to_json(), status=status.HTTP_404_NOT_FOUND)
        except:

            return Response(Utils.objects.definir_respuesta(Utils.BAD_REQUEST).to_json(), status=status.HTTP_400_BAD_REQUEST)
