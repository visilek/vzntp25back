# Django & DRF imports
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Thidr party imports
from http import HTTPMethod

# Own modules imports
from apps.blog.models import BlogpostTag
from .serializers import (
    BlogpostTagListSerializer,
    BlogpostTagRetrievedSerializer,
)


class BlogpostTagViewset(ViewSet):

    model_manager = BlogpostTag.api_v1

    instance_list_serializer = BlogpostTagListSerializer
    instance_retrieved_serializer = BlogpostTagRetrievedSerializer

    allowed_list_filter_keys = []

    def get_object(self, pk):
        qs = self.model_manager.as_retrieved()
        obj = get_object_or_404(qs, pk=pk)
        return obj

    def list(self, request):
        qs = self.model_manager.as_list().filter_by_request(
            request, self.allowed_list_filter_keys
        )
        serializer = self.instance_list_serializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = self.instance_retrieved_serializer(obj)
        return Response(serializer.data)
