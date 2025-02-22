from django.db.models import QuerySet, Count
from common.api import querysets as commons


class BlogpostTagApiQueryset(
    commons.FilterableByRequestMixin,
    commons.WithCreatedByBriefDataMixin,
    commons.WithUpdatedByBriefDataMixin,
    QuerySet,
):

    def as_base(self):
        return self.with_created_by_brief_data()

    def as_list(self):
        return self.as_base().defer("detailed").with_blogposts_tagged_count()

    def as_retrieved(self):
        return self.as_base().with_updated_by_brief_data()

    def with_blogposts_tagged_count(self):
        return self.annotate(
            blogposts_tagged_count=Count("blogposts_tagged", distinct=True)
        )
