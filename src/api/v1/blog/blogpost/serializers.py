from rest_framework import serializers
from common.api.serializers import (
    CreatedByRelationBriefSerializer,
    UpdatedByRelationBriefSerializer,
)
from apps.blog.models import Blogpost, BlogRubric
from apps.authorisation.models import CustomUser


class BlogRubricRelationBriefSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class BlogpostTagRelationBriefSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class BlogpostBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    subtitle = serializers.CharField()
    created_at = serializers.DateTimeField()
    created_by = CreatedByRelationBriefSerializer()
    blog_rubric = BlogRubricRelationBriefSerializer()
    blogpost_tags = BlogpostTagRelationBriefSerializer(many=True)
    blogpost_likes_count = serializers.IntegerField()


class BlogpostListSerializer(BlogpostBaseSerializer):
    figures_count = serializers.IntegerField()
    blogpost_comments_count = serializers.IntegerField()


class BlogpostRetrieveSerializer(BlogpostBaseSerializer):
    detailed = serializers.CharField()
    updated_at = serializers.DateTimeField()
    updated_by = UpdatedByRelationBriefSerializer()


class BlogpostFormSerializer(serializers.Serializer):

    INSTANCE_MODEL = Blogpost
    INSTANCE_UPDATABLE_FIELDS = [
        "title",
        "subtitle",
        "detailed",
        "blog_rubric",
        "updated_at",
        "updated_by",
    ]

    title = serializers.CharField(max_length=127)
    subtitle = serializers.CharField(max_length=255, allow_blank=True)
    detailed = serializers.CharField(allow_blank=True)
    blog_rubric = serializers.PrimaryKeyRelatedField(queryset=BlogRubric.objects.all())
    created_at = serializers.DateTimeField(required=False, read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    updated_at = serializers.DateTimeField(required=False, read_only=True)
    updated_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    def create(self, validated_data):
        return self.INSTANCE_MODEL.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr_name in self.INSTANCE_UPDATABLE_FIELDS:
            setattr(
                instance,
                attr_name,
                validated_data.get(attr_name, getattr(instance, attr_name)),
            )
        instance.save()
        return instance
