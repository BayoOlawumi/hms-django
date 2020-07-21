from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserProfileSerializer
from .models import UserProfile

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()