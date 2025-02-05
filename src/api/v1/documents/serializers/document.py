from rest_framework import serializers
from apps.documents.models import Document
from apps.authorisation.models import CustomUser

class BlogpostListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    detailed = serializers.CharField()
    documents_album = serializers.PrimaryKeyRelatedField(read_only=True)
    created_at = serializers.DateTimeField()
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    # created_by_string = serializers.CharField()
    updated_at = serializers.DateTimeField()
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)
    # updated_by_string = serializers.CharField()