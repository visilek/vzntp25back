from django.db import models
from common.models import (CreateTrackingModel, UpdateTrackingModel)
from common.storage import (
    uploading_path_getter,
    post_delete_attachment_delete_handler,
    pre_save_attachment_update_handler,
)

class Figure(CreateTrackingModel, UpdateTrackingModel):

    class Meta:
        verbose_name = "иллюстрация"
        verbose_name_plural = "иллюстрации"

    attachment_field_name = "file"

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
    file = models.ImageField(
        "файл",
        upload_to=uploading_path_getter,
    )

    def __str__(self):
        return self.title


models.signals.post_delete.connect(
    post_delete_attachment_delete_handler,
    sender=Figure,
    dispatch_uid="figures__figure__post_delete__attachment_delete",
)

models.signals.pre_save.connect(
    pre_save_attachment_update_handler,
    sender=Figure,
    dispatch_uid="figures__figure__pre_save__attachment_update",
)