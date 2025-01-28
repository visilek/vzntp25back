from django.db import models
from common.models import (CreateTrackingModel, UpdateTrackingModel)

class Document(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "документы"

    title = models.CharField(
        "название",
        max_length=127,
        blank=False)
    detailed = models.TextField(
        "описание",
        blank=True)
    documents_album = models.ForeignKey(
        "DocumentsAlbum",
        verbose_name="альбом",
        related_name="documents",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title