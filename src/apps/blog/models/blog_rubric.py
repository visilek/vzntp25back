from django.db import models
from common.models import (CreateTrackingModel, UpdateTrackingModel)

class BlogRubric(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "рубрика блога"
        verbose_name_plural = "рубрики блога"

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
        related_name="blog_rubrics_covered",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title