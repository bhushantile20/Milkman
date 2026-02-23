from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from customer.models import Customer  # Will be created later

class SubscriptionType(models.Model):
    TYPE_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ]
    
    name = models.CharField(max_length=20, choices=TYPE_CHOICES, unique=True)
    duration_days = models.PositiveIntegerField(help_text="Duration in days")
    price_multiplier = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)
    
    class Meta:
        verbose_name = "Subscription Type"
        verbose_name_plural = "Subscription Types"

    def __str__(self):
        return self.get_name_display()

class Subscription(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, related_name='subscriptions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subscriptions')
    sub_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_number = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    telegram_notified = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer.user.username} - {self.product} - {self.sub_type} (₹{self.total_amount})"

    def save(self, *args, **kwargs):
        # Auto-calculate end_date based on subscription type
        if self.start_date and self.sub_type:
            self.end_date = self.start_date + timedelta(days=self.sub_type.duration_days)
        super().save(*args, **kwargs)
