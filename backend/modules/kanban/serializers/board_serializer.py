from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from modules.kanban.models.board import Board


class BoardSerializer(ModelSerializer):
    pipeline_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pipeline-detail'
    )

    class Meta:
        model = Board
        fields = ('id', 'name', 'pipeline_set')
