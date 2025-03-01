from django.db import models
from common.models.base import CreateTrackingModel, UpdateTrackingModel
from common.storage import uploading_path, attachment_handlers

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
        upload_to=uploading_path.get_path,
    )

    def __str__(self):
        return self.title


on_post_delete_file_handler = attachment_handlers.get_on_post_delete_attachment_handler(
    attachment_fieldname="file"
)
models.signals.post_delete.connect(
    receiver=on_post_delete_file_handler,
    sender=Document,
    dispatch_uid="documents__document__post_delete__file_delete",
)

on_pre_save_file_handler = attachment_handlers.get_on_pre_save_attachment_handler(
    attachment_fieldname="file"
)
models.signals.pre_save.connect(
    receiver=on_pre_save_file_handler,
    sender=Document,
    dispatch_uid="documents__document__pre_save__file_update",
)
