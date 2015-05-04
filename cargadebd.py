#from rest_framework import generics, permissions
#from rest_framework import views
#from rest_framework.response import Response
#from rest_framework import status
#from rest_framework import serializers
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

from decimal import Decimal

from django.contrib.auth.models import User

from authentication.models import Usuario, Proyecto, Flujo, Actividad, Sprint, UserStory

from authentication.serializers import UsuarioSerializer, ProyectoSerializer, FlujoSerializer, ActividadSerializer, SprintSerializer, UserStorySerializer, UserSerializer

user1 = User.objects.get(pk=1)
user2 = User.objects.get(pk=2)
user3 = User.objects.get(pk=3)
user4 = User.objects.get(pk=4)
user5 = User.objects.get(pk=5)

usuario1 = Usuario(id=1, user=user1, nombre='Jesus', apellido='Aguilar', correo=user1.email, telefono='123', direccion='calle23', tipo='C')
usuario1.save()
usuario2 = Usuario(id=2, user=user2, nombre='Ana', apellido='Lesme', correo=user1.email, telefono='567', direccion='colon567', tipo='E')
usuario2.save()
usuario3 = Usuario(id=3, user=user3, nombre='Juan', apellido='Gomez', correo=user1.email, telefono='0987', direccion='Herrera253', tipo='C')
usuario3.save()
usuario4 = Usuario(id=4, user=user4, nombre='Osvaldo', apellido='Sousa', correo=user1.email, telefono='847', direccion='Brizuela598', tipo='E')
usuario4.save()
usuario5 = Usuario(id=5, user=user5, nombre='Belen', apellido='Britez', correo=user1.email, telefono='867', direccion='Diaz345', tipo='E')
usuario5.save()

proyecto1 = Proyecto(id=1, nombre='Proyecto1', owner=user1, cliente=usuario1, fecha_ini='2015-06-28 23:03:05.654997-04', fecha_fin= '2015-09-25 23:03:05.654997-04')
proyecto1.save()
proyecto2 = Proyecto(id=2, nombre='Proyecto2', owner=user2, cliente=usuario2, fecha_ini='2015-07-28 23:03:05.654997-04', fecha_fin= '2015-09-28 23:03:05.654997-04')
proyecto2.save()
proyecto3 = Proyecto(id=3, nombre='Proyecto3', owner=user3, cliente=usuario3, fecha_ini='2015-06-22 23:03:05.654997-04', fecha_fin= '2015-09-25 23:03:05.654997-04')
proyecto3.save()
proyecto4 = Proyecto(id=4, nombre='Proyecto4', owner=user4, cliente=usuario4, fecha_ini='2015-07-25 23:03:05.654997-04', fecha_fin= '2015-09-18 23:03:05.654997-04')
proyecto4.save()
proyecto5 = Proyecto(id=5, nombre='Proyecto5', owner=user5, cliente=usuario5, fecha_ini='2015-08-10 23:03:05.654997-04', fecha_fin= '2015-10-28 23:03:05.654997-04')
proyecto5.save()

sprint1 = Sprint(id=1, owner=user1, proyecto=proyecto1, fecha_ini='2015-06-28 23:03:05.654997-04')
sprint1.save()
sprint2 = Sprint(id=2, owner=user2, proyecto=proyecto2, fecha_ini='2015-07-28 23:03:05.654997-04', duracionHoras=100)
sprint2.save()
sprint3 = Sprint(id=3, owner=user3, proyecto=proyecto3, fecha_ini='2015-06-22 23:03:05.654997-04', duracionHoras=150)
sprint3.save()
sprint4 = Sprint(id=4, owner=user4, proyecto=proyecto4, fecha_ini='2015-07-25 23:03:05.654997-04', duracionHoras=90)
sprint4.save()
sprint5 = Sprint(id=5, owner=user5, proyecto=proyecto5, fecha_ini='2015-08-10 23:03:05.654997-04', duracionHoras=125)
sprint5.save()

flujo1 = Flujo(id=1, owner=user1, nombre='Proyecto1',proyecto=proyecto1)
flujo1.save()
flujo2 = Flujo(id=2, owner=user1, nombre='Proyecto1',proyecto=proyecto1)
flujo2.save()
flujo3 = Flujo(id=3, owner=user2, nombre='Proyecto2',proyecto=proyecto2)
flujo3.save()
flujo4 = Flujo(id=4, owner=user3, nombre='Proyecto3',proyecto=proyecto3)
flujo4.save()
flujo5 = Flujo(id=5, owner=user3, nombre='Proyecto3',proyecto=proyecto3)
flujo5.save()
flujo6 = Flujo(id=6, owner=user4, nombre='Proyecto4',proyecto=proyecto4)
flujo6.save()
flujo7 = Flujo(id=7, owner=user5, nombre='Proyecto5',proyecto=proyecto5)
flujo7.save()

actividad1 = Actividad(id=1, owner=user1, nombre='AnalisisCaso', flujo=flujo1, orden=1)
actividad1.save()
actividad2 = Actividad(id=2, owner=user1, nombre='AnalisisEmpresa', flujo=flujo1, orden=2)
actividad2.save()
actividad3 = Actividad(id=3, owner=user1, nombre='AnalisisRequerimientos', flujo=flujo1, orden=3)
actividad3.save()
actividad4 = Actividad(id=4, owner=user1, nombre='AnalisisSistema', flujo=flujo1, orden=4)
actividad4.save()
actividad5 = Actividad(id=5, owner=user1, nombre='DisenhoCasodeUso', flujo=flujo2, orden=1)
actividad5.save()
actividad6 = Actividad(id=6, owner=user1, nombre='DisenhoUML', flujo=flujo2, orden=2)
actividad6.save()
actividad7 = Actividad(id=7, owner=user1, nombre='DisenhoSistema', flujo=flujo2, orden=3)
actividad7.save()
actividad8 = Actividad(id=8, owner=user2, nombre='Programacion', flujo=flujo3, orden=1)
actividad8.save()
actividad9 = Actividad(id=9, owner=user2, nombre='Testing', flujo=flujo3, orden=2)
actividad9.save()
actividad10 = Actividad(id=10, owner=user2, nombre='Despliegue', flujo=flujo3, orden=3)
actividad10.save()

us1 = UserStory(id=1, flujo_actual=flujo1, sprint=sprint1, actividad_actual=actividad1, owner=user1, prioridad= 15, fecha_ini='2015-06-28 23:03:05.654997-04', fecha_fin='2015-07-04 23:03:05.654997-04', valorNegocio=800, valorTecnico=10)
us1.save()
us2 = UserStory(id=2, flujo_actual=flujo3, sprint=sprint2, actividad_actual=actividad8, owner=user2, prioridad= 15, fecha_ini='2015-07-28 23:03:05.654997-04', tamanho=40, fecha_fin='2015-08-07 23:03:05.654997-04', valorNegocio=700, valorTecnico=15)
us2.save()
us3 = UserStory(id=3, flujo_actual=flujo3, sprint=sprint2, actividad_actual=actividad8, owner=user2, prioridad= 15, fecha_ini='2015-07-28 23:03:05.654997-04', tamanho=40, fecha_fin='2015-09-25 23:03:05.654997-04', valorNegocio=600, valorTecnico=15)
us3.save()

