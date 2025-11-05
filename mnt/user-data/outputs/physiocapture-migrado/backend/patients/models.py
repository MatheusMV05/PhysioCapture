"""
Models do app patients
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from datetime import date
from core.models import TimeStampedModel


class Patient(TimeStampedModel):
    """
    Modelo para Paciente
    """
    
    class PatientStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Ativo')
        INACTIVE = 'INACTIVE', _('Inativo')
        EVALUATION = 'EVALUATION', _('Em Avaliação')
        DISCHARGED = 'DISCHARGED', _('Alta')
    
    # Dados pessoais
    full_name = models.CharField(_('nome completo'), max_length=255)
    cpf_validator = RegexValidator(
        regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        message='CPF deve estar no formato: 000.000.000-00'
    )
    cpf = models.CharField(_('CPF'), max_length=14, unique=True, validators=[cpf_validator])
    date_of_birth = models.DateField(_('data de nascimento'))
    age = models.IntegerField(_('idade'), editable=False)
    phone = models.CharField(_('telefone'), max_length=20)
    phone_secondary = models.CharField(_('telefone secundário'), max_length=20, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    
    # Endereço
    zip_code = models.CharField(_('CEP'), max_length=9, blank=True, null=True)
    street = models.CharField(_('rua'), max_length=255, blank=True, null=True)
    number = models.CharField(_('número'), max_length=20, blank=True, null=True)
    complement = models.CharField(_('complemento'), max_length=255, blank=True, null=True)
    neighborhood = models.CharField(_('bairro'), max_length=100, blank=True, null=True)
    city = models.CharField(_('cidade'), max_length=100, blank=True, null=True)
    state = models.CharField(_('estado'), max_length=2, blank=True, null=True)
    
    # Profissional/Convênio
    occupation = models.CharField(_('profissão'), max_length=100, blank=True, null=True)
    insurance = models.CharField(_('convênio'), max_length=100, blank=True, null=True)
    insurance_number = models.CharField(_('número do convênio'), max_length=50, blank=True, null=True)
    
    # Status
    status = models.CharField(_('status'), max_length=20, choices=PatientStatus.choices,
                             default=PatientStatus.ACTIVE)
    
    # Observações gerais
    general_notes = models.TextField(_('observações gerais'), blank=True, null=True)
    
    # Anamnese
    chief_complaint = models.TextField(_('queixa principal'), blank=True, null=True)
    current_illness = models.TextField(_('história da doença atual'), blank=True, null=True)
    medical_history = models.TextField(_('histórico médico'), blank=True, null=True)
    medications = models.TextField(_('medicamentos em uso'), blank=True, null=True)
    allergies = models.TextField(_('alergias'), blank=True, null=True)
    lifestyle = models.TextField(_('estilo de vida'), blank=True, null=True)
    physical_assessment = models.TextField(_('avaliação física'), blank=True, null=True)
    
    # Relacionamentos
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE,
                              related_name='patients', verbose_name=_('clínica'))
    assigned_therapist = models.ForeignKey('users.User', on_delete=models.SET_NULL,
                                          related_name='assigned_patients', null=True, blank=True,
                                          verbose_name=_('fisioterapeuta responsável'))
    
    # Auditoria
    last_visit_date = models.DateTimeField(_('data da última visita'), null=True, blank=True)
    
    class Meta:
        verbose_name = _('paciente')
        verbose_name_plural = _('pacientes')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['clinic', 'status']),
            models.Index(fields=['cpf']),
            models.Index(fields=['full_name']),
            models.Index(fields=['assigned_therapist']),
        ]

    def __str__(self):
        return f'{self.full_name} - {self.cpf}'

    def save(self, *args, **kwargs):
        """Calcula a idade automaticamente antes de salvar"""
        if self.date_of_birth:
            today = date.today()
            self.age = today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        super().save(*args, **kwargs)

    @property
    def full_address(self):
        """Retorna o endereço completo"""
        if not self.street:
            return ''
        parts = [
            f"{self.street}, {self.number}" if self.number else self.street,
            self.complement,
            self.neighborhood,
            f"{self.city} - {self.state}" if self.city and self.state else None,
            self.zip_code
        ]
        return ' - '.join(filter(None, parts))

    @property
    def consultations_count(self):
        """Retorna o número total de consultas"""
        return self.consultations.count()

    @property
    def documents_count(self):
        """Retorna o número total de documentos"""
        return self.documents.count()

    @property
    def therapist_name(self):
        """Retorna o nome do fisioterapeuta responsável"""
        return self.assigned_therapist.name if self.assigned_therapist else None
