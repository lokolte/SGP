from rest_framework import serializers

from flujos.models import Actividad, Flujo
from authentication.serializers import UsuarioSerializer
from proyectos.serializers import ProyectoSerializer

class FlujoSerializer(serializers.ModelSerializer):
    owner = UsuarioSerializer(read_only=True, required=False)
    proyecto = ProyectoSerializer(read_only=True, required=False)

    class Meta:
        model = Flujo
        fields = ('id', 'proyecto', 'owner', 'nombre', 'estado', 'fecha_creacion',
                  'iniciado', 'observacion')

        read_only_fields = ('fecha_creacion', 'fecha_modificacion',)

        def create(self, validated_data):
            return Flujo.objects.crear_flujo(**validated_data)

        def update(self, instance, validated_data):
            instance.nombre = validated_data.get('nombre', instance.nombre)
            instance.observacion = validated_data.get('observacion', instance.observacion)
            instance.save()
            return instance

    def get_validation_exclusions(self, *args, **kwargs):

        exclusions = super(FlujoSerializer, self).get_validation_exclusions()

        return exclusions + ['owner', 'proyecto']


class ActividadSerializer(serializers.ModelSerializer):
    owner = UsuarioSerializer(read_only=True, required=False)
    flujo = FlujoSerializer(read_only=True, required=False)

    class Meta:
        model = Actividad
        fields = ('id', 'nombre', 'owner', 'estado', 'flujo', 'orden', 'cantidadUS',
                  'fecha_creacion')

        read_only_fields = ('fecha_creacion', 'fecha_modificacion',)

        def create(self, validated_data):
            return Actividad.objects.crear_actividad(**validated_data)

        def update(self, instance, validated_data):
            instance.cantidadUS = validated_data.get('cantidadUS', instance.cantidadUS)
            instance.save()
            return instance

    def get_validation_exclusions(self, *args, **kwargs):

        exclusions = super(ActividadSerializer, self).get_validation_exclusions()

        return exclusions + ['owner', 'flujo']