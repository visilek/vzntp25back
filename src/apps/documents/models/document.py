from django.db import models
from common.models import CreateTrackingModel, UpdateTrackingModel
from common.storage import (
    uploading_path_getter,
    post_delete_attachment_delete_handler,
    pre_save_attachment_update_handler,
)

from api.v1.documents.document.querysets import DocumentApiQueryset

class Document(CreateTrackingModel, UpdateTrackingModel):

    objects = models.Manager()
    api_v1 = DocumentApiQueryset.as_manager()

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "документы"

    title = models.CharField("название", max_length=127, blank=False)
    detailed = models.TextField("описание", blank=True)
    documents_album = models.ForeignKey(
        "DocumentsAlbum",
        verbose_name="альбом",
        related_name="documents",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    file = models.FileField(
        "файл",
        upload_to=uploading_path_getter,
    )

    def __str__(self):
        return self.title


models.signals.post_delete.connect(
    post_delete_attachment_delete_handler("file"),
    sender=Document,
    dispatch_uid="documents__document__post_delete__attachment_delete",
)

models.signals.pre_save.connect(
    pre_save_attachment_update_handler("file"),
    sender=Document,
    dispatch_uid="documents__document__pre_save__attachment_update",
)
