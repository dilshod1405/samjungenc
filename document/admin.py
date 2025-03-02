from django.contrib import admin
from .models import DocType, DocApp


@admin.register(DocType)
class DocTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(DocApp)
class DocAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    list_filter = ('name', 'user', 'created_at')
    list_display_links = ('name', 'user')
    list_per_page = 20
    search_fields = ('name', 'user', 'created_at')
