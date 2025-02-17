from rest_framework import serializers
from common.api import serializers as commons
from apps.blog.models import Blogpost, BlogRubric


class BlogRubricRelationBriefSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()


class BlogpostTagRelationBriefSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()


class BlogpostBaseSerializer(
    commons.WithCreatedSerializerMixin, serializers.Serializer
):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    subtitle = serializers.ReadOnlyField()
    blog_rubric = BlogRubricRelationBriefSerializer()
    blogpost_tags = BlogpostTagRelationBriefSerializer(many=True)
    blogpost_likes_count = serializers.ReadOnlyField()


class BlogpostListSerializer(BlogpostBaseSerializer):
    figures_count = serializers.ReadOnlyField()
    blogpost_comments_count = serializers.ReadOnlyField()


class BlogpostRetrievedSerializer(
    commons.WithUpdatedSerializerMixin, BlogpostBaseSerializer
):
    detailed = serializers.ReadOnlyField()


class BlogpostFormSerializer(
    commons.WithCreatedFormSerializerMixin,
    commons.WithUpdatedFormSerializerMixin,
    serializers.Serializer,
):

    INSTANCE_MODEL = Blogpost

    title = serializers.CharField(max_length=127)
    subtitle = serializers.CharField(max_length=255, allow_blank=True)
    detailed = serializers.CharField(allow_blank=True)
    blog_rubric = serializers.PrimaryKeyRelatedField(queryset=BlogRubric.objects.all())

    INSTANCE_UPDATABLE_FIELDS = [
        "title",
        "subtitle",
        "detailed",
        "blog_rubric",
        "updated_by",
    ]

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