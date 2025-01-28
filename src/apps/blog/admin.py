from django.contrib import admin
from .models import BlogRubric, Blogpost, BlogpostComment, BlogpostLike, BlogpostTag

# class ContentElementInline(admin.TabularInline):
#     model = ContentElement
#     fields = (
#         'content_element_kind',
#         'full_title',
#         'brief_title',
#     )


class BlogpostCommentInline(admin.TabularInline):
    model = BlogpostComment
    fields = (
        "detailed",
        "created_by",
    )


class BlogRubricAdmin(admin.ModelAdmin):
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


admin.site.register(BlogRubric, BlogRubricAdmin)


class BlogpostAdmin(admin.ModelAdmin):
    list_display = [
        "blog_rubric",
        "title",
        "subtitle",
        "created_at",
    ]
    list_display_links = [
        "title",
    ]
    list_filter = [
        "blog_rubric",
    ]
    inlines = [
        BlogpostCommentInline,
    ]
    ordering = [
        "blog_rubric",
        "created_at",
    ]


admin.site.register(Blogpost, BlogpostAdmin)


class BlogpostCommentAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "blogpost",
        "created_by",
    ]
    list_display_links = [
        "created_at",
    ]
    list_filter = [
        "blogpost",
    ]
    ordering = [
        "created_at",
    ]
    inlines = []


admin.site.register(BlogpostComment, BlogpostCommentAdmin)


class BlogpostLikeAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "blogpost",
        "created_by",
    ]
    list_display_links = [
        "created_at",
    ]
    list_filter = [
        "blogpost",
    ]
    ordering = [
        "created_at",
    ]
    inlines = []


admin.site.register(BlogpostLike, BlogpostLikeAdmin)


class BlogpostTagAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "created_by",
    ]
    list_display_links = [
        "title",
    ]
    list_filter = []
    ordering = ["title", "created_at"]
    inlines = []


admin.site.register(BlogpostTag, BlogpostTagAdmin)
