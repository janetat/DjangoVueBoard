from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from modules.kanban.models.pipe_line import PipeLine
from modules.kanban.serializers.pipe_line_serializer import PipeLineSerializer


class PipeLineAPIView(ModelViewSet):
    queryset = PipeLine.objects.all()
    serializer_class = PipeLineSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'pipelines_list': serializer.data
            })

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'pipelines_list': serializer.data
        })
