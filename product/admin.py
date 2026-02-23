from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'packet_size', 'price', 'stock_available', 'is_active']
    list_filter = ['category', 'packet_size', 'is_active', 'created_at']
    search_fields = ['name', 'category__name']
    list_editable = ['price', 'stock_available', 'is_active']
    
    fieldsets = (
        ('Product Info', {
            'fields': ('name', 'category', 'packet_size')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock_available'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_active',),
        }),
    )
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Product, ProductAdmin)
