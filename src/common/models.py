from django.conf import settings
from django.db import models

user_model = settings.AUTH_USER_MODEL


class CreateTrackingModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        "когда создан",
        editable=False,
        auto_now_add=True
    )
    created_by = models.ForeignKey(
        user_model,
        verbose_name="кем создан",
        related_name="%(app_label)s_%(class)ss_created",
        blank=False,
        on_delete=models.CASCADE)
    

class UpdateTrackingModel(models.Model):

    class Meta:
        abstract = True

    updated_at = models.DateTimeField(
        "когда обновлен",
        editable=False,
        auto_now=True
    )
    updated_by = models.ForeignKey(
        user_model,
        verbose_name="кем обновлён",
        related_name="%(app_label)s_%(class)ss_updated",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)


class IsActiveSwitchableModel(models.Model):

    class Meta:
        abstract = True

    is_active = models.BooleanField(
        "активен",
        default=True
    )
