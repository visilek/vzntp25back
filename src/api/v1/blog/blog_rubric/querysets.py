from django.db.models import QuerySet, Count
from common.api import querysets as commons


class BlogRubricApiQueryset(
    commons.FilterableByRequestMixin,
    commons.WithCreatedByBriefDataMixin,
    commons.WithUpdatedByBriefDataMixin,
    QuerySet,
):

    def as_base(self):
        return self.with_created_by_brief_data().with_cover_figure_brief_data()

    def as_list(self):
        return self.as_base().defer("detailed").with_blogposts_count()

    def as_retrieved(self):
        return self.as_base().with_updated_by_brief_data()

    def with_cover_figure_brief_data(self):
        return self.select_related("cover_figure").defer(
            "cover_figure__figures_album",
            "cover_figure__detailed",
        )

    def with_blogposts_count(self):
        return self.annotate(blogposts_count=Count("blogposts", distinct=True))
