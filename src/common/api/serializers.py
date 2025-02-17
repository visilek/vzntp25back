from rest_framework import serializers
from apps.authorisation.models import CustomUser


class CreatedByRelationBriefSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField()


class UpdatedByRelationBriefSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()