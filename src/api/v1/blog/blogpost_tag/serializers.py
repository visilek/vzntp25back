from rest_framework import serializers
from common.api import serializers as commons


class BlogpostTagBaseSerializer(
    commons.WithCreatedSerializerMixin, serializers.Serializer
):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()


class BlogpostTagListSerializer(BlogpostTagBaseSerializer):
    blogposts_tagged_count = serializers.ReadOnlyField()


class BlogpostTagRetrievedSerializer(
    commons.WithUpdatedSerializerMixin, BlogpostTagBaseSerializer
):
    detailed = serializers.ReadOnlyField()
