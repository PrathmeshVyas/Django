from urllib import response
from html5lib import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import items
from .serializers import itemserializers

@api_view(['GET'])
def getData(request):
   item = items.objects.all()
   serializer = itemserializers(item, many=True)
   return Response(serializer.data)

@api_view(['POST'])
def additem(request):
    serializer = itemserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    