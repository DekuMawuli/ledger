from rest_framework import generics
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from api.authentications import TokenAuthentication

from users.models import CustomUser
from .serializers import CustomUserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def user_logout(request):
    logout(request)
    return Response(status=200)
