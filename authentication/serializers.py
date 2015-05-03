from django.contrib.auth.models import User

from rest_framework import serializers

from authentication.models import Usuario, Proyecto, Sprint, Flujo, UserStory, Actividad

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellido', 'correo', 'telefono', 'direccion',
                  'fecha_creacion', 'estado', 'tipo')

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id', 'nombre', 'owner', 'cliente', 'fecha_creacion', 'estado', 'fecha_ini',
                  'fecha_fin', 'observaciones')

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ('id', 'owner', 'proyecto', 'fecha_creacion', 'fecha_ini',
                  'duracionHoras', 'estado')

class FlujoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flujo
        fields = ('id', 'owner', 'nombre', 'fecha_creacion', 'estado', 'proyecto',
                  'observaciones')

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'owner', 'nombre', 'fecha_creacion', 'estado', 'flujo', 'orden')

class UserStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStory
        fields = ('id', 'flujo_actual', 'sprint', 'actividad_actual', 'owner', 'descripcionC',
                  'descripcionL', 'fecha_creacion', 'prioridad', 'tamanho', 'estado', 'fecha_ini', 'fecha_fin')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        user = super(UserSerializer, self).restore_object(attrs, instance)
        password = attrs.get('password', None)

        if password:
            user.set_password(password)

        return user
