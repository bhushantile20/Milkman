from rest_framework import serializers
from datetime import timedelta
from .models import SubscriptionType, Subscription
from product.models import Product
from customer.models import Customer

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.user.username', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    sub_type_name = serializers.CharField(source='sub_type.name', read_only=True)
    
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.filter(is_active=True))
    sub_type = serializers.PrimaryKeyRelatedField(queryset=SubscriptionType.objects.all())
    
    class Meta:
        model = Subscription
        fields = '__all__'
    
    def validate(self, data):
        """Calculate total_amount and validate dates"""
        product = data['product']
        sub_type = data['sub_type']
        quantity = data.get('quantity', 1.0)
        
        total_amount = product.price * quantity * sub_type.price_multiplier
        data['total_amount'] = total_amount
        
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
            
        return data
    
    def create(self, validated_data):
        validated_data['end_date'] = validated_data['start_date'] + timedelta(days=validated_data['sub_type'].duration_days)
        return super().create(validated_data)
