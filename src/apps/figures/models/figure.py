from django.db import models
from common.models import CreateTrackingModel, UpdateTrackingModel
from common.storage import (
    uploading_path_getter,
    get_on_post_delete_attachment_handler,
    get_on_pre_save_attachment_handler,
)


class Figure(CreateTrackingModel, UpdateTrackingModel):

    objects = models.Manager()

    class Meta:
        verbose_name = "иллюстрация"
        verbose_name_plural = "иллюстрации"

    title = models.CharField("название", max_length=127, blank=False)
    detailed = models.TextField("описание", blank=True)
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


on_post_delete_file_handler = get_on_post_delete_attachment_handler(
    attachment_fieldname="file"
)
models.signals.post_delete.connect(
    receiver=on_post_delete_file_handler,
    sender=Figure,
    dispatch_uid="figures__figure__post_delete__file_delete",
)

on_pre_save_file_handler = get_on_pre_save_attachment_handler(
    attachment_fieldname="file"
)
models.signals.pre_save.connect(
    receiver=on_pre_save_file_handler,
    sender=Figure,
    dispatch_uid="figures__figure__pre_save__file_update",
)
