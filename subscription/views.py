from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from .models import SubscriptionType, Subscription
from .serializers import SubscriptionTypeSerializer, SubscriptionSerializer

class SubscriptionTypeViewSet(viewsets.ModelViewSet):
    """Subscription Types API (daily, monthly, etc.)"""
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer
    permission_classes = [IsAuthenticated]

class SubscriptionViewSet(viewsets.ModelViewSet):
    """Main Subscriptions API"""
    queryset = Subscription.objects.select_related('customer__user', 'product__category', 'sub_type').order_by('-created_at')
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get pending subscriptions (awaiting payment)"""
        subs = self.queryset.filter(status='pending')
        serializer = self.get_serializer(subs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get active subscriptions"""
        subs = self.queryset.filter(status='active')
        serializer = self.get_serializer(subs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def confirm_payment(self, request, pk=None):
        """Confirm payment - update transaction_number and status"""
        subscription = self.get_object()
        transaction_number = request.data.get('transaction_number')
        
        if subscription.status != 'pending':
            return Response({'error': 'Only pending subscriptions can be confirmed'}, status=400)
        
        subscription.status = 'active'
        subscription.transaction_number = transaction_number
        subscription.save()
        
        serializer = self.get_serializer(subscription)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Subscription statistics for milkman dashboard"""
        today = timezone.now().date()
        data = {
            'total_subscriptions': self.queryset.count(),
            'pending_count': self.queryset.filter(status='pending').count(),
            'active_count': self.queryset.filter(status='active').count(),
            'total_revenue': self.queryset.filter(status='paid').aggregate(Sum('total_amount'))['total_amount__sum'] or 0,
        }
        return Response(data)
