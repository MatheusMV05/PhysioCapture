"""
URLs principais do projeto PhysioCapture
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Authentication
    path('api/auth/', include('users.urls')),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API endpoints
    path('api/clinics/', include('clinics.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/consultations/', include('consultations.urls')),
    path('api/documents/', include('documents.urls')),
    
    # Health check
    path('api/health/', include('core.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin customization
admin.site.site_header = 'PhysioCapture Admin'
admin.site.site_title = 'PhysioCapture'
admin.site.index_title = 'Painel Administrativo'
