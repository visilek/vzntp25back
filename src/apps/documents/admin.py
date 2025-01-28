from django.contrib import admin
from .models import DocumentsAlbum, Document, DocumentRating


class DocumentsAlbumAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    list_display_links = [
        "title",
    ]
    list_filter = []
    inlines = []
    ordering = [
        "title",
    ]


admin.site.register(DocumentsAlbum, DocumentsAlbumAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        "documents_album",
        "title",
        "created_at",
    ]
    list_display_links = [
        "title",
    ]
    list_filter = [
        "documents_album",
    ]
    inlines = []
    ordering = [
        "title",
        "created_at",
        "documents_album",
    ]


admin.site.register(Document, DocumentAdmin)


class DocumentRatingAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "document",
        "created_by",
        "value",
    ]
    list_display_links = [
        "created_at",
    ]
    list_filter = [
        "value",
    ]
    ordering = [
        "created_at",
        "document",
    ]
    inlines = []


admin.site.register(DocumentRating, DocumentRatingAdmin)
