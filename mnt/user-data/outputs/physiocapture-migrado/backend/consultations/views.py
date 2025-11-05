from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Consultation
from .serializers import ConsultationSerializer, ConsultationCreateSerializer
from users.permissions import CanPerformConsultations

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.select_related('patient', 'performer', 'clinic').all()
    permission_classes = [IsAuthenticated, CanPerformConsultations]
    filterset_fields = ['patient', 'type', 'performer']
    search_fields = ['patient__full_name', 'notes']
    ordering_fields = ['date', 'created_at']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ConsultationCreateSerializer
        return ConsultationSerializer
    
    def get_queryset(self):
        return self.queryset.filter(clinic=self.request.user.clinic)
    
    def perform_create(self, serializer):
        serializer.save(clinic=self.request.user.clinic, performer=self.request.user)
