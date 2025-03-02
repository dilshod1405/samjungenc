from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'role', 'id')
    list_filter = ('role',)
    list_editable = ('full_name', 'role')
    search_fields = ('username', 'full_name')
    ordering = ('role',)
