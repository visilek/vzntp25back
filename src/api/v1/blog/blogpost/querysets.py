from django.db.models import QuerySet, Count
from common.api import querysets as commons


class BlogpostApiQueryset(
    commons.FilterableByRequestMixin,
    commons.WithCreatedByBriefDataMixin,
    commons.WithUpdatedByBriefDataMixin,
    QuerySet,
):

    def as_base(self):
        return (
            self.with_created_by_brief_data()
            .with_blog_rubric_brief_data()
            .with_blogpost_tags_prefetched()
            .with_blogpost_likes_count()
        )

    def as_list(self):
        return self.as_base().with_blogpost_comments_count().with_figures_count()

    def as_retrieved(self):
        return self.as_base().with_updated_by_brief_data()

    def with_blog_rubric_brief_data(self):
        return self.select_related("blog_rubric").defer(
            "blog_rubric__detailed", "blog_rubric__cover_figure"
        )

    def with_blogpost_tags_prefetched(self):
        return self.prefetch_related("blogpost_tags")

    def with_blogpost_likes_count(self):
        return self.annotate(
            blogpost_likes_count=Count("blogpost_likes", distinct=True)
        )

    def with_figures_count(self):
        return self.annotate(figures_count=Count("figures", distinct=True))

    def with_blogpost_comments_count(self):
        return self.annotate(
            blogpost_comments_count=Count("blogpost_comments", distinct=True)
        )

    def by_blogpost_tags(self, options_string):
        options = self.parse_multiple_options_string(options_string)
        return self.filter(blogpost_tags__in=options)

    def by_blog_rubric(self, options_string):
        options = self.parse_multiple_options_string(options_string)
        return self.filter(blog_rubric__in=options)
