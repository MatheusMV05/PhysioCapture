"""
Serializers do app users
"""
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer completo para o modelo User
    """
    clinic_name = serializers.CharField(source='clinic.name', read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'name', 'cpf', 'phone', 'crm', 'role',
            'clinic', 'clinic_name', 'is_active', 'last_login_at',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'last_login_at']


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criação de usuários
    """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'email', 'password', 'password_confirm', 'name', 'cpf', 
            'phone', 'crm', 'role', 'clinic'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                'password': 'As senhas não coincidem.'
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer para atualização de usuários
    """
    class Meta:
        model = User
        fields = ['name', 'cpf', 'phone', 'crm', 'role', 'is_active']


class PasswordChangeSerializer(serializers.Serializer):
    """
    Serializer para mudança de senha
    """
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    new_password_confirm = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({
                'new_password': 'As senhas não coincidem.'
            })
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Senha atual incorreta.')
        return value


class LoginSerializer(serializers.Serializer):
    """
    Serializer para login
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )

            if not user:
                raise serializers.ValidationError('Email ou senha inválidos.')
            
            if not user.is_active:
                raise serializers.ValidationError('Usuário inativo.')

        else:
            raise serializers.ValidationError('Email e senha são obrigatórios.')

        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer para o perfil do usuário logado
    """
    clinic_name = serializers.CharField(source='clinic.name', read_only=True)
    clinic_plan = serializers.CharField(source='clinic.plan', read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'name', 'cpf', 'phone', 'crm', 'role',
            'clinic', 'clinic_name', 'clinic_plan', 'is_active',
            'last_login_at', 'created_at'
        ]
        read_only_fields = ['id', 'email', 'clinic', 'role', 'created_at', 'last_login_at']
