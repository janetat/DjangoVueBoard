from django.db.models.query import QuerySet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from modules.kanban.models.board import Board
from modules.kanban.serializers.board_serializer import BoardSerializer
from .authentication.csrf_exempt_auth import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication


class BoardAPIVIew(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    # TODO 现在的认证方式为基于Session且关闭了csrf的认证方式，可以改变为其他认证方式
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # HTTP GET
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'board_list': serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'board_list': serializer.data
        })

    # HTTP POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'board_data': serializer.data,

        }, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.filter(owner=self.request.user)
        return queryset
