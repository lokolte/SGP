# coding=utf-8
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

####
#from django.utils.six import BytesIO
####

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class UsuarioViewSet(viewsets.ModelViewSet):
    '''
    Conjunto de vistas que maneja el ABM de usuarios.
    '''
    lookup_field = 'username'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        #Todos tienen permiso de crear su propia cuenta
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        #Solo el dueño de una cuenta puede hacer update() o delete()
        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        #print('body: ' + request.body)
        #stream = BytesIO(request.data)
        #dato = JSONParser().parse(stream)
        #print('data: ' + dato)

        if serializer.is_valid():
            print('entroo')
            print(request.data)
            Usuario.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        print('no entro :(')
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)



class LoginView(views.APIView):
    def post(self, request, format=None):
        print('llego? antes?')
        data = json.loads(request.body)
        print(request.body)
        username = data.get('username', None)
        password = data.get('password', None)
        print('llego?')

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
        logout(request)

        return Response({'message': 'logout success'}, status=status.HTTP_204_NO_CONTENT)
