from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    Customers API - End customers who buy milk
    GET /api/customers/ - List all customers
    POST /api/customers/ - Create new customer
    """
    queryset = Customer.objects.select_related('user').filter(is_active=True).order_by('user__username')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Customer statistics for milkman"""
        data = {
            'total_customers': self.queryset.count(),
            'customers_with_telegram': self.queryset.filter(telegram_id__isnull=False).count(),
            'active_customers_by_area': dict(
                self.queryset.values('location').annotate(count=Count('id')).order_by('-count')[:5]
            )
        }
        return Response(data)

    @action(detail=False, methods=['get'])
    def telegram_customers(self, request):
        """Customers with Telegram integration"""
        customers = self.queryset.filter(telegram_id__isnull=False)
        serializer = self.get_serializer(customers, many=True)
        return Response(serializer.data)
