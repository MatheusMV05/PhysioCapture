"""
Views do app core
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import connection
from django.conf import settings


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Endpoint de health check para verificar se a API está funcionando
    """
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        db_status = 'healthy'
    except Exception as e:
        db_status = f'unhealthy: {str(e)}'
    
    return Response({
        'status': 'ok' if db_status == 'healthy' else 'error',
        'message': 'PhysioCapture API is running',
        'database': db_status,
        'debug_mode': settings.DEBUG,
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    """
    Informações sobre a API
    """
    return Response({
        'name': 'PhysioCapture API',
        'version': '1.0.0',
        'description': 'Sistema de Gestão para Clínicas de Fisioterapia',
        'endpoints': {
            'health': '/api/health/',
            'auth': '/api/auth/',
            'clinics': '/api/clinics/',
            'patients': '/api/patients/',
            'consultations': '/api/consultations/',
            'documents': '/api/documents/',
        }
    })
