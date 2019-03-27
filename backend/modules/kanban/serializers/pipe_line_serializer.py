from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from modules.kanban.models.pipe_line import PipeLine


class PipeLineSerializer(ModelSerializer):
    card_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='card-detail'
    )

    class Meta:
        model = PipeLine
        fields = ('name', 'updated_at', 'card_set')
