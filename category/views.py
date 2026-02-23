from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Milk Categories API - cow_milk, buffalo_milk, ghee
    GET /api/categories/ - List all categories
    POST /api/categories/ - Create new category
    """
    queryset = Category.objects.filter(is_active=True).order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active categories"""
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def deactivate(self, request, pk=None):
        """Deactivate a category"""
        category = self.get_object()
        category.is_active = False
        category.save()
        serializer = self.get_serializer(category)
        return Response(serializer.data)
