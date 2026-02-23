from django.db import models

class Category(models.Model):
    MILK_CATEGORIES = [
        ('cow_milk', 'Cow Milk'),
        ('buffalo_milk', 'Buffalo Milk'),
        ('ghee', 'Ghee'),
    ]
    
    name = models.CharField(max_length=50, choices=MILK_CATEGORIES, unique=True)
    description = models.TextField(blank=True, help_text="Description of milk type")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Milk Category"
        verbose_name_plural = "Milk Categories"
        ordering = ['name']

    def __str__(self):
        return self.get_name_display()
