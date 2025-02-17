from django.db import models
from common.models import CreateTrackingModel, UpdateTrackingModel
from api.v1.blog.blogpost_tag.querysets import BlogpostTagApiQueryset


class BlogpostTag(CreateTrackingModel, UpdateTrackingModel):

    objects = models.Manager()
    api_v1 = BlogpostTagApiQueryset.as_manager()

    class Meta:
        verbose_name = "тэг блога"
        verbose_name_plural = "тэги блога"

    title = models.CharField("название", max_length=127, blank=False, unique=True)
    detailed = models.TextField("описание", blank=True)

    def __str__(self):
        return self.title
