from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    uploader_name = serializers.CharField(source='uploader.name', read_only=True)
    
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['id', 'clinic', 'uploader', 'created_at', 'updated_at']

class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['file_name', 'file_url', 'file_size', 'mime_type', 'category', 
                  'title', 'description', 'patient', 'clinic', 'uploader']
