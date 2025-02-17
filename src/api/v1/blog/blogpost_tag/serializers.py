from rest_framework import serializers
from common.api.serializers import (
    CreatedByRelationBriefSerializer,
    UpdatedByRelationBriefSerializer,
)


class BlogpostTagBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    created_at = serializers.DateTimeField()
    created_by = CreatedByRelationBriefSerializer()


class BlogpostTagListSerializer(BlogpostTagBaseSerializer):
    blogposts_tagged_count = serializers.IntegerField()


class BlogpostTagRetrieveSerializer(BlogpostTagBaseSerializer):
    detailed = serializers.CharField()
    updated_at = serializers.DateTimeField()
    updated_by = UpdatedByRelationBriefSerializer()
