from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class MilkmanProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Milkman Admin'),
        ('manager', 'Delivery Manager'),
        ('staff', 'Staff'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='milkman_profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    phone = models.CharField(max_length=15, blank=True)
    telegram_id = models.CharField(max_length=50, blank=True)
    is_active_milkman = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_milkman_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        MilkmanProfile.objects.create(user=instance)
