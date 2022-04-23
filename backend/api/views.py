from rest_framework.decorators import api_view
from rest_framework.response import Response
from base import models
from . import serializers


@api_view(['GET'])
def list_items(request):
    s = serializers.ItemSerializer(
        instance=models.Item.objects.all(), many=True)
    return Response(s.data)


@api_view(['POST'])
def create_items(request):
    s = serializers.ItemSerializer(data=request.data, many=True)
    if s.is_valid():
        s.save()
        return Response({'msg': 'Saved successfuly'})
    return Response({'msg': 'Error occured'})
