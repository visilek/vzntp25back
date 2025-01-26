from django.db import models
from common.models import CreateTrackingModel, UpdateTrackingModel


class BlogpostComment(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "коммент к посту"
        verbose_name_plural = "комменты к посту"

    blogpost = models.ForeignKey(
        "Blogpost",
        verbose_name="пост",
        related_name="blogpost_comments",
        blank=False,
        on_delete=models.CASCADE,
    )
    detailed = models.TextField(
        "описание",
        blank=True,
    )

    def __str__(self):
        return f"${self.blogpost} / ${self.created_by}"
