from datetime import datetime

# Django & DRF imports
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Thidr party imports
from http import HTTPMethod

# Own modules imports
from apps.blog.models import Blogpost
from .querysets import BlogpostApiQueryset
from .serializers import (
    BlogpostListSerializer,
    BlogpostRetrieveSerializer,
    # BlogpostFormSerializer,
)


class BlogpostViewset(ViewSet):

    API_QS = Blogpost.api_v1
    INSTANCE_LIST_SERIALIZER = BlogpostListSerializer
    INSTANCE_RETRIEVE_SERIALIZER = BlogpostRetrieveSerializer
    # INSTANCE_FORM_SERIALIZER = BlogpostFormSerializer

    LIST_FILTERS = [
        "blog_rubric",
        "blogpost_tags",
    ]

    def get_object(self, pk):
        qs = self.API_QS.as_detailed()
        obj = get_object_or_404(qs, pk=pk)
        return obj

    # def get_created_updated_tracking_fields(self, author_id):
    #     timespot = datetime.now()
    #     return {
    #         "created_at": timespot,
    #         "created_by": author_id,
    #         "updated_at": timespot,
    #         "updated_by": author_id,
    #     }

    # def get_updated_tracking_fields(self, author_id):
    #     timespot = datetime.now()
    #     return {
    #         "updated_at": timespot,
    #         "updated_by": author_id,
    #     }

    def list(self, request):
        qs = self.API_QS.as_list().filter_by_request(request, self.LIST_FILTERS)
        serializer = self.INSTANCE_LIST_SERIALIZER(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = self.INSTANCE_RETRIEVE_SERIALIZER(obj)
        return Response(serializer.data)

    # def create(self, request):
    #     try:
    #         # ЗАМЕНИТЬ НА ВЫБОР ПОЛЬЗОВАТЕЛЯ ИЗ ПАРАМЕТРОВ ЗАПРОСА!!!
    #         author = 1
    #         data = request.data | self.get_created_updated_tracking_fields(author)
    #         request_serializer = self.INSTANCE_FORM_SERIALIZER(data=data)
    #         if request_serializer.is_valid():
    #             request_serializer.save()
    #             return Response(request_serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(
    #                 request_serializer.errors,
    #                 status=status.HTTP_422_UNPROCESSABLE_ENTITY,
    #             )
    #     except Exception as e:
    #         print("Exception on blogpost create:", e)
    #         return Response(e, status=status.HTTP_406_NOT_ACCEPTABLE)