from django.db import models
from common.models import CreateTrackingModel, UpdateTrackingModel


class FigureRating(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "оценка иллюстрации"
        verbose_name_plural = "оценки иллюстрации"
        unique_together = [
            ["figure", "created_by"],
        ]

    figure = models.ForeignKey(
        "Figure",
        verbose_name="иллюстрация",
        related_name="figure_ratings",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    value = models.PositiveSmallIntegerField("Балл")

    def __str__(self):
        return f"${self.figure} - ${self.created_by}"
