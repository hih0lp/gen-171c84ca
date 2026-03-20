from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Order

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone', 'status', 'desired_datetime', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'phone', 'address')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Клиент', {'fields': ('customer_name', 'phone', 'address')}),
        ('Заказ', {'fields': ('order_details', 'desired_datetime', 'status')}),
        ('Системные', {'fields': ('created_at',)}),
    )