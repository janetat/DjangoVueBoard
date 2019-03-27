from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    account_id = serializers.IntegerField(source='id')
    name = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ('account_id', 'name')
