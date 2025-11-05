"""
Models base para todos os apps
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class TimeStampedModel(models.Model):
    """
    Model abstrato que adiciona campos de data de criação e atualização
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('atualizado em'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class ActiveManager(models.Manager):
    """
    Manager que retorna apenas registros ativos
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class SoftDeleteModel(TimeStampedModel):
    """
    Model abstrato que implementa soft delete
    """
    is_active = models.BooleanField(_('ativo'), default=True)
    deleted_at = models.DateTimeField(_('deletado em'), null=True, blank=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, hard_delete=False):
        """
        Soft delete por padrão, hard delete se especificado
        """
        if hard_delete:
            super().delete(using=using, keep_parents=keep_parents)
        else:
            from django.utils import timezone
            self.is_active = False
            self.deleted_at = timezone.now()
            self.save()

    def restore(self):
        """
        Restaura um registro soft deleted
        """
        self.is_active = True
        self.deleted_at = None
        self.save()
