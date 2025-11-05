from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'type', 'date', 'performer', 'clinic']
    list_filter = ['type', 'clinic', 'date']
    search_fields = ['patient__full_name', 'notes']
    ordering = ['-date']
    readonly_fields = ['date', 'created_at', 'updated_at']
