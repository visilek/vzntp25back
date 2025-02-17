from rest_framework import serializers
from apps.authorisation.models import CustomUser


class CreatedByRelationBriefSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()


class UpdatedByRelationBriefSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()


class WithCreatedSerializerMixin(metaclass=serializers.SerializerMetaclass):
    created_at = serializers.ReadOnlyField()
    created_by = CreatedByRelationBriefSerializer()

class WithUpdatedSerializerMixin(metaclass=serializers.SerializerMetaclass):
    updated_at = serializers.ReadOnlyField()
    updated_by = CreatedByRelationBriefSerializer()

class WithCreatedFormSerializerMixin(metaclass=serializers.SerializerMetaclass):
    created_at = serializers.DateTimeField(required=False, read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())


class WithUpdatedFormSerializerMixin(metaclass=serializers.SerializerMetaclass):
    updated_at = serializers.DateTimeField(required=False, read_only=True)
    updated_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
