from django.contrib import admin
from .models import Chiller, ChillerImage

@admin.register(Chiller)
class ChillerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'charasteristic', 'created_at')
    list_filter = ('company_name', 'created_at')
    search_fields = ('company_name', 'created_at')
    list_per_page = 20

@admin.register(ChillerImage)
class ChillerImageAdmin(admin.ModelAdmin):
    list_display = ('chiller', 'image')
    list_filter = ('chiller',)
    search_fields = ('chiller',)
    list_per_page = 20
