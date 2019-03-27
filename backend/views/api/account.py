from rest_framework.response import Response
from modules.kanban.serializers.user_serializer import UserSerializer
from .base import BaseAPIView


class AccountAPIView(BaseAPIView):

    def get(self, request):
        account = self.current_user
        if account.is_authenticated:
            serializer = UserSerializer(account)
            return Response({
                'account_info': serializer.data
            })

        return Response({
            'account_info': None,
        })
