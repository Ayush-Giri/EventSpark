from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from custom_user.serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class CreateUser(CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    
    
