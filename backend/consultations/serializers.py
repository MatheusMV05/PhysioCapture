from rest_framework import serializers
from .models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    performer_name = serializers.CharField(source='performer.name', read_only=True)
    
    class Meta:
        model = Consultation
        fields = '__all__'
        read_only_fields = ['id', 'date', 'clinic', 'created_at', 'updated_at']

class ConsultationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['type', 'subjective', 'objective', 'assessment', 'plan', 
                  'exercises', 'next_visit', 'notes', 'patient', 'clinic', 'performer']
