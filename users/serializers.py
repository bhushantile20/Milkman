from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MilkmanProfile

class UserSerializer(serializers.ModelSerializer):
    milkman_profile = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'milkman_profile']
        read_only_fields = ['id', 'date_joined']

class MilkmanProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = MilkmanProfile
        fields = '__all__'
