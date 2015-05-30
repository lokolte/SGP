#from rest_framework import generics, permissions
#from rest_framework import views
#from rest_framework.response import Response
#from rest_framework import status
#from rest_framework import serializers
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser

from decimal import Decimal

from django.contrib.auth.models import User

from authentication.models import Usuario
from proyectos.models import Proyecto
from flujos.models import Flujo, Actividad
from userstories.models import UserStory
from sprints.models import Sprint

#from authentication.serializers import UsuarioSerializer, ProyectoSerializer, FlujoSerializer, ActividadSerializer, SprintSerializer, UserStorySerializer, UserSerializer

#user1 = User.objects.get(pk=1)
#user2 = User.objects.get(pk=2)
#user3 = User.objects.get(pk=3)
#user4 = User.objects.get(pk=4)
#user5 = User.objects.get(pk=5)

#crear superuser hace a un usuario empleado y is_admin = true asi seria un Scrum Master siendo superuser
usuario1 = Usuario.objects.create_superuser(username='jesus', password='jesus',
                                            nombre='Jesus', apellido='Aguilar',
                                            email='jesus@gmail.com', telefono='123',
                                            direccion='calle23')
#usuario1.save()

usuario2 = Usuario.objects.crear_cliente(username='ana', password='ana',
                                            nombre='Ana', apellido='Lesme',
                                            email='ana@gmail.com', telefono='123',
                                            direccion='colo323')
#usuario2.save()

#usuario3 = Usuario(nombre='Juan', apellido='Gomez', correo=user1.email, telefono='0987', direccion='Herrera253', tipo='C')
#usuario3.save()
#usuario4 = Usuario(nombre='Osvaldo', apellido='Sousa', correo=user1.email, telefono='847', direccion='Brizuela598', tipo='E')
#usuario4.save()
#usuario5 = Usuario(nombre='Belen', apellido='Britez', correo=user1.email, telefono='867', direccion='Diaz345', tipo='E')
#usuario5.save()

proyecto1 = Proyecto(nombre='Proyecto1', owner_id=usuario1.id, cliente_id=usuario2.id,
                     fecha_ini='2015-06-28 23:03:05.654997-04',
                     fecha_fin= '2015-09-25 23:03:05.654997-04')
#proyecto1.save()

#proyecto2 = Proyecto(id=2, nombre='Proyecto2', owner=user2, cliente=usuario2, fecha_ini='2015-07-28 23:03:05.654997-04', fecha_fin= '2015-09-28 23:03:05.654997-04')
#proyecto2.save()
#proyecto3 = Proyecto(id=3, nombre='Proyecto3', owner=user3, cliente=usuario3, fecha_ini='2015-06-22 23:03:05.654997-04', fecha_fin= '2015-09-25 23:03:05.654997-04')
#proyecto3.save()
#proyecto4 = Proyecto(id=4, nombre='Proyecto4', owner=user4, cliente=usuario4, fecha_ini='2015-07-25 23:03:05.654997-04', fecha_fin= '2015-09-18 23:03:05.654997-04')
#proyecto4.save()
#proyecto5 = Proyecto(id=5, nombre='Proyecto5', owner=user5, cliente=usuario5, fecha_ini='2015-08-10 23:03:05.654997-04', fecha_fin= '2015-10-28 23:03:05.654997-04')
#proyecto5.save()

sprint1 = Sprint.objects.crear_sprint(owner_id=usuario1.id, proyecto_id=proyecto1.id,
                                      fecha_ini='2015-06-28 23:03:05',#.654997-04',
                                      duracionHoras=10.00)
#sprint1.save()

#sprint2 = Sprint(id=2, owner=user2, proyecto=proyecto2, fecha_ini='2015-07-28 23:03:05.654997-04', duracionHoras=100)
#sprint2.save()
#sprint3 = Sprint(id=3, owner=user3, proyecto=proyecto3, fecha_ini='2015-06-22 23:03:05.654997-04', duracionHoras=150)
#sprint3.save()
#sprint4 = Sprint(id=4, owner=user4, proyecto=proyecto4, fecha_ini='2015-07-25 23:03:05.654997-04', duracionHoras=90)
#sprint4.save()
#sprint5 = Sprint(id=5, owner=user5, proyecto=proyecto5, fecha_ini='2015-08-10 23:03:05.654997-04', duracionHoras=125)
#sprint5.save()

flujo1 = Flujo.objects.crear_flujo(owner_id=usuario1.id, nombre='Desarrollo',
               proyecto_id=proyecto1.id)
#flujo1.save()

#flujo2 = Flujo(id=2, owner=user1, nombre='Proyecto1', proyecto=proyecto1)
#flujo2.save()
#flujo3 = Flujo(id=3, owner=user2, nombre='Proyecto2', proyecto=proyecto2)
#flujo3.save()
#flujo4 = Flujo(id=4, owner=user3, nombre='Proyecto3', proyecto=proyecto3)
#flujo4.save()
#flujo5 = Flujo(id=5, owner=user3, nombre='Proyecto3', proyecto=proyecto3)
#flujo5.save()
#flujo6 = Flujo(id=6, owner=user4, nombre='Proyecto4', proyecto=proyecto4)
#flujo6.save()
#flujo7 = Flujo(id=7, owner=user5, nombre='Proyecto5', proyecto=proyecto5)
#flujo7.save()

actividad1 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='AnalisisCaso', flujo_id=flujo1.id, orden=1)

actividad2 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='AnalisisEmpresa', flujo_id=flujo1.id, orden=2)

actividad3 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='AnalisisRequerimientos', flujo_id=flujo1.id, orden=3)

actividad4 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='AnalisisSistema', flujo_id=flujo1.id, orden=4)

#actividad5 = Actividad(id=5, owner=user1, nombre='DisenhoCasodeUso', flujo=flujo2, orden=1)
#actividad5.save()
#actividad6 = Actividad(id=6, owner=user1, nombre='DisenhoUML', flujo=flujo2, orden=2)
#actividad6.save()
#actividad7 = Actividad(id=7, owner=user1, nombre='DisenhoSistema', flujo=flujo2, orden=3)
#actividad7.save()
#actividad8 = Actividad(id=8, owner=user2, nombre='Programacion', flujo=flujo3, orden=1)
#actividad8.save()
#actividad9 = Actividad(id=9, owner=user2, nombre='Testing', flujo=flujo3, orden=2)
#actividad9.save()
#actividad10 = Actividad(id=10, owner=user2, nombre='Despliegue', flujo=flujo3, orden=3)
#actividad10.save()

us1 = UserStory.objects.crear_us(flujo_actual=flujo1.id, sprint_id=sprint1.id, actividad_actual=actividad1.id,
                owner_id=usuario1.id, prioridad=15, fecha_ini='2015-06-28 23:03:05',
                fecha_fin='2015-07-04 23:03:05', valorNegocio=800, valorTecnico=10)
us1.save()
#us2 = UserStory(id=2, flujo_actual=flujo3, sprint=sprint2, actividad_actual=actividad8, owner=user2, prioridad= 15, fecha_ini='2015-07-28 23:03:05.654997-04', tamanho=40, fecha_fin='2015-08-07 23:03:05.654997-04', valorNegocio=700, valorTecnico=15)
#us2.save()
#us3 = UserStory(id=3, flujo_actual=flujo3, sprint=sprint2, actividad_actual=actividad8, owner=user2, prioridad= 15, fecha_ini='2015-07-28 23:03:05.654997-04', tamanho=40, fecha_fin='2015-09-25 23:03:05.654997-04', valorNegocio=600, valorTecnico=15)
#us3.save()

