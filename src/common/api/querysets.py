class FilterableByRequestMixin:
    def filter_by_request(self, request, allowed_filter_keys):
        for key, value in request.GET.items():
            if key in allowed_filter_keys:
                self = getattr(self, f"by_{key}")(value)
        return self


class WithCreatedByBriefDataMixin:
    def with_created_by_brief_data(self):
        return self.select_related("created_by").defer(
            "created_by__is_active",
            "created_by__is_staff",
            "created_by__date_joined",
        )


class WithUpdatedByBriefDataMixin:
    def with_updated_by_brief_data(self):
        return self.select_related("updated_by").defer(
            "updated_by__is_active",
            "updated_by__is_staff",
            "updated_by__date_joined",
        )
