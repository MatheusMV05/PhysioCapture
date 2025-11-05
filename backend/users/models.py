"""
Models do app users
"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import TimeStampedModel


class UserManager(BaseUserManager):
    """
    Manager customizado para o modelo User
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e salva um usuário com o email e senha fornecidos
        """
        if not email:
            raise ValueError(_('O email é obrigatório'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e salva um superusuário com o email e senha fornecidos
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'ADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser deve ter is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser deve ter is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    Modelo de usuário customizado que usa email ao invés de username
    """
    
    class UserRole(models.TextChoices):
        ADMIN = 'ADMIN', _('Administrador')
        MANAGER = 'MANAGER', _('Gestor')
        PHYSIOTHERAPIST = 'PHYSIOTHERAPIST', _('Fisioterapeuta')
        RECEPTIONIST = 'RECEPTIONIST', _('Recepcionista')
    
    # Campos de autenticação
    email = models.EmailField(_('email'), unique=True)
    password = models.CharField(_('senha'), max_length=128)
    
    # Dados pessoais
    name = models.CharField(_('nome completo'), max_length=255)
    cpf = models.CharField(_('CPF'), max_length=14, unique=True, null=True, blank=True)
    phone = models.CharField(_('telefone'), max_length=20, null=True, blank=True)
    
    # Dados profissionais
    crm = models.CharField(_('CRM/CREFITO'), max_length=20, null=True, blank=True, 
                           help_text=_('Registro no conselho profissional'))
    role = models.CharField(_('função'), max_length=20, choices=UserRole.choices, 
                           default=UserRole.PHYSIOTHERAPIST)
    
    # Vínculo com clínica
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE, 
                              related_name='users', verbose_name=_('clínica'))
    
    # Status
    is_active = models.BooleanField(_('ativo'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superusuário'), default=False)
    
    # Auditoria
    last_login_at = models.DateTimeField(_('último login'), null=True, blank=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['clinic', 'role']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f'{self.name} ({self.email})'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0] if self.name else self.email

    @property
    def is_admin(self):
        return self.role == self.UserRole.ADMIN or self.is_superuser

    @property
    def is_manager(self):
        return self.role == self.UserRole.MANAGER or self.is_admin

    @property
    def can_manage_patients(self):
        return self.role in [
            self.UserRole.ADMIN,
            self.UserRole.MANAGER,
            self.UserRole.PHYSIOTHERAPIST,
            self.UserRole.RECEPTIONIST
        ]

    @property
    def can_perform_consultations(self):
        return self.role in [
            self.UserRole.ADMIN,
            self.UserRole.MANAGER,
            self.UserRole.PHYSIOTHERAPIST
        ]
