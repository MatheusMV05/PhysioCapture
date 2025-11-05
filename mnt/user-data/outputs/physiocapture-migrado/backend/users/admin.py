"""
Admin do app users
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Admin customizado para o modelo User
    """
    list_display = ['email', 'name', 'role', 'clinic', 'is_active', 'created_at']
    list_filter = ['role', 'is_active', 'is_staff', 'clinic']
    search_fields = ['email', 'name', 'cpf', 'phone']
    ordering = ['-created_at']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Informações Pessoais'), {'fields': ('name', 'cpf', 'phone')}),
        (_('Informações Profissionais'), {'fields': ('crm', 'role', 'clinic')}),
        (_('Permissões'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Datas Importantes'), {'fields': ('last_login_at', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'clinic', 'role'),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'last_login_at']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(clinic=request.user.clinic)
