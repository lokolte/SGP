from authentication.models import Usuario
from proyectos.models import Proyecto
from flujos.models import Flujo, Actividad
from userstories.models import UserStory
from sprints.models import Sprint

usuario1 = Usuario.objects.create_superuser(username='chuchosoft', password='chuchosoft',
                                            nombre='Junior', apellido='Aguilar',
                                            email='chuchosoft_239@hotmail.es', telefono='123',
                                            direccion='colo323')

usuario2 = Usuario.objects.crear_empleado(username='veronica', password='veronica',
                                            nombre='Veronica', apellido='Gayoso',
                                            email='vritogayoso@gmail.com', telefono='123',
                                            direccion='calle23')

usuario3 = Usuario.objects.crear_cliente(username='anastacia', password='anastacia',
                                            nombre='Anastacia', apellido='Bogado',
                                            email='anastacia@gmail.com', telefono='123',
                                            direccion='colo323')

proyecto1 = Proyecto.objects.crear_proyecto(nombre='Proyecto CNC', owner_id=usuario1.id,
                                            cliente_id=usuario3.id,
                                            fecha_ini='2015-06-28 23:03:05',
                                            fecha_fin= '2015-09-25 23:03:05',
                                            observacion='Proyecto EULA')

proyecto1.empleado.add(usuario2)

proyecto1.save()

proyecto2 = Proyecto.objects.crear_proyecto(nombre='Proyecto Cervepar', owner_id=usuario1.id, cliente_id=usuario3.id,
                     fecha_ini='2015-01-28 23:03:05',
                     fecha_fin= '2015-02-25 23:03:05', observacion='Proyecto de Contrataciones')

proyecto2.empleado.add(usuario2)

proyecto2.save()

sprint1 = Sprint.objects.crear_sprint(owner_id=usuario1.id, proyecto_id=proyecto1.id,
                                      fecha_ini='2015-06-28 23:03:05',
                                      duracionHoras=200.00)

sprint2 = Sprint.objects.crear_sprint(owner_id=usuario1.id, proyecto_id=proyecto2.id,
                                      fecha_ini='2015-06-28 23:03:05',
                                      duracionHoras=130.00)

flujo1 = Flujo.objects.crear_flujo(owner_id=usuario1.id, nombre='Desarrollo',
               proyecto_id=proyecto1.id, observacion='Flujo donde se tendra en cuenta el rendimiento individual')

flujo2 = Flujo.objects.crear_flujo(owner_id=usuario1.id, nombre='Analisis',
               proyecto_id=proyecto1.id, observacion='Atender bien a los clientes')

flujo3 = Flujo.objects.crear_flujo(owner_id=usuario1.id, nombre='Desarrollo',
               proyecto_id=proyecto2.id, observacion='Flujo donde se tendra en cuenta el rendimiento individual')

flujo4 = Flujo.objects.crear_flujo(owner_id=usuario1.id, nombre='Analisis',
               proyecto_id=proyecto2.id, observacion='Atender bien a los clientes')

flujo5 = Flujo.objects.crear_flujo(owner_id=usuario1.id, nombre='Implementacion',
               proyecto_id=proyecto2.id, observacion='Implementar el sistema con robustez')

#####  flujo1  ######
actividad1 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Desarrollo Frontend',
                                               flujo_id=flujo1.id, orden=1)

actividad2 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Desarrollo Backend',
                                               flujo_id=flujo1.id, orden=2)

actividad3 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Integracion Backend-Frontend',
                                               flujo_id=flujo1.id, orden=3)

actividad4 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Produccion',
                                               flujo_id=flujo1.id, orden=4)

#####  flujo2  ######
actividad5 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Analisis Caso',
                                               flujo_id=flujo2.id, orden=1)

actividad6 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Analisis Empresa',
                                               flujo_id=flujo2.id, orden=2)

actividad7 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Analisis Requerimientos',
                                               flujo_id=flujo2.id, orden=3)
#####  flujo3  ######
actividad8 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Desarrollo Backend',
                                               flujo_id=flujo3.id, orden=1)

actividad9 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Desarrollo Frontend',
                                               flujo_id=flujo3.id, orden=2)
#####  flujo4  ######
actividad10 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Analisis Empresa',
                                               flujo_id=flujo2.id, orden=3)

actividad11 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Analisis Requerimientos',
                                               flujo_id=flujo2.id, orden=4)

#####  flujo5  ######
actividad12 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Implementacion RRHH',
                                               flujo_id=flujo2.id, orden=3)

actividad13 = Actividad.objects.crear_actividad(owner_id=usuario1.id, nombre='Implementacion Secretaria',
                                               flujo_id=flujo2.id, orden=4)

###### US de flujo1 #############
us1 = UserStory.objects.crear_us(nombre='Login Frontend', flujo_id=flujo1.id, sprint_id=sprint1.id,
                                 actividad_actual=actividad1.id, owner_id=usuario1.id,
                                 prioridad=5, fecha_ini='2015-06-28 23:03:05', proyecto_id=proyecto1.id,
                                 fecha_fin='2015-07-04 23:03:05', valorNegocio=800, valorTecnico=10,
                                 descripcionC='Login consumidor del servicio REST')

us2 = UserStory.objects.crear_us(nombre='Login Backend', flujo_id=flujo1.id, sprint_id=sprint1.id,
                                 actividad_actual=actividad1.id, owner_id=usuario1.id,
                                 prioridad=6, fecha_ini='2015-06-28 23:03:05', proyecto_id=proyecto1.id,
                                 fecha_fin='2015-07-04 23:03:05', valorNegocio=800, valorTecnico=10,
                                 descripcionC='Login debidamente REST')

us3 = UserStory.objects.crear_us(nombre='Administracion Proyectos', flujo_id=flujo1.id, sprint_id=sprint1.id,
                                 actividad_actual=actividad1.id, owner_id=usuario1.id,
                                 prioridad=8, fecha_ini='2015-06-28 08:03:05', proyecto_id=proyecto1.id,
                                 fecha_fin='2015-07-06 11:03:05', valorNegocio=800, valorTecnico=10,
                                 descripcionC='Se debe tener en cuenta los Roles')