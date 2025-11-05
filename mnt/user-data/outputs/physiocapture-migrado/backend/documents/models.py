from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel

class Document(TimeStampedModel):
    class DocumentCategory(models.TextChoices):
        EXAME_IMAGEM = 'EXAME_IMAGEM', _('Exame de Imagem')
        EXAME_LABORATORIAL = 'EXAME_LABORATORIAL', _('Exame Laboratorial')
        RECEITA = 'RECEITA', _('Receita Médica')
        ATESTADO = 'ATESTADO', _('Atestado')
        CONSENTIMENTO = 'CONSENTIMENTO', _('Termo de Consentimento')
        ANAMNESE = 'ANAMNESE', _('Anamnese')
        RELATORIO_EVOLUCAO = 'RELATORIO_EVOLUCAO', _('Relatório de Evolução')
        OUTROS = 'OUTROS', _('Outros')
    
    file_name = models.CharField(_('nome do arquivo'), max_length=255)
    file_url = models.URLField(_('URL do arquivo'), max_length=500)
    file_size = models.IntegerField(_('tamanho do arquivo'))
    mime_type = models.CharField(_('tipo MIME'), max_length=100)
    category = models.CharField(_('categoria'), max_length=30, choices=DocumentCategory.choices)
    title = models.CharField(_('título'), max_length=255, blank=True, null=True)
    description = models.TextField(_('descrição'), blank=True, null=True)
    
    # Relacionamentos
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE, related_name='documents')
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='documents')
    uploader = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='documents_uploaded')
    
    class Meta:
        verbose_name = _('documento')
        verbose_name_plural = _('documentos')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['clinic', 'patient']),
            models.Index(fields=['category']),
        ]
    
    def __str__(self):
        return f'{self.title or self.file_name} - {self.patient.full_name}'
