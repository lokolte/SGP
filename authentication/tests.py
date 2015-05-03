from django.test import TestCase
from authentication.models import Usuario
from django.contrib.auth.models import User
from authentication.serializers import UsuarioSerializer
from datetime import date

class UsuarioTests(TestCase):
    def setUp(self):
        user = User.objects.create_user('username')
        usuario = Usuario(id=1, user=user, nombre='Juan', apellido='Perez', correo='jperez@sgp.net', telefono='12345', direccion='Calle Falsa 123', fecha_creacion=date.today(), estado='A', tipo='E')
        usuario.save()

    def testGetUserFromDB(self):
        usuario = Usuario.objects.get(id=1)
        self.assertEqual(usuario.nombre, 'Juan')

    def testUsuarioSerializer(self):
        usuario = Usuario.objects.get(id=1)
        serializer = UsuarioSerializer(data=usuario)
        assert serializer.is_valid()

    def test_whatever(self):
        '''
        Prueba si los tests funcionan
        '''
        self.assertEqual(True, True)
        self.assertFalse(True == False)

