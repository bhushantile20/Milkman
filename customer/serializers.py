from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def create(self, validated_data):
        # Create User first, then Customer
        user_data = {
            'username': validated_data.pop('user_username', f"cust_{validated_data['phone']}"),
            'email': validated_data.pop('user_email', ''),
            'first_name': validated_data.pop('first_name', ''),
        }
        user = User.objects.create_user(**user_data)
        validated_data['user'] = user
        return super().create(validated_data)
