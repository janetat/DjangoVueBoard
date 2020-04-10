from rest_framework.serializers import ModelSerializer, DateTimeField
from modules.kanban.models.card import Card


class CardSerializer(ModelSerializer):
    updated_at = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Card
        fields = ('pipe_line', 'title', 'content', 'updated_at')
