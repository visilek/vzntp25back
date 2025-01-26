# django and drf imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# own code imports
from .CustomUserManagers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    objects = CustomUserManager()

    class Meta:
        verbose_name = "аккаунт"
        verbose_name_plural = "аккаунты"

    email = models.EmailField(
        "email",
        unique=True,
    )
    is_active = models.BooleanField(
        "учетная запись активна",
        default=True,
    )
    is_staff = models.BooleanField(
        "доступ в django-админку",
        default=False,
    )
    date_joined = models.DateTimeField(
        "дата регистрации",
        auto_now_add=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
