# django and drf imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# own code imports
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'

    email = models.EmailField(
        verbose_name='email',
        unique=True
    )
    is_active = models.BooleanField(
        verbose_name='учетная запись активна',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='доступ в django-админку',
        default=False
    )
    date_joined = models.DateTimeField(
        verbose_name='дата регистрации',
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email