from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    # safe allowos list to turn inot json list 
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    # many objects of json are returned
    serializer = RoomSerializer(rooms,many=True)
    # rooms is a python object(object cannot be converted to json)
    return Response(serializer.data)

    
@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id = pk)
    # many used for multiple objects to return
    # in this case not multiple are returned only 1 is returned
    serializer = RoomSerializer(room , many=False)
    # rooms is a python object(object cannot be converted to json)
    return Response(serializer.data)