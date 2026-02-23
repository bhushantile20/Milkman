from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import MilkmanProfile

class MilkmanProfileInline(admin.StackedInline):
    model = MilkmanProfile
    can_delete = False

class MilkmanUserAdmin(UserAdmin):
    inlines = (MilkmanProfileInline,)

# Re-register UserAdmin for milkman users
admin.site.unregister(User)
admin.site.register(User, MilkmanUserAdmin)
admin.site.register(MilkmanProfile)
