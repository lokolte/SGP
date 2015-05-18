from rest_framework import serializers

from proyectos.models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = ('id', 'nombre', 'owner', 'cliente', 'fecha_creacion', 'estado', 'fecha_ini',
                  'fecha_fin', 'observacion')
        read_only_fields = ('fecha_creacion', 'fecha_modificacion',)

        def create(self, validated_data):
            return Proyecto.objects.crear_proyecto(**validated_data)

        def update(self, instance, validated_data):
            instance.nombre = validated_data.get('nombre', instance.nombre)
            instance.observacion = validated_data.get('observacion', instance.observacion)
            return instance

