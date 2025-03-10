from django.db import models
from common.models.base import CreateTrackingModel


class BlogpostLike(CreateTrackingModel):

    class Meta:
        verbose_name = "лайк к посту"
        verbose_name_plural = "лайки к посту"
        unique_together = [["blogpost", "created_by"]]

    blogpost = models.ForeignKey(
        "Blogpost",
        verbose_name="пост",
        related_name="blogpost_likes",
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.blogpost} - {self.created_by}"
