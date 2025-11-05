from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer, DocumentCreateSerializer
from users.permissions import CanManagePatients

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.select_related('patient', 'uploader', 'clinic').all()
    permission_classes = [IsAuthenticated, CanManagePatients]
    filterset_fields = ['patient', 'category', 'uploader']
    search_fields = ['file_name', 'title', 'description', 'patient__full_name']
    ordering_fields = ['created_at', 'file_name']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return DocumentCreateSerializer
        return DocumentSerializer
    
    def get_queryset(self):
        return self.queryset.filter(clinic=self.request.user.clinic)
    
    def perform_create(self, serializer):
        serializer.save(clinic=self.request.user.clinic, uploader=self.request.user)
