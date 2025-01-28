from django.contrib import admin
from .models import FiguresAlbum, Figure, FigureRating


class FiguresAlbumAdmin(admin.ModelAdmin):
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


admin.site.register(FiguresAlbum, FiguresAlbumAdmin)


class FigureAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "figures_album",
        "created_at",
    ]
    list_display_links = [
        "title",
    ]
    list_filter = [
        "figures_album",
    ]
    inlines = []
    ordering = [
        "title",
        "created_at",
        "figures_album",
    ]


admin.site.register(Figure, FigureAdmin)


class FigureRatingAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "figure",
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
        "figure",
    ]
    inlines = []


admin.site.register(FigureRating, FigureRatingAdmin)
