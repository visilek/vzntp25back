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
    BlogpostTagRetrieveSerializer,
)


class BlogpostTagViewset(ViewSet):

    API_QS = BlogpostTag.api_v1
    INSTANCE_LIST_SERIALIZER = BlogpostTagListSerializer
    INSTANCE_RETRIEVE_SERIALIZER = BlogpostTagRetrieveSerializer
    LIST_FILTERS = []

    def get_object(self, pk):
        qs = self.API_QS.as_detailed()
        obj = get_object_or_404(qs, pk=pk)
        return obj

    def list(self, request):
        qs = self.API_QS.as_list().filter_by_request(request, self.LIST_FILTERS)
        serializer = self.INSTANCE_LIST_SERIALIZER(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = self.INSTANCE_RETRIEVE_SERIALIZER(obj)
        return Response(serializer.data)
