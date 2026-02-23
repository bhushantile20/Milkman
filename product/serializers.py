from rest_framework import serializers
from .models import Product
from category.models import Category
from category.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_display = serializers.CharField(source='category.get_name_display', read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_category(self, value):
        """Ensure category exists and is active"""
        if not value.is_active:
            raise serializers.ValidationError("Category must be active.")
        return value
    
    def validate(self, data):
        """Ensure unique product per category+packet_size"""
        category = data.get('category')
        packet_size = data.get('packet_size')
        if Product.objects.filter(category=category, packet_size=packet_size).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("This packet size already exists for this category.")
        return data
