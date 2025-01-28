from django.db import models
from common.models import CreateTrackingModel, UpdateTrackingModel


class BlogpostTag(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "тэг блога"
        verbose_name_plural = "тэги блога"

    title = models.CharField("название", max_length=127, blank=False)
    detailed = models.TextField("описание", blank=True)

    def __str__(self):
        return self.title