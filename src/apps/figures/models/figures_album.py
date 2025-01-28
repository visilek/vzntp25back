from django.db import models
from common.models import (CreateTrackingModel, UpdateTrackingModel)

class FiguresAlbum(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "альбом иллюстраций"
        verbose_name_plural = "альбомы иллюстраций"

    title = models.CharField(
        "название",
        max_length=127,
        blank=False)
    detailed = models.TextField(
        "описание",
        blank=True)
    cover_figure = models.ForeignKey(
        "Figure",
        verbose_name="обложка",
        related_name="figures_albums_covered",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title