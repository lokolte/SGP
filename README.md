# Proyecto IS2 Sistema de Gestion de Proyectos Agiles
#
##########################################################
#Metodos (describe el efecto del metodo sobre el/los objeto(s))
    En caso de que los metodos se hayan ejecutado y sus ejecuciones sean:

Redundantes (Sin efectos):
    - Rta: 'SIN_EFECTOS'

Exito (Efecto esperado):
    - Rta: el/los Objetos (Instancia)

Error:
    - Rta: 'ERROR'

No permitido:
    - Rta: 'NO_PERMITIDO'

No encontrado:
    - Rta: 'NO_ENCONTRADO'

Nota: los efectos esperados son los que retornan el/los mismo(s) objeto(s).

#########################################################
#Formatos para los Views
    Para los metodos que retornan:

Sin efectos:
    - {
       'status': '',
       'message': 'Sin efectos'
       }

El/los mismo(s) objeto(s) con exito:
    - {'atributos': 'datos'} (Objeto/s)
    - [{objeto1},{objeto2}]

Con error:
    -{
       'status': 'Internal Error',
       'message': 'Ocurrio un error en el servidor al ejecutarse su peticion.'
     }

Para peticiones con formato inadecuado:
    - {
       'status': 'Bad request',
       'message': 'Peticion Invalida'
      }

############################################################
#Observaciones
    - Los estados utilizados en backend son las abreviaturas, tener cuidado con el uso de estos en el frontend

    - Para las fechas se utilizara el formato de YYYY-MM-DD HH:MM:SS sin excepciones

###########################################################

