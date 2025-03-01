from rest_framework import serializers
from common.api import serializers as commons
from apps.documents.models import Document


class DocumentsAlbumCoverFigureRelationPathSerializer(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    file = serializers.CharField(read_only=True)

class DocumentsAlbumRelationBriefSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()

class DocumentsAlbumRelationCoveredBriefSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    cover_figure = DocumentsAlbumCoverFigureRelationPathSerializer()


class DocumentBaseSerializer(
    commons.WithCreatedSerializerMixin, serializers.Serializer
):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    file = serializers.CharField(read_only=True)


class DocumentListSerializer(DocumentBaseSerializer):
    documents_album = DocumentsAlbumRelationBriefSerializer()


class DocumentRetrievedSerializer(
    commons.WithUpdatedSerializerMixin, DocumentBaseSerializer
):
    detailed = serializers.ReadOnlyField()
    documents_album = DocumentsAlbumRelationCoveredBriefSerializer()


class DocumentFormSerializer(
    commons.WithCreatedFormSerializerMixin,
    commons.WithUpdatedFormSerializerMixin,
    serializers.Serializer,
):

    INSTANCE_MODEL = Document

    title = serializers.CharField(max_length=127)
    detailed = serializers.CharField(allow_blank=True)
    file = serializers.FileField()

    INSTANCE_UPDATABLE_FIELDS = [
        "title",
        "detailed",
        "file",
        "updated_by",
    ]

    def create(self, validated_data):
        return self.INSTANCE_MODEL.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     for attr_name in self.INSTANCE_UPDATABLE_FIELDS:
    #         setattr(
    #             instance,
    #             attr_name,
    #             validated_data.get(attr_name, getattr(instance, attr_name)),
    #         )

    #     instance.save()
    #     return instance
