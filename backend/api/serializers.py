from rest_framework import serializers
from base import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'
