# Django & DRF imports
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Thidr party imports
from http import HTTPMethod

# Own modules imports
from apps.documents.models import Document
from .serializers import (
    DocumentListSerializer,
    DocumentRetrievedSerializer,
)


class DocumentViewset(ViewSet):

    model_manager = Document.api_v1

    instance_list_serializer = DocumentListSerializer
    instance_retrieved_serializer = DocumentRetrievedSerializer
    # instance_form_serializer = DocumentFormSerializer

    allowed_list_filter_keys = [
        "documents_album",
    ]

    def list(self, request):
        qs = self.model_manager.as_list().filter_by_request(
            request, self.allowed_list_filter_keys
        )
        serializer = self.instance_list_serializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model_manager.as_retrieved(), pk=pk)
        serializer = self.instance_retrieved_serializer(obj)
        return Response(serializer.data)
