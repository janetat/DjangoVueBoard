from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, DateTimeField

from modules.kanban.models.pipe_line import PipeLine


class PipeLineSerializer(ModelSerializer):
    updated_at = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    card_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='card-detail'
    )

    class Meta:
        model = PipeLine
        fields = ('board', 'name', 'updated_at', 'card_set')
