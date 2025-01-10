from django.db import models
from common.models import (CreateTrackingModel, UpdateTrackingModel)

class Post(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"

    title = models.CharField(
        "заголовок",
        max_length=127,
        blank=False)
    subtitle = models.CharField(
        "подзаголовок",
        max_length=255,
        blank=True)
    detailed = models.TextField(
        "текст записи",
        blank=True)

    def __str__(self):
        return self.title
