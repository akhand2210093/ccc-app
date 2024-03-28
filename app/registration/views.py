from django.shortcuts import render

# registration/views.py
from rest_framework import generics
from .serializers import UserRegistrationSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
