from rest_framework import serializers
from common.api import serializers as commons
from apps.blog.models import BlogRubric
from apps.figures.models import Figure


class CoverFigureRelationBriefSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    file = serializers.CharField(read_only=True)


class BlogRubricBaseSerializer(
    commons.WithCreatedSerializerMixin, serializers.Serializer
):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    cover_figure = CoverFigureRelationBriefSerializer()


class BlogRubricListSerializer(BlogRubricBaseSerializer):
    blogposts_count = serializers.IntegerField()


class BlogRubricRetrievedSerializer(
    commons.WithUpdatedSerializerMixin, BlogRubricBaseSerializer
):
    detailed = serializers.CharField()


class BlogRubricFormSerializer(
    commons.WithCreatedFormSerializerMixin,
    commons.WithUpdatedFormSerializerMixin,
    serializers.Serializer,
):

    INSTANCE_MODEL = BlogRubric

    title = serializers.CharField(max_length=127)
    detailed = serializers.CharField(allow_blank=True)
    cover_figure = serializers.PrimaryKeyRelatedField(queryset=Figure.objects.all())

    INSTANCE_UPDATABLE_FIELDS = [
        "title",
        "detailed",
        "cover_figure",
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
