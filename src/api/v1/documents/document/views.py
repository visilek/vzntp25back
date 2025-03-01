# Django & DRF imports
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser, FormParser
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
    DocumentFormSerializer,
)
from common.storage import uploading_path


class DocumentViewset(ViewSet):

    parser_classes = (MultiPartParser, FormParser)

    model_manager = Document.api_v1

    instance_list_serializer = DocumentListSerializer
    instance_retrieved_serializer = DocumentRetrievedSerializer
    instance_form_serializer = DocumentFormSerializer

    allowed_list_filter_keys = [
        "documents_album",
    ]

    def list(self, request):
        qs = self.model_manager.as_list().filter_by_request(
            request,
            filter_keys=self.allowed_list_filter_keys,
        )
        serializer = self.instance_list_serializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model_manager.as_retrieved(), pk=pk)
        serializer = self.instance_retrieved_serializer(obj)
        return Response(serializer.data)

    # def create(self, request):
    #     print(request.data)
    #     print(request.FILES.get("file"))
    #     try:
    #         # ЗАМЕНИТЬ НА ВЫБОР ПОЛЬЗОВАТЕЛЯ ИЗ ПАРАМЕТРОВ ЗАПРОСА!!!
    #         author = 1
    #         data = request.data | {"created_by": author, "updated_by": author}
    #         request_serializer = self.instance_form_serializer(data=data)

    #         # !!! УБРАТЬ КОСТЫЛЬ !!!
    #         for key, val in request.data.items():
    #             if key in ["title", "detailed", "documents_album", "file"]:
    #                 val = val[0]
    #         # !!! КОНЕЦ КОСТЫЛЯ

    #         import pdb
    #         pdb.set_trace()

    #         if request_serializer.is_valid():
    #             uploaded_file = serializer.validated_data["file"]

    #             save_path = uploading_path.get_path(
    #                 instance=None,
    #                 filename=uploaded_file.name,
    #                 app_name="documents",
    #                 model_name="document",
    #             )

    #             with open(save_path, "wb+") as destination:
    #                 for chunk in uploaded_file.chunks():
    #                     destination.write(chunk)
    #             request_serializer.save()
    #             return Response(request_serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(
    #                 request_serializer.errors,
    #                 status=status.HTTP_422_UNPROCESSABLE_ENTITY,
    #             )
    #     except Exception as e:
    #         print("Exception on blog rubric create:", e)
    #         return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)
