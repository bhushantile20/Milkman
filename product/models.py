from django.db import models
from category.models import Category

class Product(models.Model):
    PACKET_SIZES = [
        ('half_litre', 'Half Litre (0.5L)'),
        ('one_litre', '1 Litre (1L)'),
        ('two_litre', '2 Litre (2L)'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    packet_size = models.CharField(max_length=20, choices=PACKET_SIZES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_available = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['category', 'packet_size']  # One packet size per category
        verbose_name = "Milk Product"
        verbose_name_plural = "Milk Products"
        ordering = ['category', 'packet_size']

    def __str__(self):
        return f"{self.category.name} - {self.get_packet_size_display()} - ₹{self.price}"

