from django.db import models
from common.models import CreateTrackingModel, UpdateTrackingModel


class DocumentRating(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "оценка документа"
        verbose_name_plural = "оценки документа"
        unique_together = [
            ["document", "created_by"],
        ]

    document = models.ForeignKey(
        "Document",
        verbose_name="документ",
        related_name="document_ratings",
        blank=False,
        on_delete=models.CASCADE,
    )
    value = models.PositiveSmallIntegerField("Балл")

    def __str__(self):
        return f"${self.document} - ${self.created_by}"
