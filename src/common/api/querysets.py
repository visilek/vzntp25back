class FilterableByRequestMixin:
    def parse_multiple_options_string(self, options_string):
        return [int(option) for option in str(options_string).split()]

    def filter_by_request(self, request, filter_keys=[]):
        for key, value in request.GET.items():
            if key in filter_keys:
                try:
                    self = getattr(self, f"by_{key}")(value)
                except NotImplementedError as e:
                    print(e)
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
