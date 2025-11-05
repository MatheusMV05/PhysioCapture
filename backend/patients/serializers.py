"""
Serializers do app patients
"""
from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer completo para o modelo Patient
    """
    therapist_name = serializers.CharField(read_only=True)
    full_address = serializers.CharField(read_only=True)
    consultations_count = serializers.IntegerField(read_only=True)
    documents_count = serializers.IntegerField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'full_name', 'cpf', 'date_of_birth', 'age', 'phone',
            'phone_secondary', 'email', 'zip_code', 'street', 'number',
            'complement', 'neighborhood', 'city', 'state', 'full_address',
            'occupation', 'insurance', 'insurance_number', 'status',
            'general_notes', 'chief_complaint', 'current_illness',
            'medical_history', 'medications', 'allergies', 'lifestyle',
            'physical_assessment', 'clinic', 'assigned_therapist',
            'therapist_name', 'consultations_count', 'documents_count',
            'last_visit_date', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'age', 'created_at', 'updated_at', 'last_visit_date',
            'therapist_name', 'full_address', 'consultations_count', 'documents_count'
        ]


class PatientListSerializer(serializers.ModelSerializer):
    """
    Serializer simplificado para listagem de pacientes
    """
    therapist_name = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'id', 'full_name', 'cpf', 'age', 'phone', 'email',
            'status', 'assigned_therapist', 'therapist_name',
            'last_visit_date', 'created_at'
        ]


class PatientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criação de pacientes
    """
    class Meta:
        model = Patient
        fields = [
            'full_name', 'cpf', 'date_of_birth', 'phone', 'phone_secondary',
            'email', 'zip_code', 'street', 'number', 'complement',
            'neighborhood', 'city', 'state', 'occupation', 'insurance',
            'insurance_number', 'status', 'general_notes', 'chief_complaint',
            'current_illness', 'medical_history', 'medications', 'allergies',
            'lifestyle', 'physical_assessment', 'clinic', 'assigned_therapist'
        ]

    def validate_cpf(self, value):
        """Valida formato do CPF"""
        import re
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
            raise serializers.ValidationError('CPF deve estar no formato: 000.000.000-00')
        return value


class PatientUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização de pacientes
    """
    class Meta:
        model = Patient
        fields = [
            'full_name', 'phone', 'phone_secondary', 'email', 'zip_code',
            'street', 'number', 'complement', 'neighborhood', 'city', 'state',
            'occupation', 'insurance', 'insurance_number', 'status',
            'general_notes', 'chief_complaint', 'current_illness',
            'medical_history', 'medications', 'allergies', 'lifestyle',
            'physical_assessment', 'assigned_therapist'
        ]


class PatientStatsSerializer(serializers.Serializer):
    """
    Serializer para estatísticas do paciente
    """
    total_consultations = serializers.IntegerField()
    total_documents = serializers.IntegerField()
    last_consultation_date = serializers.DateTimeField(allow_null=True)
    consultations_this_month = serializers.IntegerField()
    consultations_by_type = serializers.DictField()
