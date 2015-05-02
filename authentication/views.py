from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers import UserSerializer

from django.shortcuts import render
from confproyecto.models import Usuario, Proyecto, Sprint, Flujo, Actividad, UserStory
from confproyecto.serializers import UsuarioSerializer, ProyectoSerializer, SprintSerializer, FlujoSerializer, ActividadSerializer, UserStorySerializer
from django.http import Http404
from rest_framework.views import APIView

class UsuarioList(APIView):

    def get(self, request, format=None):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProyectoList(APIView):

    def get(self, request, format=None):
        proyectos = Proyecto.objects.all()
        serializer = ProyectoSerializer(proyectos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProyectoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProyectoDetail(APIView):

    def get_object(self, pk):
        try:
            return Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        proyecto = self.get_object(pk)
        serializer = ProyectoSerializer(proyecto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        proyecto = self.get_object(pk)
        serializer = ProyectoSerializer(proyecto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proyecto = self.get_object(pk)
        proyecto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SprintList(APIView):

    def get(self, request, format=None):
        sprints = Sprint.objects.all()
        serializer = SprintSerializer(sprints, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SprintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SprintDetail(APIView):

    def get_object(self, pk):
        try:
            return Sprint.objects.get(pk=pk)
        except Sprint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sprint = self.get_object(pk)
        serializer = SprintSerializer(sprint)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sprint = self.get_object(pk)
        serializer = SprintSerializer(sprint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sprint = self.get_object(pk)
        sprint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlujoList(APIView):

    def get(self, request, format=None):
        flujos = Flujo.objects.all()
        serializer = FlujoSerializer(flujos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FlujoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlujoDetail(APIView):

    def get_object(self, pk):
        try:
            return Flujo.objects.get(pk=pk)
        except Flujo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flujo = self.get_object(pk)
        serializer = FlujoSerializer(flujo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        flujo = self.get_object(pk)
        serializer = FlujoSerializer(flujo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flujo = self.get_object(pk)
        flujo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActividadList(APIView):

    def get(self, request, format=None):
        actividades = Actividad.objects.all()
        serializer = ActividadSerializer(actividades, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActividadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActividadDetail(APIView):

    def get_object(self, pk):
        try:
            return Actividad.objects.get(pk=pk)
        except Actividad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        actividad = self.get_object(pk)
        serializer = ActividadSerializer(actividad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        actividad = self.get_object(pk)
        serializer = ActividadSerializer(actividad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        actividad = self.get_object(pk)
        actividad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserStoryList(APIView):

    def get(self, request, format=None):
        userStories = UserStory.objects.all()
        serializer = UserStorySerializer(userStories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserStorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserStoryDetail(APIView):

    def get_object(self, pk):
        try:
            return UserStory.objects.get(pk=pk)
        except UserStory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userStory = self.get_object(pk)
        serializer = UserStorySerializer(userStory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userStory = self.get_object(pk)
        serializer = UserStorySerializer(userStory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userStory = self.get_object(pk)
        userStory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#    def get(self, request, format=None):
#        user = User.objects.all()
#        serializer = UserSerializer(user, many=True)
#        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(),)
        return (permissions.AllowAny(),)


class UserDetailAPIView(views.APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.is_valid = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)