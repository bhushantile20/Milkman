from django.contrib import admin
from .models import SubscriptionType, Subscription

@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_days', 'price_multiplier']
    list_editable = ['duration_days', 'price_multiplier']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'sub_type', 'status', 'total_amount', 'start_date']
    list_filter = ['status', 'sub_type', 'start_date', 'created_at']
    search_fields = ['customer__user__username', 'transaction_number']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Customer & Product', {
            'fields': ('customer', 'product', 'sub_type', 'quantity')
        }),
        ('Dates & Status', {
            'fields': ('start_date', 'end_date', 'status', 'transaction_number')
        }),
        ('Payment', {
            'fields': ('total_amount',),
            'classes': ('collapse',)
        }),
    )
