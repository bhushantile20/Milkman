# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .models import MilkmanProfile
from .serializers import UserSerializer, MilkmanProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Milkman/Admin Users API - Full CRUD
    GET /api/users/ - List all users
    POST /api/users/ - Create new milkman
    """
    queryset = User.objects.filter(is_staff=True).select_related('milkman_profile')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class MilkmanProfileViewSet(viewsets.ModelViewSet):
    """
    Milkman Profiles API
    """
    queryset = MilkmanProfile.objects.select_related('user')
    serializer_class = MilkmanProfileSerializer
    permission_classes = [IsAdminUser]
