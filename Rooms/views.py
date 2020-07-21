from django.shortcuts import render
from .serializers import RoomSerializer, RoomCategorySerializer
from .models import Room, RoomCategory
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly



# Create your views here.

class RoomListCreateAPI(ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    name = 'room-list'
    permission_classes =[permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(creator = self.request.creator)


class RoomUpdateAPI(RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    name = 'update-room'
    permission_classes =[permissions.IsAuthenticated]

class RoomDeleteAPI(RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    name = 'delete-room'

class RoomRetrieveAPI(RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    name = 'get-room' 
    lookup_field ='pk'


"""class RoomViewSet(viewsets.ReadOnlyModelViewSet):
   
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
"""
class RoomCategoryViewset(viewsets.ModelViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer



