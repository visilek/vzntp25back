from django.db import models
from common.models.base import CreateTrackingModel, UpdateTrackingModel
from api.v1.blog.blogpost.querysets import BlogpostApiQueryset


class Blogpost(CreateTrackingModel, UpdateTrackingModel):

    objects = models.Manager()
    api_v1 = for_api = BlogpostApiQueryset.as_manager()

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"

    title = models.CharField("заголовок", max_length=127, blank=False)
    subtitle = models.CharField("подзаголовок", max_length=255, blank=True)
    detailed = models.TextField("текст записи", blank=True)
    blog_rubric = models.ForeignKey(
        "BlogRubric",
        verbose_name="рубрика",
        related_name="blogposts",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    blogpost_tags = models.ManyToManyField(
        "BlogpostTag",
        verbose_name="тэги",
        related_name="blogposts_tagged",
    )
    figures = models.ManyToManyField(
        "figures.Figure",
        verbose_name="иллюстрации",
        related_name="blogposts_referring",
    )

    documents = models.ManyToManyField(
        "documents.Document",
        verbose_name="документы",
        related_name="blogposts_referring",
    )

    def __str__(self):
        return self.title
