from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'created_at', 'user', 'is_done', 'is_canceled')
    list_filter = ('name', 'quantity', 'created_at', 'user', 'is_done', 'is_canceled')
    search_fields = ('name', 'quantity', 'created_at', 'user', 'is_done', 'is_canceled')
