from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from modules.kanban.models import Card
from modules.kanban.serializers.card_serializer import CardSerializer
from .authentication.csrf_exempt_auth import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication


class CardAPIView(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    # HTTP GET
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'card_data': serializer.data
        })

    # HTTP PUT, HTTP PATCH 为 def partial_update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({
            'card_data': serializer.data
        })

    # HTTP DELETE
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True
        }, status=status.HTTP_204_NO_CONTENT)
