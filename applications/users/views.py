from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
@extend_schema(
    request=UserSerializer,
    responses={201: UserSerializer},
    description="Registro de un nuevo usuario"
)

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
