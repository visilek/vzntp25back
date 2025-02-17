from rest_framework import serializers
from common.api.serializers import (
    CreatedByRelationBriefSerializer,
    UpdatedByRelationBriefSerializer,
)


class CoverFigureRelationBriefSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    file = serializers.CharField()


class BlogRubricBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    created_by = CreatedByRelationBriefSerializer()
    cover_figure = CoverFigureRelationBriefSerializer()


class BlogRubricListSerializer(BlogRubricBaseSerializer):
    blogposts_count = serializers.IntegerField()


class BlogRubricRetrieveSerializer(BlogRubricBaseSerializer):
    detailed = serializers.CharField()
    updated_at = serializers.DateTimeField()
    updated_by = UpdatedByRelationBriefSerializer()