from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'file_name', 'category', 'patient', 'uploader', 'created_at']
    list_filter = ['category', 'clinic', 'created_at']
    search_fields = ['file_name', 'title', 'patient__full_name']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
