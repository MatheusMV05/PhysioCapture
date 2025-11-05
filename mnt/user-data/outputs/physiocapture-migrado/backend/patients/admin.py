from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'cpf', 'age', 'phone', 'status', 'clinic', 'created_at']
    list_filter = ['status', 'clinic', 'assigned_therapist']
    search_fields = ['full_name', 'cpf', 'phone', 'email']
    ordering = ['-created_at']
    readonly_fields = ['age', 'created_at', 'updated_at', 'last_visit_date']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(clinic=request.user.clinic)
