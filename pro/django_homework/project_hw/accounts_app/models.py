from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.contenttypes.fields import GenericRelation

from django.db import models
from django.utils import timezone


class MembersUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        if not phone_number:
            raise ValueError('User must have a phone number')
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, phone_number, password, **extra_fields)


class MembersUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True, verbose_name='Електронна адреса', max_length=255)
    phone_number = models.CharField(max_length=20, unique=True, verbose_name='Номер телефону')
    first_name = models.CharField(max_length=30, blank=True, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="Прізвище")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата народження')
    profile_picture = models.ImageField(upload_to='profile_pict/', null=True, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_active = models.BooleanField(default=True, verbose_name='Активний')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата реєстрації')
    preffered_language = models.CharField(max_length=10, choices=[
        ('uk', 'Ukrainian'),
        ('en', 'English'),
    ], default='uk', verbose_name='Мова')
    logs = GenericRelation('action_logs_app.ActionLog', related_query_name='user_account')


    objects = MembersUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()
