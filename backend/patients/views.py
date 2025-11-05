"""
Views do app patients
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import Patient
from .serializers import (
    PatientSerializer, PatientListSerializer, PatientCreateSerializer,
    PatientUpdateSerializer, PatientStatsSerializer
)
from users.permissions import CanManagePatients, IsSameClinic


class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar pacientes
    """
    queryset = Patient.objects.select_related('clinic', 'assigned_therapist').all()
    permission_classes = [IsAuthenticated, CanManagePatients]
    filterset_fields = ['status', 'assigned_therapist']
    search_fields = ['full_name', 'cpf', 'phone', 'email']
    ordering_fields = ['full_name', 'created_at', 'last_visit_date']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        elif self.action == 'create':
            return PatientCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return PatientUpdateSerializer
        return PatientSerializer
    
    def get_queryset(self):
        """Retorna apenas pacientes da clínica do usuário"""
        return self.queryset.filter(clinic=self.request.user.clinic)
    
    def perform_create(self, serializer):
        """Adiciona a clínica automaticamente ao criar paciente"""
        serializer.save(clinic=self.request.user.clinic)
    
    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        """Retorna estatísticas do paciente"""
        patient = self.get_object()
        now = timezone.now()
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        consultations = patient.consultations.all()
        consultations_by_type = consultations.values('type').annotate(count=Count('id'))
        
        stats = {
            'total_consultations': consultations.count(),
            'total_documents': patient.documents.count(),
            'last_consultation_date': consultations.first().date if consultations.exists() else None,
            'consultations_this_month': consultations.filter(date__gte=start_of_month).count(),
            'consultations_by_type': {item['type']: item['count'] for item in consultations_by_type}
        }
        
        serializer = PatientStatsSerializer(stats)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        """Alterna o status do paciente entre ACTIVE e INACTIVE"""
        patient = self.get_object()
        if patient.status == Patient.PatientStatus.ACTIVE:
            patient.status = Patient.PatientStatus.INACTIVE
        else:
            patient.status = Patient.PatientStatus.ACTIVE
        patient.save()
        return Response({
            'message': f'Paciente {patient.status.lower()}',
            'status': patient.status
        })
