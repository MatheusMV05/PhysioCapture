from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel

class Consultation(TimeStampedModel):
    class ConsultationType(models.TextChoices):
        INITIAL_EVALUATION = 'INITIAL_EVALUATION', _('Avaliação Inicial')
        REASSESSMENT = 'REASSESSMENT', _('Reavaliação')
        TREATMENT_SESSION = 'TREATMENT_SESSION', _('Sessão de Tratamento')
        DISCHARGE = 'DISCHARGE', _('Alta')
        RETURN = 'RETURN', _('Retorno')
    
    date = models.DateTimeField(_('data'), auto_now_add=True)
    type = models.CharField(_('tipo'), max_length=30, choices=ConsultationType.choices)
    
    # SOAP
    subjective = models.TextField(_('subjetivo'), blank=True, null=True)
    objective = models.TextField(_('objetivo'), blank=True, null=True)
    assessment = models.TextField(_('avaliação'), blank=True, null=True)
    plan = models.TextField(_('plano'), blank=True, null=True)
    
    exercises = models.TextField(_('exercícios prescritos'), blank=True, null=True)
    next_visit = models.DateTimeField(_('próxima visita'), blank=True, null=True)
    notes = models.TextField(_('observações'), blank=True, null=True)
    
    # Relacionamentos
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE, related_name='consultations')
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='consultations')
    performer = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='consultations')
    
    can_edit = models.BooleanField(_('pode editar'), default=True)
    
    class Meta:
        verbose_name = _('consulta')
        verbose_name_plural = _('consultas')
        ordering = ['-date']
        indexes = [
            models.Index(fields=['clinic', 'patient']),
            models.Index(fields=['date']),
        ]
    
    def __str__(self):
        return f'{self.patient.full_name} - {self.date.strftime("%d/%m/%Y")}'
