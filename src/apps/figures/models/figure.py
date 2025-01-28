from django.db import models
from common.models import (CreateTrackingModel, UpdateTrackingModel)

class Figure(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "иллюстрация"
        verbose_name_plural = "иллюстрации"

    title = models.CharField(
        "название",
        max_length=127,
        blank=False)
    detailed = models.TextField(
        "описание",
        blank=True)
    figures_album = models.ForeignKey(
        "FiguresAlbum",
        verbose_name="альбом",
        related_name="figures",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title