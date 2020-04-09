from rest_framework.serializers import ModelSerializer
from modules.kanban.models.card import Card


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('pipe_line', 'title', 'content', 'updated_at')
