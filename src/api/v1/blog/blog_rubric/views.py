# Django & DRF imports
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Thidr party imports
from http import HTTPMethod

# Own modules imports
from apps.blog.models import BlogRubric
from .serializers import (
    BlogRubricListSerializer,
    BlogRubricRetrievedSerializer,
    BlogRubricFormSerializer,
)


class BlogRubricViewset(ViewSet):

    model_manager = BlogRubric.api_v1

    instance_list_serializer = BlogRubricListSerializer
    instance_retrieved_serializer = BlogRubricRetrievedSerializer
    instance_form_serializer = BlogRubricFormSerializer

    allowed_list_filter_keys = []

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

    def create(self, request):
        try:
            # ЗАМЕНИТЬ НА ВЫБОР ПОЛЬЗОВАТЕЛЯ ИЗ ПАРАМЕТРОВ ЗАПРОСА!!!
            author = 1
            data = request.data | {"created_by": author, "updated_by": author}
            request_serializer = self.instance_form_serializer(data=data)
            if request_serializer.is_valid():
                request_serializer.save()
                return Response(request_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    request_serializer.errors,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
        except Exception as e:
            print("Exception on blog rubric create:", e)
            return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, pk=None):
        try:
            # ЗАМЕНИТЬ НА ПОДСТАНОВКУ ПОЛЬЗОВАТЕЛЯ ИЗ ЗАПРОСА request.user!!!
            author = 1
            obj = get_object_or_404(self.model_manager.all(), pk=pk)
            data = request.data | {
                "created_by": obj.created_by.pk,
                "updated_by": author,
            }
            request_serializer = self.instance_form_serializer(obj, data=data)
            if request_serializer.is_valid():
                request_serializer.save()
                return Response(request_serializer.data, status=status.HTTP_200_OK)
            else:
                print("invalid serializer", request_serializer.errors)
                return Response(
                    request_serializer.errors,
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )
        except Exception as e:
            print("Exception on blog rubric update:", e)
            return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, pk=None):
        try:
            obj = get_object_or_404(self.model_manager.all(), pk=pk)
            result = obj.delete()
            return Response(
                f"Blog rubric deleted: {result}", status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            print("Exception on blog rubric delete:", e)
            return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)
