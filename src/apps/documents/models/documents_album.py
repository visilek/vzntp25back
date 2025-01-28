from django.db import models
from common.models import (CreateTrackingModel, UpdateTrackingModel)

class DocumentsAlbum(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "альбом документов"
        verbose_name_plural = "альбомы документов"

    title = models.CharField(
        "название",
        max_length=127,
        blank=False)
    detailed = models.TextField(
        "описание",
        blank=True)
    cover_figure = models.ForeignKey(
        "figures.Figure",
        verbose_name="обложка",
        related_name="documents_albums_covered",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title