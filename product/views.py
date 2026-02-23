from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    Products API - Half/1L/2L packets for each category
    GET /api/products/ - List all products
    POST /api/products/ - Create new product
    """
    queryset = Product.objects.filter(is_active=True).select_related('category').order_by('category', 'packet_size')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get products with stock > 0"""
        products = self.queryset.filter(stock_available__gt=0)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Filter products by category ID"""
        category_id = request.query_params.get('category_id')
        if category_id:
            products = self.queryset.filter(category_id=category_id)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response([])

    @action(detail=True, methods=['patch'])
    def restock(self, request, pk=None):
        """Update stock quantity"""
        product = self.get_object()
        quantity = request.data.get('quantity', 0)
        product.stock_available = quantity
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data)
