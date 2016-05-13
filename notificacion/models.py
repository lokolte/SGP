from django.core.mail import send_mail

# Create your models here.

class Notificaciones:
    def notificar(usuarios,subj,mensaje):

        try:
            for u in usuarios:
                mail= u.email
                send_mail(subj, mensaje, 'sgp2015r13@gmail.com',[mail], fail_silently=False)
        except:
            try:
                mail= usuarios.email
                send_mail(subj, mensaje, 'sgp2015r13@gmail.com',[mail], fail_silently=False)
            except:
                mail=usuarios
                send_mail(subj, mensaje, 'sgp2015r13@gmail.com',[mail], fail_silently=False)

    def notificar_creacion_usuario(usuarios):
        #Usuario= models.ForeignKey()
        mensaje = u'Hola %s. Se ha creado su usuario exitosamente.Su username es %s '%(usuarios.first_name,usuarios.username)
        subj = u'Creacion de cuenta sgpa2015'
        Notificaciones.notificar(usuarios,subj,mensaje)


    def notificar_mod_usuario(usuario):

        mensaje = u'Se han modificado uno o mas campos de su cuenta. Por favor consulte la proxima vez que inicie sesion'
        subj = u'Modificacon de cuenta sgpa2015'
        Notificaciones.notificar(usuario,subj,mensaje)


    def notificar_elim_usuario(usuario):

        mensaje = u'Se ha eliminado su cuenta. Consulte con el administrador'
        subj = u'Eliminacion de cuenta sgpa2015'
        Notificaciones.notificar(usuario,subj,mensaje)

    def notificar_asignacion_proyecto(usuarios,proyecto):

        mensaje = u'Se le ha agregado al equipo del sgte Proyecto %s.' %(proyecto)
        subj = u'Asignacion Proyecto SGPA2015'
        Notificaciones.notificar(usuarios,subj,mensaje)

    def notificar_mod_proyecto(usuarios,proyecto):

        mensaje = u'Se han realizado cambios en los campos del sgte Proyecto %s que tiene asignado.' %(proyecto)
        subj = u'Modificacion Proyecto SGPA2015'
        Notificaciones.notificar(usuarios,subj,mensaje)

    def notificar_creacion_proyecto(usuarios,proyecto):

        mensaje = u'Se ha creado satisfactoriamente el proyecto %s.' %(proyecto)
        subj = u'Creacion Proyecto en SGPA2015'
        Notificaciones.notificar(usuarios,subj,mensaje)

    def notificar_asignacion_us(usuarios,proyecto):

        mensaje = u'Se le ha asignado satisfactoriamente un us en el proyecto %s.' %(proyecto)
        subj = u'Asignacion de us en SGPA2015'
        Notificaciones.notificar(usuarios,subj,mensaje)

    def notificar_creacion_us(usuarios,proyecto):

        mensaje = u'Se ha creado satisfactoriamente un us en el proyecto %s. donde usted es lider' %(proyecto)
        subj = u'Creacion de us en SGPA2015'
        Notificaciones.notificar(usuarios,subj,mensaje)

    def notificar_mod_us(usuarios,proyecto):
        mensaje = u'Se ha modificado satisfactoriamente un us en el proyecto %s. donde usted es lider' %(proyecto)
        subj = u'Modificacion de us en SGPA2015'
        Notificaciones.notificar(usuarios,subj,mensaje)

    def notificar_generico(usuarios,proyecto,mensaje,subj):

        Notificaciones.notificar(usuarios,subj,mensaje)