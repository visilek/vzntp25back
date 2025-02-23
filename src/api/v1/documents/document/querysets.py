from django.db.models import QuerySet, Count
from common.api import querysets as commons


class DocumentApiQueryset(
    commons.FilterableByRequestMixin,
    commons.WithCreatedByBriefDataMixin,
    commons.WithUpdatedByBriefDataMixin,
    QuerySet,
):

    def as_base(self):
        return self.with_created_by_brief_data()

    def as_list(self):
        return self.as_base().with_documents_album_brief_data()

    def as_retrieved(self):
        return (
            self.as_base()
            .with_updated_by_brief_data()
            .with_documents_album_covered_brief_data()
        )

    def with_documents_album_brief_data(self):
        return self.select_related("documents_album").defer(
            "documents_album__detailed",
            "documents_album__cover_figure",
        )

    def with_documents_album_covered_brief_data(self):
       return self.select_related("documents_album__cover_figure").defer(
            "documents_album__detailed",
            "documents_album__cover_figure__id",
            "documents_album__cover_figure__title",
            "documents_album__cover_figure__detailed",
            "documents_album__cover_figure__figures_album",
        )

    def by_documents_album(self, options_string):
        options = self.parse_multiple_options_string(options_string)
        return self.filter(documents_album__in=options)
