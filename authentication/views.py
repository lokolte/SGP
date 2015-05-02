from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers import UserSerializer

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