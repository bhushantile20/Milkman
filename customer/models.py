from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=15)
    address = models.TextField()
    location = models.CharField(max_length=100, blank=True, help_text="Area/Landmark")
    telegram_id = models.CharField(max_length=50, blank=True, help_text="Telegram user ID for notifications")
    is_active = models.BooleanField(default=True)
    delivery_instructions = models.TextField(blank=True, help_text="Gate passcode, etc.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['user__username']
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.user.username} - {self.phone}"

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    """Auto-create customer profile for regular users"""
    if created and not instance.is_staff:
        Customer.objects.get_or_create(
            user=instance,
            defaults={
                'phone': '',
                'address': '',
                'location': ''
            }
        )
